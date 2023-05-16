from flask import *
from database import init_db, db_session
from models import *
from internship_manager import *
from helper import *

from sqlalchemy import desc, or_


app = Flask(__name__)

# TODO: Change the secret key
app.secret_key = "vRghFoiVXCFNulgLLg=="


# TODO: Fill in methods and routes



@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route("/trending",methods=["GET","POST"])
def trending():
    is_student = session.get("is_student",False)
    if request.method == "POST":
            #Finds internship that user is interested in and increases its num_interested variable by 1
            internship_name = request.form["internship_name"]
            target_internship = db_session.query(Internship).where(Internship.name == internship_name).first()
            target_internship.num_interested += 1
            current_user = db_session.query(Student).where(Student.username == session.get("user_id",None)).first()
            current_user.internships.append(target_internship)
            db_session.commit()
    #Find the 6 internships with the largest numbers of interested students, and pass those internships as cards to "trending.html"
    trending_internships = db_session.query(Internship).order_by(desc(Internship.num_interested)).limit(6).all()
    cards = get_cards(trending_internships)
    return render_template("trending.html",cards=cards,is_student = is_student)


    

@app.route("/interests",methods=["GET","POST"])
def interests():
    #Find the current user and the internships that align with the user's tags, and pass those internships as cards
    current_user = db_session.query(Student).where(Student.username == session.get('user_id',None)).first()
    internship_feed = db_session.query(Internship).filter(Internship.tags.any(Tag.id.in_([tag.id for tag in current_user.tags]))).all()
    cards = get_cards(internship_feed)
    if request.method == "GET":
        return render_template("interests.html",cards=cards,is_student = True)
    if request.method == "POST":
        #Flash a warning to a student if the internship they searched for doesn't exist in database
        internship_name = request.form["internship_search"]
        target_internship = db_session.query(Internship).where(Internship.name == internship_name).first()
        if target_internship == None:
            flash("Internship does not exist","warning")
            return render_template("interests.html",cards=cards,is_student=True)
        else:
            cards = get_cards([target_internship])
            return render_template("search_results.html",cards=cards)

   



@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("login.html",login_message = None)
    if request.method == "POST":
        #Authenticate the user's username, password, and status (admin or student)  
        username = request.form["username"]
        password = request.form["password"]
        existing_student= db_session.query(Student).where(Student.username == username).first()
        existing_admin = db_session.query(Administrator).where(Administrator.username == username).first()
        if existing_student:
            '''
            Use a session object to store the current user's information for database queries

            is_student: determines whether current user is a student
            user_id: gets current user's username
            '''
            session['is_student'] = True
            session['user_id'] = existing_student.username
            return redirect(url_for("interests"))
        elif existing_admin:
            session['is_student'] = False
            session['user_id'] = existing_admin.username
            return redirect(url_for('add_internship'))
        else:
            flash("Login Unsuccessful","warning") 
            return render_template("login.html")


@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    if request.method == "POST":
        #Add the user's username, password, and status (admin or student) to the database
        admin_box = request.form.get('admin_box')
        username = request.form.get('username')
        password = request.form.get('password')
        new_user = None
        if admin_box:
            #Lines 109 and 122: These lines of code were modified from ChatGPT
            if not db_session.query(Administrator).where(or_(Administrator.username == username, Administrator.password == password)).first():
                new_user = Administrator(username,password)
                db_session.add(new_user)
                db_session.commit()
            else:
                flash("Username or password already exists","warning")
                return render_template("signup.html")
        else:
            '''
            If user is a student, ensure that their interest tags exist in the database.
            This allows for their interests.html page to be populated with internships that
            have tags corresponding to this user's tags.
            '''
            if not db_session.query(Student).where(or_(Student.username == username, Student.password == password)).first():
                new_user = Student(username,password)
                interests = request.form.get('interests').split(",")
                tag_exists = add_student_tags(new_user,interests)
            else:
                flash("Username or password already exists","warning")
                return render_template("signup.html")
            if not tag_exists:
                flash("One or more tags do not yet exist. Try Again.","warning")
                return render_template("signup.html")
            else:
                db_session.add(new_user)
                db_session.commit()
        return redirect(url_for("home"))
            

        
@app.route("/add-internship",methods=["GET","POST"])
def add_internship():
     if request.method == "GET":
        return render_template("add_internship.html",add_internship_message = None)
     if request.method == "POST":
         #Add an internship based on form responses to the database
         name = request.form["internship_name"]
         duration = request.form["duration"]
         start_date = request.form["start_date"]
         end_date = request.form["end_date"]
         location = request.form["location"]
         link = request.form["link"]
         #Line 140: splits the tags into a list where each element has the format: tag/image_link
         tags = request.form["tags"].split(",")
         administrator_id = session.get("user_id",None)
         new_internship = Internship(name,duration,start_date,end_date,location,link,administrator_id)
         '''
         Iterate through list of tags in user's reponse, extract each tag's content and image link, and use this
         information to create a new tag object and add it to the database
         '''
         for tag in tags:
             tag_content,_,tag_image = tag.partition("/")
             new_internship.tags.append(Tag(tag_content,tag_image))
         db_session.add(new_internship)
         db_session.commit()
         return redirect(url_for("trending"))
       



if __name__ == "__main__":
    init_db()
    #Add administrators and internships so the website is functional for demonstration
    add_internships()
    app.run(debug=True, port=5002)

from flask import *
from database import init_db, db_session
from models import *
from Internship_Manager import add_internships
from sqlalchemy import desc #CHECK THIS

app = Flask(__name__)

# TODO: Change the secret key
app.secret_key = "512345"


# TODO: Fill in methods and routes

@app.route("/trending")
def trending():
   trending_internships = db_session.query(Internship).all()
   cards = []
   for internship in trending_internships:
        cards.append({
            "title":internship.name,
            "image_url": db_session.join(Tag, StudentTag).where(Tag.id == StudentTag.tag_id) #cHANGE THIS UP

            
        })
   return render_template("trending.html", cards=cards)


@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("login.html",login_message = None)
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        get_student = 2 == 3
        if get_student == False:
            flash("Login Unsuccessful","warning") #WOULD THIS BE WARNING or INFO?
        else:
            return redirect(url_for("trending"))
    return render_template("login.html")

@app.route("/interests")
def interests():
    return render_template("interests.html")

@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    if request.method == "POST":
        interests = request.form["interests"].split()
        username = request.form["username"]
        password = request.form["password"]
        new_student = Student(username,password)
        db_session.add(new_student)
        for interest in interests:
            new_tag = Tag(interest)
            db_session.add(new_tag)
            new_student.tags.append(new_tag)
        db_session.commit()

    return redirect(url_for("trending"))
        




if __name__ == "__main__":
    init_db()
    add_internships()
    app.run(debug=True, port=5002)

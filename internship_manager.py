from models import *
from database import init_db, db_session

def add_internships():

    #Clear database tables 
    db_session.query(Internship).delete()
    db_session.query(Administrator).delete()
    db_session.query(Student).delete()

   
    #Create administrators
    admin1 = Administrator("admin1","admin1")
    admin2 = Administrator("admin2","admin2")
    admin3 = Administrator("admin3","admin3")

    
    #Create internships
    internship1 = Internship("Research Science Institute","6 weeks","June 20","August 2","MIT","https://www.cee.org/programs/research-science-institute","admin1")
    internship2 = Internship("Summer Science Program","5 weeks","June 24","July 27","New Mexico","https://summerscience.org/","admin1")
    internship3 = Internship("Google Engineering Practicum", "12 weeks","June 14","September 3","Remote","https://buildyourfuture.withgoogle.com/programs/step","admin1")
    internship4 = Internship("Microsoft Explore","10 weeks","June 21", "August 27", "Redmond, WA","https://careers.microsoft.com/students/us/en/usexploremicrosoftprogram","admin1")
    internship5 = Internship("Facebook University","8 weeks", "June 14","August 6", "Various Locations","https://www.metacareers.com/careerprograms/pathways/metauniversity","admin2")
    internship6 = Internship("Salesforce Internship","12 weeks","June 7","August 27","Remote","https://www.salesforce.com/company/careers/university-recruiting/summer-internship/","admin2")
    internship7 = Internship("Goldman Sachs Engineering Practicum","10 weeks","June 7", "August 23","New York, NY","https://www.google.com/search?q=goldman+sachs+engineering+practicum&oq=goldman+sachs+engineering+practicum&aqs=chrome..69i57j0i22i30l5j0i390i650l3.5866j0j7&sourceid=chrome&ie=UTF-8&safe=active&ssui=on","admin2")
    internship8 = Internship("NASA Internships","10 weeks","June 7","August 13", "Various Locations","https://intern.nasa.gov/","admin2")
    internship9 = Internship("Y Combinator Fellowship","8 weeks","June 14","August 6", "Remote","https://www.google.com/search?q=y+combinator+fellowship&oq=y+combinator+fellows&aqs=chrome.0.0i512j69i57j0i22i30j0i390i650l4j69i64l2.2174j0j7&sourceid=chrome&ie=UTF-8&safe=active&ssui=on","admin3")
    internship10 = Internship("Disney Imagineering","12 weeks","June 7", "August 27", "Glendale, CA","https://sites.disney.com/waltdisneyimagineering/internships/","admin3")
    internship11 = Internship("JPL Summer Internship","10 weeks","June 7","August 13", "Pasadena, CA","https://www.jpl.nasa.gov/edu/intern/apply/summer-internship-program/","admin3")
    internship12 = Internship("IBM Extreme Blue","12 weeks","June 7","August 27","Various Locations","https://www.ibm.com/blogs/jobs/extreme-blue-ibms-leadership-program-for-future-tech-business-leaders/","admin3")



    # Create tags
    tag1 = Tag("science","data:image/jpeg;base64,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")
    tag2 = Tag("engineering","data:image/jpeg;base64,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")
    tag3 = Tag("technology","https://static.vecteezy.com/system/resources/previews/006/430/145/original/technology-background-concept-circuit-board-electronic-system-futuristic-hi-tech-light-on-dark-blue-free-vector.jpg")
    tag4 = Tag("business","https://static.vecteezy.com/system/resources/thumbnails/007/951/672/small/cityscape-on-white-background-building-perspective-modern-building-in-the-city-skyline-city-silhouette-city-skyscrapers-business-center-vector.jpg")
    tag5 = Tag("finance","https://static.vecteezy.com/system/resources/thumbnails/011/898/241/small/illustration-of-business-finance-banking-and-economic-growth-background-vector.jpg")

    # Add tags to internships
    internship1.tags.append(tag1)
    internship2.tags.append(tag1)
    internship3.tags.append(tag2)
    internship4.tags.append(tag2)
    internship5.tags.append(tag3)
    internship6.tags.append(tag3)
    internship7.tags.append(tag4)
    internship8.tags.append(tag1)
    internship9.tags.append(tag5)
    internship10.tags.append(tag2)
    internship11.tags.append(tag1)
    internship12.tags.append(tag2)

    #Assign internships to administrators
    admin1.internships.append(internship1)
    admin1.internships.append(internship2)
    admin1.internships.append(internship3)
    admin1.internships.append(internship4)
    admin2.internships.append(internship5)
    admin2.internships.append(internship6)
    admin2.internships.append(internship7)
    admin2.internships.append(internship8)
    admin3.internships.append(internship9)
    admin3.internships.append(internship10)
    admin3.internships.append(internship11)
    admin3.internships.append(internship12)


    # Add internships to the session
    db_session.add(internship1)
    db_session.add(internship2)
    db_session.add(internship3)
    db_session.add(internship4)
    db_session.add(internship5)
    db_session.add(internship6)
    db_session.add(internship7)
    db_session.add(internship8)
    db_session.add(internship9)
    db_session.add(internship10)
    db_session.add(internship11)
    db_session.add(internship12)

    #Commit changes to database
    db_session.commit()

from flask import *
from database import init_db, db_session
from models import *

def get_cards(internships):
    '''
    Create a card for each internship in the list of internships
    internships: list of internship objects
    Source: This code was modified from ChatGPT
    '''
    cards = []
    internship_counter = 0
    for internship in internships:
            internship_counter += 1
            cards.append({
                "counter":str(internship_counter), 
                "title":internship.name,
                "image_url":db_session.query(Tag).first().tag_image,
                "duration":internship.duration,
                "start_date":internship.start_date,
                "end_date":internship.end_date,
                "location":internship.location,
                "num_interested":internship.num_interested,
                "link":internship.link
            })
    return cards


def add_student_tags(student,tag_input):
    '''
    Given a list of several tags' contents (inputted by the user) and a student object,
    create new tag objects, add them to the database, and connect these
    tag objects to the given user
    student: student object
    tag_input: list of strings where each string is a tag's content
    '''
    in_db = False
    for tag_content in tag_input:
        target_tag = db_session.query(Tag).where(Tag.content == tag_content).first()
        if target_tag:
            in_db = True
            student.tags.append(target_tag)
    return in_db
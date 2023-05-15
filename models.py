"""
The file that holds the schema/classes
that will be used to create objects
and connect to data tables.
"""

from sqlalchemy import ForeignKey, Column, INTEGER, TEXT
from sqlalchemy.orm import relationship
from database import Base

# TODO: Complete your models

class Student(Base):
    __tablename__ = "students"
    username = Column("username",TEXT,primary_key=True)
    password = Column("password",TEXT,nullable=False)

  
    internships = relationship("Internship",secondary="studentinternships",back_populates="students")
    tags = relationship("Tag",secondary="studenttags",back_populates = "students")


    def __init__(self,username,password):
        self.username = username
        self.password = password


class StudentInternship(Base):
    __tablename__ = "studentinternships"
    id = Column("id",INTEGER,primary_key = True)
    student_id = Column("student_id",ForeignKey("students.username"))
    internship_id = Column("internship_id",ForeignKey("internships.name"))

class Internship(Base):
    __tablename__ = "internships"
    name = Column("name",TEXT,nullable=False,primary_key=True)
    duration = Column("duration",TEXT,nullable=False)
    start_date = Column("start_date",TEXT,nullable=False)
    end_date = Column("end_date",TEXT,nullable=False)
    num_interested = Column("num_interested",INTEGER,nullable=False,default=0)
    location = Column("location",TEXT,nullable=False)
    link = Column("link",TEXT,nullable=False)
    administrator_id = Column(INTEGER,ForeignKey("administrators.username"))

    students = relationship("Student",secondary="studentinternships",back_populates="internships")
    tags = relationship("Tag",secondary="internshiptags",back_populates = "internships")
    administrator = relationship("Administrator",back_populates = "internships") #I want a collection of them

    def __init__(self,name,duration,start_date,end_date,location,link,administrator_id):
       self.name = name
       self.duration = duration
       self.start_date = start_date
       self.end_date = end_date
       self.location = location
       self.link = link
       self.administrator_id = administrator_id

class InternshipTag(Base):
    __tablename__ = "internshiptags"
    id = Column("id",INTEGER,primary_key = True)
    internship_id = Column("internship_id",ForeignKey("internships.name")) #would you call it id if it is just a name
    tag_id = Column("tag_id",ForeignKey("tags.id"))


class StudentTag(Base):
    __tablename__ = "studenttags"
    id = Column("id",INTEGER,primary_key = True)
    student_id = Column("student_id",ForeignKey("students.username"))
    tag_id = Column("tag_id",ForeignKey("tags.id"))

class Administrator(Base):
    __tablename__ = "administrators"
    username = Column("username",TEXT,primary_key=True,nullable=False)
    password = Column("password",TEXT,nullable=False)

    def __init__(self,username,password):
        self.username = username
        self.password = password

    internships = relationship("Internship",back_populates="administrator")

class Tag(Base):
    # TODO: Complete the class
    __tablename__ = "tags"
    id = Column("id",INTEGER,primary_key = True)
    content = Column("content",TEXT,nullable = False)
    tag_image = Column("tag_image",TEXT,nullable = False)

    def __init__(self,content,tag_image):
        self.content = content
        self.tag_image = tag_image

    internships = relationship("Internship",secondary="internshiptags",back_populates="tags")
    students = relationship("Student",secondary = "studenttags",back_populates = "tags")




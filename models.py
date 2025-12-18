from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

degreeCourses = db.Table( #Mit hilfe von ChatGPT erstellt
    "degree_courses",
    db.Column("degree_id", db.Integer, db.ForeignKey("degrees.id_degree"), primary_key=True),
    db.Column("course_id", db.Integer, db.ForeignKey("courses.id_course"), primary_key=True), 
)

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = False)
    role = db.Column(db.String(25), nullable = False, default = "Student")

class Professor(db.Model):
    __tablename__ = "professors"
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(255))
    title = db.Column(db.String(50))
    surname = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)

    teaching_style = db.Column(db.Integer, nullable=False)
    selfstudy = db.Column(db.Integer, nullable=False)
    character = db.Column(db.Integer, nullable=False)
    digital = db.Column(db.Integer, nullable=False)
    ai_usage = db.Column(db.Integer, nullable=False)
    theses_is_supervisor = db.Column(db.Boolean, nullable=False, default=False)

class Degree(db.Model):
    __tablename__= "degrees"
    id_degree = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    semester_amount = db.Column(db.Integer, nullable=False)
    corny_quote = db.Column(db.String(255), nullable=True)

    courses = db.relationship("Course", secondary=degreeCourses, back_populates="degrees")

class Course(db.Model):
    __tablename__= "courses"
    course_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    difficulty = db.Column(db.Integer, nullable=True)

    degrees = db.relationship("Degree", secondary=degreeCourses, back_populates="courses")


class User_Attributes(db.Model):
    __tablename__= "userAttributes"
    id_user = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    teaching_style = db.Column(db.Integer, nullable = False)
    selfstudy = db.Column(db.Integer, nullable=False)
    character = db.Column(db.Integer, nullable=False)
    digital = db.Column(db.Integer, nullable=False)
    ai_usage = db.Column(db.Integer, nullable=False)
    user = db.relationship("User", backref=db.backref("attributes", uselist=False)) 




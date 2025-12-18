from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint


db = SQLAlchemy()

degreeCourses = db.Table( #Mit hilfe von ChatGPT erstellt
    "degree_courses",
    db.Column("degree_id", db.Integer, db.ForeignKey("degrees.id"), primary_key=True),
    db.Column("course_id", db.Integer, db.ForeignKey("courses.id"), primary_key=True), 
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
    description = db.Column(db.Text, nullable=True)

    teaching_style = db.Column(db.Integer, nullable=False)
    selfstudy = db.Column(db.Integer, nullable=False)
    character = db.Column(db.Integer, nullable=False)
    digital = db.Column(db.Integer, nullable=False)
    ai_usage = db.Column(db.Integer, nullable=False)
    theses_is_supervisor = db.Column(db.Boolean, nullable=False, default=False)

    __table_args__ = (
        db.CheckConstraint("teaching_style BETWEEN 1 AND 10", name="chk_prof_teaching_style"),
        db.CheckConstraint("selfstudy BETWEEN 1 AND 10", name="chk_prof_selfstudy"),
        db.CheckConstraint("character BETWEEN 1 AND 10", name="chk_prof_character"),
        db.CheckConstraint("digital BETWEEN 1 AND 10", name="chk_prof_digital"),
        db.CheckConstraint("ai_usage BETWEEN 1 AND 10", name="chk_prof_ai_usage"),
    )

class Degree(db.Model):
    __tablename__= "degrees"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    semester_amount = db.Column(db.Integer, nullable=False)
    corny_quote = db.Column(db.String(255), nullable=True)

    courses = db.relationship("Course", secondary=degreeCourses, back_populates="degrees")

class Course(db.Model):
    __tablename__= "courses"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    difficulty = db.Column(db.Integer, nullable=True)

    degrees = db.relationship("Degree", secondary=degreeCourses, back_populates="courses")


class User_Attributes(db.Model):
    __tablename__= "userAttributes"
    id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    teaching_style = db.Column(db.Integer, nullable = False)
    selfstudy = db.Column(db.Integer, nullable=False)
    character = db.Column(db.Integer, nullable=False)
    digital = db.Column(db.Integer, nullable=False)
    ai_usage = db.Column(db.Integer, nullable=False)
    user = db.relationship("User", backref=db.backref("attributes", uselist=False))

    __table_args__ = (
        db.CheckConstraint("teaching_style BETWEEN 1 AND 10", name="chk_user_teaching_style"),
        db.CheckConstraint("selfstudy BETWEEN 1 AND 10", name="chk_user_selfstudy"),
        db.CheckConstraint("character BETWEEN 1 AND 10", name="chk_user_character"),
        db.CheckConstraint("digital BETWEEN 1 AND 10", name="chk_user_digital"),
        db.CheckConstraint("ai_usage BETWEEN 1 AND 10", name="chk_user_ai_usage"),
    )

    


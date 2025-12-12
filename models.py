import db
from flask_login import UserMixin
from sqlalchemy import func


class User(db.User, UserMixin):

    tablename = "student_users"
    id = db.Column(db.Integer, primary_key=True)
    
class Professor: # Die Professoren Klasse
    def __innit__(
        self,
        id_professor: int,
        image_path: str,
        title: str,
        surname: str,
        name: str,
        description: str, # Kurze Bio des Professors
        teaching_style: int, # Hier wird die Art des Lehrstils definiert 1-10: 1= reiner Frantaluntericht 10= Komplett Gruppenorientiert und interaktiv
        selfstudy: int, # 1= Kompletter Präsenzuntericht 10= 100% self study
        character: int, # 1= MEGA Seriös 10= extremer Witzbold
        digital: int,# 1= Kreide an der Tafel 10= kein Papier erlaubt
        ai_usage: int, # 1= KI ist der Teufel 10= KI ist die christliche Neugeburt
        theses_is_supervisor: bool # Betreut Bachelor/Master?

    ):
    
        self.id_professor = id_professor
        self.image_path = image_path
        self.title = title
        self.surname = surname
        self.name = name
        self.description = description
        self.teaching_style = teaching_style
        self.selfstudy = selfstudy
        self.character = character
        self.digital = digital
        self.ai_usage = ai_usage
        self.theses_is_supervisor = theses_is_supervisor
    def full_name (self):
        return (self.title + " " + self.name + " "+ self.surname)


class Degree:
    def __innit__(
        self,      
        id_degree: int,
        name: str,
        semester_amount: int,
        module1_id: int,
        module2_id: int,
        module3_id: int,
        module4_id: int,
        module5_id: int
        #alle weiteren Module nachtragen
        
    ):
        self.id_degree = id_degree,
        self.name = name
        self.semester_amount = semester_amount
        self.module1_id = module1_id
        self.module2_id = module2_id
        self.module3_id = module3_id
        self.module4_id = module4_id
        self.module5_id = module5_id
        #alle weiteren Moule nachtragen

class Course():
    def __innit__(
            self,
            id_course: str,
            name: str,
            difficulty: int #Die komplexität/Aufwand des Kurses#

    ):
        self.id_course = id_course
        self.name = name
        self.difficulty = difficulty

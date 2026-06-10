from sqlalchemy.orm import DeclarativeBase, Mapped, relationship
import sqlalchemy as db
from datetime import datetime

class Base(DeclarativeBase):
    pass

"""CREATE TABLE Section (
  section_id int NOT NULL,
  section_name varchar(50),
  delegate_id int,
  CONSTRAINT PK_section PRIMARY KEY (section_id)
);
"""
class Section(Base):
    __tablename__ = "section"

    id: Mapped[int] = db.Column(db.Integer, primary_key=True)
    name: Mapped[str] = db.Column(db.String(50))
    # can use alter
    # delegate_id: Mapped[int] = db.Column(db.Integer, db.ForeignKey("student.id"))
    # delegate: Mapped["Student"] = relationship("Student", foreign_keys=[delegate_id])

"""CREATE TABLE Professor (
  professor_id int NOT NULL,
  professor_name varchar(30) NOT NULL,
  professor_surname varchar(30) NOT NULL,
  section_id int NOT NULL,
  professor_office int NOT NULL,
  professor_email varchar(30) NOT NULL,
  professor_hire_date timestamp NOT NULL,
  professor_wage int NOT NULL,
  CONSTRAINT PK_professor PRIMARY KEY (professor_id),
  constraint FK_professor_section foreign key (section_id) references section (section_id)
);"""

class Professor(Base):
    __tablename__ = "professor"

    id: Mapped[int] = db.Column(db.Integer, primary_key=True)
    name: Mapped[str] = db.Column(db.String(30), nullable=False)
    surname: Mapped[str] = db.Column(db.String(30), nullable= False)
    office: Mapped[int] = db.Column(db.Integer, nullable= False)
    email: Mapped[str] = db.Column(db.String(30), nullable= False)
    hire_date: Mapped[datetime] = db.Column(db.DateTime, nullable= False)
    wage: Mapped[int] = db.Column(db.Integer, nullable=False)

    section_id: Mapped[int] = db.Column(db.Integer, db.ForeignKey("section.id"))

    section: Mapped["Section"] = relationship()

"""
CREATE TABLE Course (
  course_id varchar(8) NOT NULL ,
  course_name varchar(200) NOT NULL ,
  course_ects decimal(3,1) NOT NULL,
  professor_id int NOT NULL,
  CONSTRAINT PK_course PRIMARY KEY (course_id),
  constraint FK_course_professor foreign key (professor_id) references professor (professor_id)
);
"""
class Course(Base):
    __tablename__ = "course"

    id: Mapped[int] = db.Column(db.Integer, primary_key=True)
    name: Mapped[str] = db.Column(db.String(200), nullable=True)
    ects: Mapped[float] = db.Column(db.Float, nullable=True)

    professor_id: Mapped[int] = db.Column(db.Integer, db.ForeignKey("professor.id"))

    professor: Mapped["Professor"] = relationship()

"""
CREATE TABLE Student (
  student_id int NOT NULL,
  first_name varchar(50),
  last_name varchar(50),
  birth_date timestamp,
  login varchar(50),
  section_id int,
  year_result int,
  course_id varchar(6) NOT NULL,
  CONSTRAINT PK_student PRIMARY KEY (student_id),
  constraint FK_student_section foreign key (section_id) references section (section_id)
);"""
class Student(Base):
    __tablename__ = "student"

    id: Mapped[int] = db.Column(db.Integer, primary_key=True)
    first_name: Mapped[str] = db.Column(db.String(50))
    second_name: Mapped[str] = db.Column(db.String(50))
    birth_date: Mapped[datetime] = db.Column(db.DateTime)
    login: Mapped[str] = db.Column(db.String(50))
    year_result: Mapped[int] = db.Column(db.Integer)

    # One To Many
    section_id: Mapped[int] = db.Column(db.Integer, db.ForeignKey("section.id"))
    course_id: Mapped[int] = db.Column(db.Integer, db.ForeignKey("course.id"))

    section: Mapped["Section"] = relationship()
    course: Mapped["Course"] = relationship()

"""
CREATE TABLE Grade (
  grade char(2) NOT NULL ,
  lower_bound int NOT NULL,
  upper_bound int NOT NULL,
  CONSTRAINT PK_grade PRIMARY KEY (grade)
);"""
class Grade(Base):
    __tablename__ = "grade"

    grade: Mapped[str] = db.Column(db.String(2), primary_key=True, nullable=False)
    lower_bound: Mapped[int] = db.Column(db.Integer, nullable=False)
    upper_bound: Mapped[int] = db.Column(db.Integer, nullable=False)



engine = db.create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/dbslidealchemy")
## Créer la BD
Base.metadata.create_all(engine)

grade = Grade(grade="IG",lower_bound= 0, upper_bound=7)

session_factory = db.orm.sessionmaker(bind=engine)
session = session_factory()
session.add(grade)

session.commit()
"""INSERT INTO grade VALUES ('IG', 0, 7);
INSERT INTO grade VALUES ('I', 8, 9);
INSERT INTO grade VALUES ('F', 10, 11);
INSERT INTO grade VALUES ('S', 12, 13);
INSERT INTO grade VALUES ('B', 14, 15);
INSERT INTO grade VALUES ('TB', 16, 17);
INSERT INTO grade VALUES ('E', 18, 20);"""

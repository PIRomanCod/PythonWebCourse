import random
from database.db import session
from database.models_sample import Teacher, Student, TeacherStudent



def create_relationship():
    students = session.query(Student).all()
    teachers = session.query(Teacher).all()

    for student in students:
        teacher = random.choice(teachers)
        rel = TeacherStudent(teacher_id=teacher.id, student_id=student.id)
        session.add(rel)
    session.commit()


if __name__ == '__main__':
    create_relationship()
import random
from faker import Faker
from database.db import session
from database.models_sample import Teacher, Student, TeacherStudent

fake = Faker("uk_Ua")


def create_teachers():
    for _ in range(1, 6):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            cell_phone=fake.phone_number(),
            address=fake.address(),
            start_work=fake.date_between(start_date='-10y')
        )
        session.add(teacher)
    session.commit()


def create_students():
    for _ in range(10):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            cell_phone=fake.phone_number(),
            address=fake.address()
        )
        session.add(student)
    session.commit()


def create_relationship():
    students = session.query(Student).all()
    teachers = session.query(Teacher).all()

    for student in students:
        teacher = random.choice(teachers)
        rel = TeacherStudent(teacher_id=teacher.id, student_id=student.id, subject='Math')
        session.add(rel)
    session.commit()



if __name__ == '__main__':
    create_teachers()
    create_students()
    create_relationship()

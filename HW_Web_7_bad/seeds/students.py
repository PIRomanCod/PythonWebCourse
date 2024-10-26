from faker import Faker
from database.db import session
from database.models_sample import Student

fake = Faker("uk_Ua")


def create_students():
    for _ in range(50):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            phone=fake.phone_number(),
            address=fake.address()
        )
        session.add(student)
    session.commit()


if __name__ == '__main__':
    create_students()

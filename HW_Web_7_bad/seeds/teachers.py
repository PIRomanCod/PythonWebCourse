import random
from faker import Faker
from database.db import session
from database.models_sample import Teacher

fake = Faker("uk_Ua")


def create_teachers():
    for _ in range(1, 6):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            phone=fake.phone_number(),
            address=fake.address(),
            start_work=fake.date_between(start_date='-10y')
        )
        session.add(teacher)
    session.commit()


if __name__ == '__main__':
    create_teachers()
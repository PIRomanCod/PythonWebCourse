"""
Заповніть отриману базу даних випадковими даними
(~30-50 студентів,
3 групи,
5-8 предметів,
3-5 викладачів,
до 20 оцінок у кожного студента з усіх предметів)
"""

import faker
from random import randint, choice
from psycopg2 import DatabaseError
from postgress_connector import postgres_connection
from datetime import datetime, date, timedelta


NUMBER_GROUPS = 3
NUMBER_STUDENTS = 40
NUMBER_LESSONS = 8
NUMBER_TEACHERS = 5
NUMBER_SCORES = 20


def generate_fake_data(number_groups: int, number_students: int, number_lessons: int, number_teachers: int) -> tuple:
    fake_groups = []  # тут зберігатимемо групи
    fake_students = []  # тут зберігатимемо студентів
    fake_lessons = []  # тут зберігатимемо назви предметів
    fake_teachers = []  # тут зберігатимемо викладачів

    fake_data = faker.Faker(["uk_UA"])  # локалізація

    # Створимо набір груп
    for _ in range(number_groups):
        fake_groups.append(fake_data.license_plate())

    # Згенеруємо тепер студентів
    for _ in range(number_students):
        fake_students.append(fake_data.name())

    # Набір предметів, але не зовсім коректні виходять, не знайшов більш підходящої функції
    for _ in range(number_lessons):
        fake_lessons.append(fake_data.job())

    # Набір викладачів
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    return fake_groups, fake_students, fake_lessons, fake_teachers


def prepare_data(groups: list, students: list, lessons: list, teachers: list) -> tuple:
    for_groups = []
    # підготовляємо список кортежів назв груп
    for group in groups:
        for_groups.append((group, ))

    for_teachers = []
    # підготовляємо список кортежів викладачів
    for teacher in teachers:
        for_teachers.append((teacher,))

    for_students = []  # для таблиці студентів

    for student in students:

        for_students.append((student, randint(1, len(groups))))

    for_lessons = []  # для таблиці предметів

    for lesson in lessons:

        for_lessons.append((lesson, randint(1, len(teachers))))

    for_scores = []
    start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    end_date = datetime.strptime("2023-06-15", "%Y-%m-%d")

    def get_list_date(start: date, end: date) -> list[date]:
        result = []
        current_date = start
        while current_date <= end:
            if current_date.isoweekday() < 6:
                result.append(current_date)
            current_date += timedelta(1)
        return result

    list_dates = get_list_date(start_date, end_date)

    for day in list_dates:
        random_lesson = randint(1, len(lessons))
        random_students = [randint(1, NUMBER_STUDENTS) for _ in range(5)]
        for student in random_students:
            for_scores.append((random_lesson, student, randint(1, 12), day.date()))

    return for_groups, for_students, for_teachers, for_lessons, for_scores


def insert_data_to_db(conn, groups: tuple, students: tuple, teachers: tuple, lessons: tuple, scores: tuple) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними

    try:
        cur = conn.cursor()
        # Наповнюємо таблицю груп
        sql_to_groups = "INSERT INTO groups (group_name) VALUES (%s)"
        # print(*groups)
        for item in groups:
            cur.execute(sql_to_groups, item)

        # Наповнюємо таблицю студентів
        sql_to_students = "INSERT INTO students (student_name, group_id) VALUES (%s, %s)"
        for item in students:
            cur.execute(sql_to_students, item)

        # Наповнюємо таблицю викладачів
        sql_to_teachers = """INSERT INTO teachers(teacher_name) VALUES (%s)"""
        for item in teachers:
            cur.execute(sql_to_teachers, item)

        # Наповнюємо таблицю предметів
        sql_to_lessons = """INSERT INTO lessons(lessons_name, teacher_id) VALUES (%s, %s)"""
        for item in lessons:
            cur.execute(sql_to_lessons, item)

        # Наповнюємо таблицю успішності
        sql_to_scores = """INSERT INTO scores(lesson_id, student_id, score, created_at) VALUES (%s, %s, %s, %s)"""
        for item in scores:
            cur.execute(sql_to_scores, item)

        # Фіксуємо наші зміни в БД
        cur.close()
        conn.commit()

    except DatabaseError as error:
        print(error)


if __name__ == "__main__":
    groups, students, teachers, lessons, scores = \
        prepare_data(*generate_fake_data(NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_LESSONS, NUMBER_TEACHERS))
    with postgres_connection() as conn:
        if conn is not None:
            insert_data_to_db(conn, groups, students, teachers, lessons, scores)

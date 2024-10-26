"""
Заповніть отриману базу даних випадковими даними
(~30-50 студентів,
3 групи,
5-8 предметів,
3-5 викладачів,
до 20 оцінок у кожного студента з усіх предметів)
"""


from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 40
NUMBER_LESSONS = 8
NUMBER_TEACHERS = 5
NUMBER_SCORES = 20


def generate_fake_data(number_groups, number_students, number_lessons, number_teachers) -> tuple():
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


def prepare_data(groups, students, lessons, teachers) -> tuple():
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

        for_students.append((student, choice(groups)))

    for_lessons = []  # для таблиці предметів

    for lesson in lessons:

        for_lessons.append((lesson, choice(teachers)))

    for_scores = []

    for lesson in lessons:
        # Виконуємо цикл по кожному предмету
        for student in students:
            score_date = datetime(2023, 1, randint(1, 31)).date()
            # Виконуємо цикл за кількістю студентів
            for_scores.append((lesson, student, randint(3, 5), score_date))

    return for_groups, for_students, for_teachers, for_lessons, for_scores


def insert_data_to_db(groups, students, teachers, lessons, scores) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними

    with sqlite3.connect('university.db') as con:

        cur = con.cursor()
        # Наповнюємо таблицю груп
        sql_to_groups = """INSERT INTO groups(group_name)
                               VALUES (?)"""

        cur.executemany(sql_to_groups, groups)
        # Наповнюємо таблицю студентів
        sql_to_students = """INSERT INTO students (student, group_name)
                                       VALUES (?, ?)"""

        cur.executemany(sql_to_students, students)
        # Наповнюємо таблицю викладачів
        sql_to_teachers = """INSERT INTO teachers(teacher)
                                            VALUES (?)"""

        cur.executemany(sql_to_teachers, teachers)
        # Наповнюємо таблицю успішності
        sql_to_scores = """INSERT INTO scores(lesson, student, score, created_at)
                                      VALUES (?, ?, ?, ?)"""

        cur.executemany(sql_to_scores, scores)
        # Наповнюємо таблицю предметів
        sql_to_lessons = """INSERT INTO lessons(lessons_name, teacher_id)
                               VALUES (?, ?)"""

        cur.executemany(sql_to_lessons, lessons)

        # Фіксуємо наші зміни в БД

        con.commit()


if __name__ == "__main__":
    groups, students, teachers, lessons, scores = prepare_data(*generate_fake_data(NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_LESSONS, NUMBER_TEACHERS))
    insert_data_to_db(groups, students, teachers, lessons, scores)
  
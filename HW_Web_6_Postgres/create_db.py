"""
Реалізуйте базу даних, схема якої містить:

Таблиця студентів;
Таблицю груп;
Таблицю викладачів;
Таблицю предметів із вказівкою викладача, який читає предмет;
Таблицю, де у кожного студента є оцінки з предметів із зазначенням коли оцінку отримано;
"""
from psycopg2 import DatabaseError
from postgress_connector import postgres_connection


def create_db(conn):
    # читаємо файл зі скриптом для створення БД
    with open('create_tables.sql', 'r') as f:
        sql = f.read()

    # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    try:
        cur = conn.cursor()
        # виконуємо скрипт із файлу, який створить таблиці в БД
        cur.execute(sql)
        cur.close()
    except DatabaseError as error:
        print(error)


if __name__ == '__main__':
    with postgres_connection() as conn:
        if conn is not None:
            create_db(conn)
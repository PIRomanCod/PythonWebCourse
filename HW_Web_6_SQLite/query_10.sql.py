"""
Список курсів, які певному студенту читає певний викладач.
для пошуку треба ввести у рядок #24 номери:
s.id від 1 до 40 --> NUMBER_STUDENTS = 40
t.id від 1 до 5 --> NUMBER_TEACHERS = 5
"""

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT sc.student, l.lessons_name, t.teacher
FROM scores sc
LEFT JOIN lessons l ON l.lessons_name = sc.lesson
LEFT JOIN students s  ON s.student = sc.student
LEFT JOIN teachers t ON t.teacher = l.teacher_id 
WHERE  s.id = 30 and t.id = 2;
"""

res = execute_query(sql)
for n, item in enumerate(res, start=1):
    print(n, item)


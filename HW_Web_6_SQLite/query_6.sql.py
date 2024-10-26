"""
Знайти список студентів у певній групі.
для пошуку групи треба ввести у рядок #20 номер від 1 до 3 --> NUMBER_GROUPS = 3
"""

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s.student, s.group_name
FROM students AS s
LEFT JOIN groups AS g ON s.group_name = g.group_name
WHERE g.id = 2;
"""

res = execute_query(sql)
for n, item in enumerate(res, start=1):
    print(n, item)

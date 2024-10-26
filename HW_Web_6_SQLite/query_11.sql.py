"""
Середній бал, який певний викладач ставить певному студентові.
для пошуку  треба ввести у рядок #24 номер:
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

"""

res = execute_query(sql)
for item in res:
    print(item)

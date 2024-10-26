"""
Знайти студента із найвищим середнім балом з певного предмета
"""

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT lesson, student, MAX(score) as grade
FROM scores 
GROUP BY lesson
ORDER BY grade DESC
"""

res = execute_query(sql)
for n, item in enumerate(res, start=1):
    print(n, item)

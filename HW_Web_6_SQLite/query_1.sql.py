"""
Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
"""

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT student, ROUND(AVG(score), 2) as grade
FROM scores 
GROUP BY student
ORDER BY grade DESC
LIMIT 5
"""

res = execute_query(sql)
for n, item in enumerate(res, start=1):
    print(n, item)

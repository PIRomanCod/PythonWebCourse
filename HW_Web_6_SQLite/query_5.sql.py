"""
Знайти які курси читає певний викладач.
"""

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT teacher_id, lessons_name
FROM lessons 
ORDER BY teacher_id
"""

res = execute_query(sql)
for n, item in enumerate(res, start=1):
    print(n, item)

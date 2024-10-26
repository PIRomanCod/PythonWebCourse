"""
Знайти середній бал, який ставить певний викладач зі своїх предметів.
"""

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT t.teacher, sc.lesson,  ROUND(AVG(sc.score), 2) as average_grade
FROM scores sc
LEFT JOIN lessons AS l ON l.lessons_name = sc.lesson 
LEFT JOIN teachers AS t ON t.teacher = l.teacher_id
GROUP BY l.lessons_name
ORDER BY t.id;
"""

res = execute_query(sql)
for n, item in enumerate(res, start=1):
    print(n, item)
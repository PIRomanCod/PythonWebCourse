"""
Знайти список курсів, які відвідує студент
"""

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT sc.lesson 
FROM scores sc
LEFT JOIN lessons l ON l.lessons_name = sc.lesson 
GROUP BY l.id;
"""

res = execute_query(sql)
for n, item in enumerate(res, start=1):
    print(n, item)

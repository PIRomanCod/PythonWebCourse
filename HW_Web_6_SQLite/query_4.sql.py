"""
Знайти середній бал на потоці (по всій таблиці оцінок).
"""

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT ROUND(AVG(score), 2)
FROM scores 
"""

res = execute_query(sql)
for item in res:
    print(item)

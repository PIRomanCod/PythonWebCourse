"""
Оцінки студентів у певній групі з певного предмета на останньому занятті.
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

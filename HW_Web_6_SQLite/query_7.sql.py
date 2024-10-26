"""
Знайти оцінки студентів у окремій групі з певного предмета.
для пошуку групи треба ввести у рядок #24 номер:
g.id від 1 до 3 --> NUMBER_GROUPS = 3
l.id від 1 до 8 --> NUMBER_LESSONS = 8
"""

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT st.group_name, sc.lesson, st.student, score
FROM scores sc
LEFT JOIN students st ON sc.student  = st.student 
LEFT JOIN groups AS g ON st.group_name = g.group_name
LEFT JOIN lessons AS l ON l.lessons_name = sc.lesson 
WHERE g.id = 2 and l.id = 4;
"""

res = execute_query(sql)
for n, item in enumerate(res, start=1):
    print(n, item)
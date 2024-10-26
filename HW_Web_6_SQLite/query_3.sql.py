"""
Знайти середній бал у групах з певного предмета
"""

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT st.group_name, sc.lesson, ROUND(AVG(sc.score), 2) as average_grade
FROM scores sc
LEFT JOIN students st ON sc.student  = st.student  
GROUP BY sc.lesson, st.group_name
ORDER BY st.group_name;
"""

res = execute_query(sql)
for n, item in enumerate(res, start=1):
    print(n, item)

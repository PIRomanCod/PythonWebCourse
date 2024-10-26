--3. Знайти середній бал у групах з певного предмета
SELECT l.lessons_name, g.group_name, ROUND(AVG(sc.score), 2) as grade
from scores sc
left join students st on st.id = sc.student_id
left join "groups" g on g.id = st.group_id
left join lessons l on l.id = sc.lesson_id
where lesson_id = 1
GROUP BY g.group_name, l.lessons_name
ORDER BY grade desc;
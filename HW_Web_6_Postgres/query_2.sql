--2. Знайти студента із найвищим середнім балом з певного предмета
SELECT st.student_name, ROUND(AVG(sc.score), 2) as grade
from scores sc
left join students st on st.id = sc.student_id
where lesson_id = 5
GROUP BY st.student_name
ORDER BY grade DESC
LIMIT 1;
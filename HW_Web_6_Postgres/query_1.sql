--1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів
SELECT st.student_name, ROUND(AVG(sc.score), 2) as grade
FROM scores sc
left join students st on st.id = sc.student_id
GROUP BY st.student_name
ORDER BY grade DESC
LIMIT 5;
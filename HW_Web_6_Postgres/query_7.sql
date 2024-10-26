--7. Знайти оцінки студентів у окремій групі з певного предмета
SELECT g.group_name, l.lessons_name , st.student_name , score
FROM scores sc
LEFT JOIN students st ON sc.student_id  = st.id
LEFT JOIN "groups" AS g ON st.group_id = g.id
LEFT JOIN lessons AS l ON l.id = sc.lesson_id
WHERE g.id = 1 and l.id = 3
ORDER by score desc;
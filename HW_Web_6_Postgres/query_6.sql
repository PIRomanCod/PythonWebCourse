--6. Знайти список студентів у певній групі
SELECT s.student_name , g.group_name
FROM students AS s
LEFT JOIN "groups" AS g ON s.group_id  = g.id
WHERE g.id = 1;
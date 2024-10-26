--8. Знайти середній бал, який ставить певний викладач зі своїх предметів
SELECT l.lessons_name, ROUND(AVG(score), 2)
FROM scores sc
LEFT JOIN lessons AS l ON l.id = sc.lesson_id
LEFT JOIN teachers AS t ON t.id = l.teacher_id
WHERE l.teacher_id  = 5
GROUP by l.id;
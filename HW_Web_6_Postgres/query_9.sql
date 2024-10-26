--9. Знайти список курсів, які відвідує студент
SELECT l.lessons_name, s.student_name
FROM scores sc
LEFT JOIN lessons l ON l.id = sc.lesson_id
LEFT JOIN students s  ON s.id = sc.student_id
WHERE sc.student_id  = 13
GROUP BY l.lessons_name, s.student_name;
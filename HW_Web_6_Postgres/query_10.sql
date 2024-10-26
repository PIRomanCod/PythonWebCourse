--10. Список курсів, які певному студенту читає певний викладач
SELECT s.student_name , l.lessons_name, t.teacher_name
FROM scores sc
LEFT JOIN lessons l ON l.id = sc.lesson_id
LEFT JOIN students s  ON s.id  = sc.student_id
LEFT JOIN teachers t ON t.id = l.teacher_id
WHERE  s.id = 18 and t.id = 2
GROUP BY l.lessons_name, s.student_name, t.teacher_name;
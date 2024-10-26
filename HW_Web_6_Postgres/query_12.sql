--12. Оцінки студентів у певній групі з певного предмета на останньому занятті
SELECT  g.group_name, t.teacher_name, l.lessons_name, s.student_name, sc.score
FROM scores sc
LEFT JOIN lessons l ON l.id = sc.lesson_id
LEFT JOIN students s  ON s.id  = sc.student_id
LEFT JOIN teachers t ON t.id = l.teacher_id
LEFT join "groups" g on g.id = s.group_id
WHERE  t.id = 2 and g.id = 2 and sc.created_at IN (select created_at last_date
													from scores
													ORDER BY created_at DESC
													LIMIT 1)
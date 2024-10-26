--5. Знайти які курси читає певний викладач
SELECT t.teacher_name, l.lessons_name
FROM lessons l
left join teachers t on t.id = l.teacher_id
ORDER BY teacher_id
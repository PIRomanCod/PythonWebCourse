--11. Середній бал, який певний викладач ставить певному студентові
select t.teacher_name, st.student_name,  ROUND(AVG(score), 2)
--select l.lessons_name, t.teacher_name, st.student_name,  ROUND(AVG(score), 2) -- inverse select+group for lesson slice
from scores sc
LEFT JOIN lessons l ON l.id = sc.lesson_id
LEFT JOIN students st  ON st.id  = sc.student_id
LEFT JOIN teachers t ON t.id = l.teacher_id
WHERE  st.id = 11 and t.id = 2
GROUP by st.student_name, t.teacher_name
--GROUP by st.student_name, l.lessons_name, t.teacher_name
;
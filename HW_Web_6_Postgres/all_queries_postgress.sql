--1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів
SELECT st.student_name, ROUND(AVG(sc.score), 2) as grade
FROM scores sc
left join students st on st.id = sc.student_id 
GROUP BY st.student_name
ORDER BY grade DESC
LIMIT 5;

--2. Знайти студента із найвищим середнім балом з певного предмета
SELECT st.student_name, ROUND(AVG(sc.score), 2) as grade
from scores sc 
left join students st on st.id = sc.student_id 
where lesson_id = 5
GROUP BY st.student_name
ORDER BY grade DESC
LIMIT 1;

--3. Знайти середній бал у групах з певного предмета
SELECT l.lessons_name, g.group_name, ROUND(AVG(sc.score), 2) as grade
from scores sc 
left join students st on st.id = sc.student_id
left join "groups" g on g.id = st.group_id 
left join lessons l on l.id = sc.lesson_id 
where lesson_id = 1
GROUP BY g.group_name, l.lessons_name
ORDER BY grade desc;

--4. Знайти середній бал на потоці (по всій таблиці оцінок)
SELECT ROUND(AVG(score), 2)
FROM scores;

--5. Знайти які курси читає певний викладач
SELECT t.teacher_name, l.lessons_name
FROM lessons l
left join teachers t on t.id = l.teacher_id 
ORDER BY teacher_id

--6. Знайти список студентів у певній групі
SELECT s.student_name , g.group_name 
FROM students AS s
LEFT JOIN "groups" AS g ON s.group_id  = g.id
WHERE g.id = 1;


--7. Знайти оцінки студентів у окремій групі з певного предмета
SELECT g.group_name, l.lessons_name , st.student_name , score
FROM scores sc
LEFT JOIN students st ON sc.student_id  = st.id 
LEFT JOIN "groups" AS g ON st.group_id = g.id 
LEFT JOIN lessons AS l ON l.id = sc.lesson_id  
WHERE g.id = 1 and l.id = 3
ORDER by score desc;

--8. Знайти середній бал, який ставить певний викладач зі своїх предметів
SELECT l.lessons_name, ROUND(AVG(score), 2)
FROM scores sc
LEFT JOIN lessons AS l ON l.id = sc.lesson_id  
LEFT JOIN teachers AS t ON t.id = l.teacher_id 
WHERE l.teacher_id  = 5
GROUP by l.id;


--9. Знайти список курсів, які відвідує студент
SELECT l.lessons_name, s.student_name  
FROM scores sc
LEFT JOIN lessons l ON l.id = sc.lesson_id 
LEFT JOIN students s  ON s.id = sc.student_id 
WHERE sc.student_id  = 13
GROUP BY l.lessons_name, s.student_name;


--10. Список курсів, які певному студенту читає певний викладач
SELECT s.student_name , l.lessons_name, t.teacher_name 
FROM scores sc
LEFT JOIN lessons l ON l.id = sc.lesson_id 
LEFT JOIN students s  ON s.id  = sc.student_id 
LEFT JOIN teachers t ON t.id = l.teacher_id 
WHERE  s.id = 18 and t.id = 2
GROUP BY l.lessons_name, s.student_name, t.teacher_name;


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


-- Тут лише порівняння результатів запросів з файлу my_select та прямим SQL запросом

--1 SQL Знайти 5 студентів із найбільшим середнім балом з усіх предметів
SELECT students.name AS students_name, round(avg(scores.value), 2) AS avg_score 
FROM scores 
JOIN students ON students.id = scores.student_id 
GROUP BY students.id 
ORDER BY avg_score DESC 
LIMIT 5

--1 ORM interpreted Знайти 5 студентів із найбільшим середнім балом з усіх предметів
SELECT st.student_name, ROUND(AVG(sc.score), 2) as grade
FROM scores sc
left join students st on st.id = sc.student_id 
GROUP BY st.student_name
ORDER BY grade DESC
LIMIT 5;

--2. SQL Знайти студента із найвищим середнім балом з певного предмета
SELECT st.name, ROUND(AVG(sc.value), 2) as grade
from scores sc 
left join students st on st.id = sc.student_id 
where lesson_id = 1
GROUP BY st.name
ORDER BY grade DESC
LIMIT 1;

--2. ORM interpreted Знайти студента із найвищим середнім балом з певного предмета
SELECT students.name AS students_name, lessons.name AS lessons_name, round(avg(scores.value), 2) AS max_score 
FROM scores 
JOIN students ON students.id = scores.student_id 
JOIN lessons ON lessons.id = scores.lesson_id 
WHERE lessons.id = 1 
GROUP BY lessons.id, students.id 
ORDER BY max_score DESC 
LIMIT 1
 
--3. SQL Знайти середній бал у групах з певного предмета
SELECT l.name, g.name, ROUND(AVG(sc.value), 2) as grade
from scores sc 
left join students st on st.id = sc.student_id
left join "groups" g on g.id = st.group_id 
left join lessons l on l.id = sc.lesson_id 
where lesson_id = 1
GROUP BY g.name, l.name
ORDER BY grade desc;

--3. ORM interpreted Знайти середній бал у групах з певного предмета
SELECT lessons.name AS lessons_name, groups.name AS groups_name, round(avg(scores.value), 2) AS max_score 
FROM scores 
LEFT OUTER JOIN students ON students.id = scores.student_id 
LEFT OUTER JOIN lessons ON lessons.id = scores.lesson_id 
LEFT OUTER JOIN groups ON groups.id = students.group_id 
WHERE scores.lesson_id = 1 
GROUP BY groups.id, lessons.id 
ORDER BY max_score DESC

--4. SQL Знайти середній бал на потоці (по всій таблиці оцінок)
SELECT ROUND(AVG(value), 2)
FROM scores;

--4. ORM interpreted Знайти середній бал на потоці (по всій таблиці оцінок)
SELECT round(avg(scores.value), 2) AS round_1 
FROM scores

--5. SQL Знайти які курси читає певний викладач
SELECT t.name, l.name
FROM lessons l
left join teachers t on t.id = l.teacher_id
where t.id = 3
ORDER BY teacher_id

--5. ORM interpreted Знайти які курси читає певний викладач
SELECT teachers.name AS teachers_name, lessons.name AS lessons_name 
FROM lessons 
JOIN teachers ON teachers.id = lessons.teacher_id 
WHERE teachers.id = 3

--6. SQL Знайти список студентів у певній групі
SELECT s.name , g.name
FROM students AS s
LEFT JOIN "groups" AS g ON s.group_id  = g.id
WHERE g.id = 2;

--6. ORM interpreted Знайти список студентів у певній групі
SELECT groups.name AS groups_name, students.name AS students_name 
FROM "groups" 
JOIN students ON groups.id = students.group_id 
WHERE groups.id = 2

--7. SQL Знайти оцінки студентів у окремій групі з певного предмета
SELECT g.name as group_name, l.name as lesson, st.name as student, value 
FROM scores sc
LEFT JOIN students st ON sc.student_id  = st.id
LEFT JOIN "groups" AS g ON st.group_id = g.id
LEFT JOIN lessons AS l ON l.id = sc.lesson_id
WHERE g.id = 1 and l.id = 1
ORDER by value desc;

--7. ORM interpreted Знайти оцінки студентів у окремій групі з певного предмета
SELECT groups.name AS groups_name, lessons.name AS lessons_name, students.name AS students_name, scores.value AS scores_value 
FROM scores 
LEFT OUTER JOIN students ON students.id = scores.student_id 
LEFT OUTER JOIN lessons ON lessons.id = scores.lesson_id 
LEFT OUTER JOIN groups ON groups.id = students.group_id 
WHERE scores.lesson_id = 1 AND groups.id = 1 
ORDER BY scores.value desc

--8. SQL Знайти середній бал, який ставить певний викладач зі своїх предметів
SELECT l.name, ROUND(AVG(value), 2)
FROM scores sc
LEFT JOIN lessons AS l ON l.id = sc.lesson_id
LEFT JOIN teachers AS t ON t.id = l.teacher_id
WHERE l.teacher_id  = 3
GROUP by l.id;

--8. ORM interpreted Знайти середній бал, який ставить певний викладач зі своїх предметів
SELECT teachers.name AS teachers_name, lessons.name AS lessons_name, round(avg(scores.value), 2) AS round_1 
FROM scores 
LEFT OUTER JOIN lessons ON lessons.id = scores.lesson_id 
LEFT OUTER JOIN teachers ON teachers.id = lessons.teacher_id 
WHERE teachers.id = 3 
GROUP BY lessons.id, teachers.id

--9. SQL Знайти список курсів, які відвідує студент
SELECT l.name, s.name
FROM scores sc
LEFT JOIN lessons l ON l.id = sc.lesson_id
LEFT JOIN students s  ON s.id = sc.student_id
WHERE sc.student_id  = 13
GROUP BY l.name, s.name;

--9. ORM interpreted Знайти список курсів, які відвідує студент
SELECT students.name AS students_name, lessons.name AS lessons_name 
FROM scores 
LEFT OUTER JOIN lessons ON lessons.id = scores.lesson_id 
LEFT OUTER JOIN students ON students.id = scores.student_id 
WHERE students.id = 13 
GROUP BY lessons.id, students.name

--10. SQL Список курсів, які певному студенту читає певний викладач
SELECT s.name , l.name, t.name
FROM scores sc
LEFT JOIN lessons l ON l.id = sc.lesson_id
LEFT JOIN students s  ON s.id  = sc.student_id
LEFT JOIN teachers t ON t.id = l.teacher_id
WHERE  s.id = 18 and t.id = 3
GROUP BY l.name, s.name, t.name;

--10. ORM interpreted Список курсів, які певному студенту читає певний викладач
SELECT students.name AS students_name, lessons.name AS lessons_name, teachers.name AS teachers_name 
FROM scores 
JOIN lessons ON lessons.id = scores.lesson_id 
JOIN students ON students.id = scores.student_id 
JOIN teachers ON teachers.id = lessons.teacher_id 
WHERE teachers.id = 3 AND students.id = 18 
GROUP BY lessons.id, students.id, teachers.id

--11. SQL Середній бал, який певний викладач ставить певному студентові
select t.name, st.name,  ROUND(AVG(value), 2)
from scores sc
LEFT JOIN lessons l ON l.id = sc.lesson_id
LEFT JOIN students st  ON st.id  = sc.student_id
LEFT JOIN teachers t ON t.id = l.teacher_id
WHERE  st.id = 11 and t.id = 2
GROUP by st.name, t.name

--11. ORM interpreted Середній бал, який певний викладач ставить певному студентові
SELECT teachers.name AS teachers_name, students.name AS students_name, round(avg(scores.value), 2) AS round_1 
FROM scores 
LEFT OUTER JOIN students ON students.id = scores.student_id 
LEFT OUTER JOIN lessons ON lessons.id = scores.lesson_id 
LEFT OUTER JOIN teachers ON teachers.id = lessons.teacher_id 
WHERE teachers.id = 2 AND students.id = 11
GROUP BY students.id, teachers.id

--12.SQL Оцінки студентів у певній групі з певного предмета на останньому занятті
SELECT  g.name, t.name, l.name, s.name, sc.value
FROM scores sc
LEFT JOIN lessons l ON l.id = sc.lesson_id
LEFT JOIN students s  ON s.id  = sc.student_id
LEFT JOIN teachers t ON t.id = l.teacher_id
LEFT join "groups" g on g.id = s.group_id
WHERE  t.id = 3 and g.id = 3 and sc.date IN (select date last_date
 												    from scores
 													ORDER BY date DESC
 													LIMIT 1)
													
--12. ORM interpreted Оцінки студентів у певній групі з певного предмета на останньому занятті
SELECT groups.name AS groups_name, teachers.name AS teachers_name, 
lessons.name AS lessons_name, students.name AS students_name, scores.value AS scores_value 
FROM scores 
LEFT OUTER JOIN students ON students.id = scores.student_id 
LEFT OUTER JOIN lessons ON lessons.id = scores.lesson_id 
LEFT OUTER JOIN teachers ON teachers.id = lessons.teacher_id 
LEFT OUTER JOIN groups ON groups.id = students.group_id 
WHERE teachers.id =3 AND groups.id = 3 AND scores.date = (
														SELECT max(scores.date) AS max_1 
														FROM scores)

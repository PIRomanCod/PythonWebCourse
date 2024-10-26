-- Table: groups
DROP TABLE IF EXISTS groups CASCADE;
CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    group_name VARCHAR(255)
);


-- Table: students
DROP TABLE IF EXISTS students CASCADE;
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    student_name VARCHAR(255),
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);


-- Table: teachers
DROP TABLE IF EXISTS teachers CASCADE;
CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    teacher_name VARCHAR(255)
);

-- Table: lessons
DROP TABLE IF EXISTS lessons CASCADE;
CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    lessons_name VARCHAR(255),
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

-- Table: scores
DROP TABLE IF EXISTS scores CASCADE;
CREATE TABLE scores (
    id SERIAL PRIMARY KEY,
    lesson_id INTEGER,
    student_id INTEGER,
    score INTEGER,
    created_at DATE,
    FOREIGN KEY (student_id) REFERENCES students (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
    FOREIGN KEY (lesson_id) REFERENCES lessons (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);





use internship;

CREATE TABLE students (
  id INTEGER,
  name TEXT,
  marks INTEGER
 );

INSERT INTO students VALUES (1, 'Amit', 85);
INSERT INTO students VALUES (2, 'Riya', 92);
INSERT INTO students VALUES (3, 'John', 78);
 
SELECT * FROM students;
SELECT name, marks FROM students;

INSERT INTO students (id, name, marks) 
VALUES (6, 'Meera', 81);

INSERT INTO students VALUES (4, 'Sneha', 88);
INSERT INTO students VALUES (5, 'Arjun', 95);

SET SQL_SAFE_UPDATES = 0;

UPDATE students
SET marks = 90
WHERE name = 'Amit';

UPDATE students
SET marks = marks + 5
WHERE marks < 80;

DELETE FROM students
WHERE name = 'John';

ALTER TABLE students
ADD COLUMN grade TEXT;

ALTER TABLE students
RENAME COLUMN name TO student_name;

ALTER TABLE students
MODIFY marks FLOAT;

CREATE TABLE scores (
    subject TEXT,
    marks INTEGER
);
INSERT INTO scores VALUES ('Math', 80);
INSERT INTO scores VALUES ('Math', 90);
INSERT INTO scores VALUES ('Science', 85);
SELECT subject, AVG(marks) FROM scores GROUP BY subject;
SELECT subject, COUNT(*) FROM scores GROUP BY subject;

SELECT subject, AVG(marks) 
FROM scores 
GROUP BY subject;

SELECT subject, COUNT(*) 
FROM scores 
GROUP BY subject;

SELECT subject, GROUP_CONCAT(marks)
FROM scores
GROUP BY subject;

  
-- CREATE TABLE students(
--  student_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  birth_date DATE NOT NULL
-- )
--INSERT INTO students (first_name, last_name, birth_date)VALUES
-- ('Cohen','Yohan','2010-12-03'),
--  ('Benichou','Marc','1998-11-02'),
-- ('Lea','Benichou','1987-07-27'),('Amelia','Dux','1996-04-07'),
-- ('David','Grez','2003-06-14'),('Omer','Simpson','1980-10-03')
--('Lai','Oceanne','2001-06-06');

--SELECT * FROM students
-- SELECT first_name, Last_name FROM students
-- SELECT first_name, Last_name FROM students where student_id = 2
-- SELECT first_name, Last_name FROM students where first_name ilike '%Marc' and last_name ilike '%Benichou'
-- SELECT first_name, Last_name FROM students where first_name ilike '%Marc%' or last_name ilike '%Benichou%'
-- SELECT first_name FROM students where first_name ilike '%a%'
-- SELECT first_name FROM students where first_name ilike 'a%'
-- SELECT first_name FROM students where first_name ilike '%a'
-- SELECT first_name FROM students where first_name ilike '%a%' offset 2
-- SELECT * FROM students where student_id = 1 or student_id = 3
-- SELECT * FROM students where birth_date >= '1/01/2000'
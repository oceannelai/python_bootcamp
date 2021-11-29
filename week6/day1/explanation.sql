-- create table actors1(
-- id serial primary key,
-- first_name varchar (50),
-- last_name varchar (50),
-- number_of_oscars int)
-- insert into actors1(first_name,last_name,number_of_oscars) values
--  ('George','clooney',3),('Brad','Pritt',5);
-- insert into actors1(first_name,last_name,number_of_oscars) values
-- ('Anna','Hathaway',1);
-- insert into actors1(first_name,last_name,number_of_oscars) values
--  ('Helena','Carter',1);
--  insert into actors1(first_name,last_name,number_of_oscars) values
--  ('Brad','Pitt',2),('Leonardo','DiCaprio',1),('Tom','Hanks',2);
-- SELECT * FROM actors1;

-- insert into actors1(first_name,last_name,number_of_oscars)
-- values('Sasha','Cohen',NULL)

-- SELECT* FROM actors1 where number_of_oscars IS NULL


-- SELECT * FROM actors1 LIMIT 4 
-- SELECT *  FROM actors1 order by last_name DESC limit 4
--  SELECT * FROM actors1 where first_name ilike '%E%' 
--   SELECT * FROM actors1 WHERE number_of_oscars >= 5
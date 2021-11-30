--SELECT avg(number_of_oscars) AS average_number_oscars FROM actors1;
--SELECT DISTINCT number_of_oscars FROM actors1 ;
--SELECT * from actors1 where age > date(" ")
--SELECT * FROM actors1 WHERE first_name in ('David','Morgan','Will');

-- insert into actors1(first_name,last_name,number_of_oscars) values
-- ('matt','Damon',5)

--UPDATE actors1 SET first_name = 'Maty' WHERE first_name = 'Matt'


-- UPDATE actors1
-- set number_of_oscars = 4 where first_name = 'George'
-- returning actors1

 --ALTER TABLE actors1 RENAME COLUMN age TO birthdate
-- DELETE FROM actors1 WHERE first_name = 'Helena'


-- create table movies(
-- movie_id serial,
-- movies_title varchar(50),
-- movies_story TEXT,
-- actor_playing_id INTEGER,
-- PRIMARY KEY (movie_id),
-- FOREIGN KEY (actor_playing_id) REFERENCES actors1 (id)
-- );

-- INSERT INTO movies (movies_title, movies_story, actor_playing_id) VALUES
--     ( 'Good Will Hunting.', 
--     'Written by Affleck and Damon, the film follows 20-year-old South Boston janitor Will Hunting',
--     (SELECT id from actors1 WHERE first_name='Maty' AND last_name='Damon')),
--     ( 'Oceans Eleven.', 
--     'American heist film directed by Steven Soderbergh and written by Ted Griffin.', 
--     (SELECT id from actors1 WHERE first_name='Maty' AND last_name='Damon'));

-- create table producers(
-- producer_id serial,
-- first_name varchar(50),
-- last_name varchar(50),
-- movie_directed varchar(50),
-- producer_movie_id INTEGER,
-- PRIMARY KEY (producer_id),
-- FOREIGN KEY (produce_movie_id) REFERENCES actors1 (id)
-- )

-- INSERT into producers(first_name,last_name,movie_directed,producer_movie_id) VALUES
-- ('Matt','Damon','Oceans Eleven',(SELECT movie_id from movies WHERE movies_title= 'Oceans Eleven.')),
-- ('Matt','Damon','Good Will Hunting',(SELECT movie_id from movies WHERE movies_title= 'Good Will Hunting.'));
--SELECT * FROM movies
-- SELECT movies.movies_title,movies.movies_story,producers.movie_directed
-- FROM movies
-- inner join producers
-- on movies.movie_id = producers.producer_id






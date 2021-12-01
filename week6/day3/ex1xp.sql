--SELECT * FROM language
-- SELECT
--     film.title, film.description, language.name
-- FROM film
-- inner join language
-- on film.language_id = language.language_id;

--  create table new_film (
--  new_films_id serial primary key,
--  new_film_name varchar(50))
-- insert into new_film(new_film_name) values
-- ('Moana'),('Haikyuu'),('Lion King'),('Red Notice')

-- create table customer_review (
-- 	review_id serial not null,
-- 	film_id integer not null,
-- 	language_id integer,
-- 	title varchar (100),
-- 	score integer not null,
-- 	check (score < 11 and score >= 0),
-- 	review_text text,
-- 	last_update timestamp default current_timestamp,
-- 	primary key (review_id),
-- 	foreign key (film_id) references new_film (new_films_id) on delete cascade,
-- 	foreign key (language_id) references language (language_id)
-- );

-- insert into customer_review(film_id, language_id,title,score,review_text)values
-- (1, 1, 'Moana', 10, 'great movie with amazing songs and animation'),
-- (2, 3, 'Haikyuu', 10, 'amazing movie, with great life lessons to learn from it'),
-- (3, 1, 'Lion King', 10, 'great songs + amazing animation'),
-- (4, 1, 'Red Notice',9,'well-directed with great sense of humour');

--Delete from new_film where new_film_name = 'Red Notice'

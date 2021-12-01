-- CREATE TABLE countries	(
-- countries_id serial primary key,
-- country_id INTEGER,
-- country_name varchar
-- )

-- insert into countries(country_id,country_name) values
-- (1,'USA'),(2,'UK'),(3,'Italy')

-- SELECT actors1.first_name, actors1.last_name, countries.country_id,countries.country_name
-- FROM actors1
-- INNER JOIN countries
-- ON actors1.id=countries.countries_id

--  SELECT actors1.first_name, actors1.last_name, countries.country_id,countries.country_name
-- FROM actors1
-- LEFT OUTER JOIN countries
-- ON actors1.id=countries.countries_id

--  SELECT actors1.first_name, actors1.last_name, countries.country_id,countries.country_name
-- FROM actors1
-- RIGHT OUTER JOIN countries
-- ON actors1.id=countries.countries_id

--  SELECT actors1.first_name, actors1.last_name, countries.country_id,countries.country_name
-- FROM actors1
-- FULL JOIN countries
-- ON actors1.id=countries.countries_id
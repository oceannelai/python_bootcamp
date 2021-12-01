-- UPDATE film
-- SET language_id = 5
-- WHERE film_id = 25 or film_id = 100
-- returning film

-- select count(rental_id) from rental where return_date is null

-- select rental.rental_id,film.title, film.rental_rate
-- FROM rental
-- inner join inventory
-- ON inventory.inventory_id = rental.inventory_id
-- inner join film
-- ON film.film_id = inventory.film_id
-- WHERE rental.return_date is NULL 
-- order by film.rental_rate DESC limit 30

-- select title
-- from film
-- inner join film_actor
-- on film.film_id = film_actor.film_id
-- inner join actor
-- on actor.actor_id = film_actor.actor_id
-- where description ilike '%sumo%' and first_name='Penelope' and last_name='Monroe';

--SELECT title ,length ,rating from film WHERE description ilike '%documentary%' and length<60 and rating= 'R';
 

--  select film.title
--  from film
--  join inventory
--  on film.film_id = inventory.film_id 
--  join rental on 
--  inventory.inventory_id = rental.inventory_id 
--  join customer
--  on rental.customer_id = customer.customer_id
--  where customer.first_name = ‘Matthew’ and rental.return_date between ‘2005-07-28’ and ‘2005-08-01’ and film.rental_rate > 4;

-- select film.title, rental.rental_id
-- from customer
-- inner join rental on customer.customer_id = rental.customer_id
-- inner join film on film.film_id = customer.customer_id
-- where customer.first_name = 'Matthew' and customer.last_name = 'Mahan' and film.rental_rate >= 4.00 and rental.return_date < '2005-08-01' and rental.return_date >= '2005-07-28'
-- limit 1;

--  select distinct film.title,film.description,film.replacement_cost
-- from film
-- join inventory on film.film_id = inventory.film_id
-- join rental on inventory.inventory_id = rental.inventory_id
-- join customer on rental.customer_id = customer.customer_id
-- where customer.first_name = 'Matthew' and customer.last_name = 'Mahan' and film.description ilike '%boat%' or film.title ilike '%boat%'
-- order by film.replacement_cost desc limit 1;





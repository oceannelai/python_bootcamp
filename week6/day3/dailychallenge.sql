-- create table customer(
-- customer_id serial primary key,
-- customer_name varchar(50))

-- create table customer_profile(
-- customer_profile_id INTEGER not null,
-- customer_character TEXT not null,
-- primary key(customer_profile_id),
-- CONSTRAINT fk_customer_id FOREIGN KEY (customer_profile_id) REFERENCES customer (customer_id)
-- )

-- insert into customer(customer_name) values
-- ('Varsh'),('Mélodie'),('Dylan'),('Christopher'),('Jordanne');

-- insert into customer_profile(customer_profile_id,customer_character) values
-- ((SELECT customer_id FROM customer WHERE customer_name = 'Jordanne'), 'Always hungry'),
-- ((SELECT customer_id FROM customer WHERE customer_name = 'Christopher'),'wants to fight');
-- SELECT customer.customer_name,customer_profile.customer_character as character
-- FROM customer
-- FULL OUTER JOIN customer_profile
-- ON customer.customer_id = customer_profile.customer_profile_id;

-- CREATE TABLE product (
-- item_id SERIAL,	
-- product_name VARCHAR(30) NOT NULL,
-- PRIMARY KEY (item_id)
-- );
-- INSERT INTO product(product_name) VALUES
-- ('Nails'),
-- ('Tensils'),
-- ('Lamps'),
-- ('Spoons'),
-- ('Hammer'),
-- ('Phone Case'),
-- ;
-- CREATE TABLE item_order (
-- customer_id INTEGER NOT NULL,
-- item_id INTEGER NOT NULL,
-- number_order INTEGER NOT NULL,
-- PRIMARY KEY (customer_id, item_id),
-- FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON UPDATE CASCADE,
-- FOREIGN KEY (item_id) REFERENCES product(item_id) ON UPDATE CASCADE
-- );

-- INSERT INTO item_order(customer_id, item_id, number_order) VALUES
-- ((SELECT customer_id FROM customer  WHERE customer_name = 'Dylan'), (SELECT item_id FROM product WHERE product_name = 'Phone Case'), 4),
-- ((SELECT customer_id FROM customer  WHERE customer_name = 'Varsh'), (SELECT item_id FROM product WHERE product_name = 'Lamps'), 1),
-- ((SELECT customer_id FROM customer  WHERE customer_name = 'Mélodie'), (SELECT item_id FROM product WHERE product_name = 'Spoons'), 5);




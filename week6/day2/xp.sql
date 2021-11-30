--SELECT * FROM items order by item_values ASC
--SELECT * FROM items where item_values>= 80 order by item_values DESC
--SELECT first_name, last_name FROM customers order by id ASC limit 3
--SELECT last_name FROM customers order by last_name DESC

-- create table purchases(
-- purchases_id serial,
-- customer_id int,
-- item_id int,
-- primary key (purchases_id),
-- FOREIGN KEY (item_id) REFERENCES  items(id),
-- FOREIGN KEY (customer_id) REFERENCES customers(id)	
-- );
-- insert into purchases(customer_id,item_id)
-- values (4,1), (5,2);
-- select * from items
-- inner join purchases
-- on items.id = purchases.purchases_id;
-- SELECT customers.id from customers
-- inner join purchases
-- on customerS.id = purchases.purchases_id;

--select item_id from purchases where customer_id =4
--select item_id from purchases where customer_id = 1 or customer_id=2
-- insert into items(item,item_values)values 
-- ('hard drive', 150);
-- insert into purchases(customer_id, item_id)
-- values (3,4);
-- select customers.first_name, customers.last_name, item, items.item_values from customers
-- inner join purchases on purchases.customer_id = customers.id
-- inner join items on purchases.purchases_id = items.id




USE sakila;

-- 1. 문제 1
SELECT f.title FROM film f 
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.first_name = 'PENELOPE' AND a.last_name = 'GUINESS';

-- 1. 문제 2
SELECT c.name, COUNT(fc.film_id) AS number_of_films FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
GROUP BY c.name;

-- 1. 문제 3
SELECT r.rental_date, f.title FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.customer_id = 5;

-- 1. 문제 4
SELECT title FROM film ORDER BY release_year DESC LIMIT 10;

-- 2. 문제 1
SELECT a.first_name, a.last_name FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
WHERE f.title = 'ACADEMY DINOSAUR';

-- 2. 문제 2
SELECT DISTINCT c.first_name, c.last_name FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE f.title = 'ACADEMY DINOSAUR';

-- 2. 문제 3
SELECT c.customer_id, c.first_name, c.last_name, r.last_rental_date, f.title
FROM customer c
JOIN (
    SELECT r.customer_id, MAX(r.rental_date) AS last_rental_date
    FROM rental r
    GROUP BY r.customer_id
) r ON c.customer_id = r.customer_id
JOIN rental rr ON r.customer_id = rr.customer_id AND r.last_rental_date = rr.rental_date
JOIN inventory i ON rr.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id;

-- 2. 문제 4
SELECT f.title, AVG(DATEDIFF(r.return_date, r.rental_date)) as avg_rental_period
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY f.title
ORDER BY avg_rental_period DESC;

-- 3. 문제 1
SELECT f.title, COUNT(r.rental_id) AS rental_count 
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY f.title
ORDER BY rental_count DESC
LIMIT 1;

-- 3. 문제 2
SELECT c.name, AVG(f.rental_rate) AS avg_rental_rate
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN film f ON fc.film_id = f.film_id
GROUP BY c.name;

-- 3. 문제 3
SELECT YEAR(p.payment_date) AS year, MONTH(p.payment_date) AS month, SUM(p.amount) AS total_slaes
FROM payment p
GROUP BY year, month;

-- 3. 문제 4
SELECT a.first_name, a.last_name, COUNT(fa.film_id) AS number_of_films
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
GROUP BY a.first_name, a.last_name
ORDER BY number_of_films DESC;

-- 4. 문제 1
SELECT f.title, SUM(p.amount) AS total_revenue
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN payment p ON r.rental_id = p.rental_id
GROUP BY f.title
ORDER BY total_revenue DESC
LIMIT 1;

-- 4. 문제 2
SELECT f.title, f.rental_rate
FROM film f
WHERE f.rental_rate > (SELECT AVG(rental_rate) FROM film);

-- 4. 문제 3
SELECT c.customer_id, c.first_name, c.last_name, COUNT(r.rental_id) AS rental_count
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
GROUP BY c.customer_id
ORDER BY rental_count DESC
LIMIT 1;

-- 4. 문제 4
SELECT f.title, COUNT(r.rental_id) AS rental_count
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
WHERE a.first_name = 'PENELOPE' AND a.last_name = 'GUINESS'
GROUP BY f.title
ORDER BY rental_count DESC
LIMIT 1;

-- 5. 문제 1
INSERT INTO film (title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features)
VALUES ('New Adventure Movie', 'A thrilling adventure of the unknown', 2023, 1, 3, 4.99, 120, 19.99, 'PG', 'Trailers,Commentaries');

-- 5. 문제 2
UPDATE address
SET address = '123 New Address, New City'
WHERE address_id = (
    SELECT address_id
    FROM customer
    WHERE customer_id = 5 
);

-- 5. 문제 3
UPDATE rental SET return_date = NOW() WHERE rental_id = 200;

-- 5. 문제 4
DELETE FROM actor WHERE actor_id = 10;
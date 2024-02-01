USE testdatabase;
SELECT * FROM users
RIGHT JOIN orders
ON users.user_id = orders.user_id;
USE testdatabase;
-- CREATE TABLE users (
-- 	user_id INT PRIMARY KEY AUTO_INCREMENT,
-- 	username VARCHAR(10) NOT NULL UNIQUE,
-- 	email TEXT NOT NULL,
-- 	age INT
-- );
-- INSERT INTO users (username, email, age) VALUES ('john_doe', 'john@example.com', 25);
-- INSERT INTO users (username, email) VALUES ('jane_doe', 'jane@example.com');
-- INSERT INTO users (username, email, age) VALUES
--     ('alice', 'alice@example.com', 30),
--     ('bob', 'bob@example.com', 28),
--     ('charlie', 'charlie@example.com', 35);
-- INSERT INTO users (username, email) VALUES
--     ('david', 'david@example.com'),
--     ('elena', 'elena@example.com');
-- INSERT IGNORE INTO users (username, email, age) VALUES ('john_doe', 'john@example.com', 25);
INSERT INTO users (username, email, age) VALUES ('john_doe', 'john@example.com', 25)
ON DUPLICATE KEY UPDATE age = 27;
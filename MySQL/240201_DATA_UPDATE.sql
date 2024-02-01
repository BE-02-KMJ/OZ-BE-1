USE testdatabase;
-- SELECT * FROM users;
-- SET SQL_SAFE_UPDATES = 0;

-- UPDATE users
-- SET username = 'SENIOR'
-- WHERE age = 25;

-- SELECT ROW_COUNT();

-- INSERT INTO users (username, email, age) VALUES ('john_park','john@email.com', 100);

-- UPDATE users
-- SET username = CASE
-- 	WHEN age >= 60 THEN 'senior'
--     ELSE 'young'
-- END;

UPDATE users
SET username = 'top5_young'
WHERE age >= 25
LIMIT 5;

SELECT * FROM users;
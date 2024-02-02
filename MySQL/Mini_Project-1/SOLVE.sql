USE yes24;
-- CREATE TABLE Books (
--     bookID INT AUTO_INCREMENT PRIMARY KEY,
--     title VARCHAR(255) NOT NULL,
--     author VARCHAR(255),
--     publisher VARCHAR(255),
--     publishing DATE,
--     rating DECIMAL(3, 1),
--     review INT,
--     sales INT,
--     price DECIMAL(10, 2),
--     ranking INT,
--     ranking_weeks INT
-- );

-- 1. 문제 1
-- SELECT title, author FROM books;

-- 1. 문제 2
-- SELECT * FROM books WHERE rating >= 8;
 
-- 1. 문제 3
-- SELECT title, review FROM books WHERE review >= 100;

-- 1. 문제 4
-- SELECT title, price FROM books WHERE price < 20000;

-- 1. 문제 5
-- SELECT * FROM books WHERE ranking_weeks >= 4;

-- 1. 문제 6
-- SELECT * FROM books WHERE author = 'ETS 저';

-- 1. 문제 7
-- SELECT * FROM books WHERE publisher = '웅진지식하우스';

-- 2. 문제 1
-- SELECT author, COUNT(*) AS books_count FROM books GROUP BY author ORDER BY books_count DESC;

-- 2. 문제 2
-- SELECT publisher, COUNT(*) AS num_books FROM books GROUP BY publisher ORDER BY num_books DESC LIMIT 1;

-- 2. 문제 3
-- SELECT author, AVG(rating) AS avg_rating FROM books GROUP BY author ORDER BY avg_rating DESC LIMIT 9; 

-- 2. 문제 4
-- SELECT title, author FROM books WHERE ranking = 1;

-- 2. 문제 5
-- SELECT title, sales, review FROM books ORDER BY sales DESC, review DESC LIMIT 10;

-- 2. 문제 6
-- SELECT * FROM books ORDER BY publishing DESC LIMIT 5;

-- 3. 문제 1
-- SELECT author, AVG(rating) FROM books GROUP BY author;

-- 3. 문제 2
-- SELECT publishing, COUNT(*) FROM books GROUP BY publishing ORDER BY publishing DESC;

-- 3. 문제 3
-- SELECT title, AVG(price) FROM books GROUP BY title ORDER BY AVG(price) DESC;

-- 3. 문제 4
-- SELECT * FROM books ORDER BY review DESC LIMIT 5;

-- 3. 문제 5
-- SELECT ranking, AVG(review) FROM books GROUP BY ranking;

-- 4. 문제 1
-- SELECT * FROM books WHERE rating > (SELECT AVG(rating) FROM books);

-- 4. 문제 2
-- SELECT title, price FROM books WHERE price > (SELECT AVG(price) FROM books);

-- 4. 문제 3
-- SELECT * FROM books WHERE review > (SELECT MAX(review) FROM books);

-- 4. 문제 4
-- SELECT * FROM books WHERE sales < (SELECT AVG(sales) FROM books);

-- 4. 문제 5
-- SELECT * FROM books 
-- WHERE author = (SELECT author FROM books GROUP BY author ORDER BY COUNT(*) DESC LIMIT 1) 
-- ORDER BY publishing DESC LIMIT 1;

-- SET SQL_SAFE_UPDATES = 0;
-- 5. 문제 1
-- UPDATE books SET price = 99999 WHERE title = "한국사";
-- SELECT * FROM books WHERE title = "한국사";

-- 5. 문제 2
-- UPDATE books SET title = '신나신나' WHERE author = '최태성';
-- SELECT * FROM books WHERE author = '최태성';

-- 5. 문제 3
-- DELETE FROM books WHERE sales = (SELECT min_sales FROM (SELECT MIN(sales) AS min_sales FROM books) AS temp);
-- SELECT * FROM books ORDER BY sales ASC;

-- 5. 문제 4
-- UPDATE books SET rating = rating + 1 WHERE publisher = '민음사';
-- SELECT * FROM books WHERE publisher = '민음사';

-- 6. 문제 1
-- SELECT author, AVG(rating) AS avg_rating, AVG(sales) AS avg_sales FROM books GROUP BY author ORDER BY avg_rating DESC, avg_sales DESC;

-- 6. 문제 2
-- SELECT publishing, AVG(price) AS avg_price FROM books GROUP BY publishing ORDER BY publishing ASC;

-- 6. 문제 3
-- SELECT publisher, COUNT(*) AS num_books, AVG(review) AS avg_review FROM books GROUP BY publisher ORDER BY num_books DESC;

-- 6. 문제 4
-- SELECT ranking, sales FROM books ORDER BY ranking;

-- 6. 문제 5
-- SELECT price, AVG(review) AS avg_review, AVG(rating) AS avg_rating FROM books GROUP BY price ORDER BY avg_review DESC, avg_rating DESC;

-- 7 문제 1
-- SELECT publisher, author, AVG(sales) AS avg_sales FROM books GROUP BY publisher, author ORDER BY publisher, avg_sales DESC;

-- 7 문제 2
-- SELECT title, review, price FROM books
-- WHERE review > (SELECT AVG(review) FROM books) AND price < (SELECT AVG(price) FROM books);

-- 7 문제 3
-- SELECT author, COUNT(DISTINCT title) AS num_books FROM books GROUP BY author ORDER BY num_books DESC LIMIT 1;

-- 7 문제 4
-- SELECT author, MAX(sales) AS max_sales FROM books GROUP BY author;

-- 7 문제 5
-- SELECT YEAR(publishing) AS year, COUNT(*) as num_books, AVG(price) AS avg_price FROM books GROUP BY year;

-- 7 문제 6
-- SELECT publisher, MAX(rating) - MIN(rating) AS rating_difference FROM books GROUP BY publisher ORDER BY rating_difference DESC LIMIT 1;

-- 7 문제 7
SELECT title, rating / sales AS ratio FROM books WHERE author = '최태성 저' ORDER BY ratio DESC LIMIT 1;
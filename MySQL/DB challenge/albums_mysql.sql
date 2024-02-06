USE testdatabase;

-- 1.
SELECT 앨범, 연도 FROM albums;
-- 2.
SELECT * FROM albums WHERE 연도 = '2000';
-- 3.
SELECT * FROM albums WHERE 최고순위 <=10;
-- 4.
SELECT * FROM albums WHERE 최고순위 = '-';
-- 5.
SELECT 연도, COUNT(*) FROM albums GROUP BY 연도;
-- 6.
SELECT * FROM albums ORDER BY 연도 DESC LIMIT 1;
-- 7.
SELECT * FROM albums ORDER BY 연도 ASC LIMIT 1;
-- 8.
SELECT * FROM albums WHERE 최고순위 >= 10;
-- 9.
SELECT * FROM albums WHERE 앨범 LIKE '%White%';
-- 10.
SELECT * FROM albums WHERE 연도 BETWEEN '2000' AND '2005';

-- CRUD
-- 1.
INSERT INTO albums (앨범, 연도, 최고순위) VALUES ('New Album', '2024', '1');
SELECT * FROM albums ORDER BY 연도 DESC;
-- 2.
SET SQL_SAFE_UPDATES = 0;
UPDATE albums SET 최고순위 = '2' WHERE 앨범 = 'New Album';
SELECT * FROM albums ORDER BY 연도 DESC;
-- 3.
DELETE FROM albums WHERE 앨범 = 'New Album';
SELECT * FROM albums ORDER BY 연도 DESC;
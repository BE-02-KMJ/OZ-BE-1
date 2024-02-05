USE classicmodels;

-- 초. 문제 1
UPDATE customers SET addressLine1 = '456 Updated St' WHERE customerNumber = 103;

-- 초. 문제 2
UPDATE products SET buyPrice = 21.99 WHERE productCode = 'S10_1500';

-- 초. 문제 3
UPDATE employees SET jobTitle = 'Manager' WHERE employeeNumber = 1165;

-- 초. 문제 4
UPDATE offices SET phone = '123 456 7891' WHERE officeCode = 1;

-- 초. 문제 5
UPDATE orders SET status = 'In Process' WHERE orderNumber = 10501;

-- 초. 문제 6
UPDATE orderdetails SET quantityOrdered = 12 WHERE orderNumber = 10504 AND productCode = 'S10_1540';

-- 초. 문제 7
UPDATE payments SET amount = 210.00 
WHERE customerNumber = 504 AND paymentDate = '2024-02-07';

-- 초. 문제 8
UPDATE productlines SET textDescription = 'Updated description' WHERE productLine = 'Vintage Cars';

-- 초. 문제 9
UPDATE customers SET phone = '40 32 2555' WHERE customerNumber = 103;

-- 초. 문제 10
UPDATE products SET buyPrice = buyPrice * 1.1;

-- 중. 문제 1
UPDATE employees SET officeCode = 9 WHERE extension = 101;

-- 중. 문제 2
UPDATE offices SET city = 'Updated City' WHERE country = 'Korea';

-- 중. 문제 3
UPDATE orders SET status = 'Cancelled'
WHERE orderDate BETWEEN '2023-02-01' AND '2023-03-01';

-- 중. 문제 4
UPDATE orderdetails SET priceEach = priceEach * 1.1 
WHERE orderNumber IN (
SELECT orderNumber FROM orders 
WHERE orderDate BETWEEN '2023-02-01' AND '2023-03-01');

-- 중. 문제 5
UPDATE payments SET amount = amount * 1.05 WHERE customerNumber = 501;

-- 중. 문제 6
UPDATE productlines SET textDescription = 'New description' 
WHERE productLine IN ('Classic Cars', 'Trains');

-- 중. 문제 7
UPDATE customers SET phone = '999-999-9999' WHERE city = 'San Francisco';
SELECT * FROM customers WHERE city = 'San Francisco';

-- 중. 문제 8
UPDATE products SET buyPrice = buyPrice * 0.95 WHERE productLine = 'Classic Cars';
SELECT * FROM products WHERE productLine = 'Classic Cars';

-- 중. 문제 9
UPDATE employees SET extension = extension * 1.05 WHERE jobTitle = 'Manager';
SELECT * FROM employees WHERE jobTitle = 'Manager';

-- 중. 문제 10
UPDATE offices SET addressLine1 = '123 New Address St', phone = '987 654 3211' WHERE officeCode = 2;
SELECT * FROM offices;

-- 고. 문제 1
UPDATE orders SET status = 'On Hold' WHERE orderDate BETWEEN '2023-01-01' AND '2023-12-31';
SELECT * FROM orders WHERE orderDate BETWEEN '2023-01-01' AND '2023-12-31';

-- 고. 문제 2
UPDATE orderdetails SET priceEach = priceEach * 1.1 WHERE orderNumber = 10504;
SELECT * FROM orderdetails WHERE orderNumber = 10504;

-- 고. 문제 3
UPDATE payments SET paymentDate = '2024-02-05' 
WHERE paymentDate BETWEEN '2024-01-01' AND '2024-03-31';
SELECT * FROM payments WHERE paymentDate BETWEEN '2024-01-01' AND '2024-03-31';

-- 고. 문제 4
UPDATE productlines SET textDescription = 'New updated description' 
 WHERE productLine IN (
 SELECT productLine FROM products 
 WHERE quantityInStock < 50);
 SELECT * FROM productlines;
 
 -- 고. 문제 5
UPDATE customers SET addressLine2 = 'New Address' 
WHERE customerNumber BETWEEN 100 AND 150;
SELECT * FROM customers;
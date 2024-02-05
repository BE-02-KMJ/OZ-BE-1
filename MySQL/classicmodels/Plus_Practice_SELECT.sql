USE classicmodels;

-- 초. 문제 1
SELECT * FROM customers;

-- 초. 문제 2
SELECT * FROM products;

-- 초. 문제 3
SELECT * FROM employees;

-- 초. 문제 4
SELECT * FROM offices;

-- 초. 문제 5
SELECT * FROM orders ORDER BY orderDate DESC LIMIT 10;

-- 초. 문제 6
SELECT * FROM orderdetails WHERE orderNumber = 10425;

-- 초. 문제 7
SELECT * FROM payments WHERE customerNumber = 486;

-- 초. 문제 8
SELECT productLine, textDescription FROM productlines;

-- 초. 문제 9
SELECT * FROM customers WHERE city = 'NYC';

-- 초. 문제 10
SELECT * FROM products WHERE buyPrice BETWEEN 10 AND 45 ORDER BY buyPrice ASC;

-- 중. 문제 1
SELECT * FROM orders WHERE customerNumber = 124;

-- 중. 문제 2
SELECT * FROM orderdetails WHERE productCode = 'S18_4600';

-- 중. 문제 3
SELECT * FROM payments WHERE paymentDate BETWEEN '2023-01-01' AND '2024-01-31';

-- 중. 문제 4
SELECT * FROM employees WHERE jobTitle = 'Manager';

-- 중. 문제 5
SELECT * FROM offices WHERE country = 'USA';

-- 중. 문제 6
SELECT * FROM products WHERE productLine = 'Classic Cars';

-- 중. 문제 7
SELECT * FROM customers ORDER BY customerNumber DESC LIMIT 5;

-- 중. 문제 8
SELECT * FROM products WHERE quantityInStock < 50;

-- 중. 문제 9
SELECT * FROM orders WHERE orderDate BETWEEN '2023-01-01' AND '2023-02-01';

-- 중. 문제 10
SELECT orderNumber, SUM(quantityOrdered * priceEach) AS total_amount FROM orderdetails 
WHERE orderNumber = 10417 GROUP BY orderNumber;

-- 고. 문제 1
SELECT city, COUNT(*) AS customerCount FROM customers GROUP BY city;

-- 고. 문제 2
SELECT productline, AVG(buyPrice) AS avg_price FROM products GROUP BY productLine;

-- 고. 문제 3
SELECT officeCode, COUNT(*) AS employeeCount FROM employees GROUP BY officeCode;

-- 고. 문제 4
SELECT officeCode, AVG(extension) AS avg_salary FROM employees GROUP BY officeCode;

-- 고. 문제 5
SELECT productCode, SUM(quantityOrdered) AS total_ordered FROM orderdetails
GROUP BY productCode ORDER BY total_ordered DESC LIMIT 5; 
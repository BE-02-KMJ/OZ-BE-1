USE classicmodels;

-- 초. 문제 1
DELETE FROM customers WHERE customerNumber = 504;

-- 초. 문제 2
DELETE FROM products WHERE productCode = 'S10_1500';

-- 초. 문제 3
DELETE FROM employees WHERE employeeNumber = 2425

-- 초. 문제 4
DELETE FROM offices WHERE officeCode = 9;

-- 초. 문제 5
DELETE FROM orders WHERE orderNumber = 10505;

-- 초. 문제 6
DELETE FROM orderdetails WHERE orderNumber = 10504;

-- 초. 문제 7
DELETE FROM payments WHERE customerNumber = 504;

-- 초. 문제 8
DELETE FROM productlines WHERE productLine = 'Classic Cars_ex';

-- 초. 문제 9
DELETE FROM customers WHERE city = 'Seattle';

-- 초. 문제 10
DELETE FROM products WHERE productLine = 'Classic Cars_ex';

-- 중. 문제 1
DELETE FROM employees WHERE officeCode = 9;

-- 중. 문제 2
DELETE FROM offices WHERE country = 'Germany';

-- 중. 문제 3
DELETE FROM orders WHERE orderDate BETWEEN '2024-01-01' AND '2024-12-31';

-- 중. 문제 4
DELETE FROM orderdetails WHERE orderNumber = 10503;

-- 중. 문제 5
DELETE FROM payments WHERE customerNumber = 501;

-- 중. 문제 6
DELETE FROM productlines WHERE productLine IN ('Motorcycles', 'Planes');

-- 중. 문제 7
DELETE c
FROM customers c
JOIN (
  SELECT customerNumber
  FROM customers
  ORDER BY customerNumber DESC
  LIMIT 5
) AS sub
ON c.customerNumber = sub.customerNumber;

-- 중. 문제 8
DELETE FROM products WHERE quantityInStock < 50;

-- 중. 문제 9
DELETE FROM employees WHERE jobTitle = 'Manager';

-- 중. 문제 10
DELETE FROM offices
WHERE officeCode = (
  SELECT officeCode
  FROM (
    SELECT officeCode, COUNT(*) AS office_employee_count
    FROM employees
    GROUP BY officeCode
    ORDER BY office_employee_count ASC
    LIMIT 1
  ) AS min_office
);

-- 고. 문제1
DELETE FROM orders WHERE orderDate BETWEEN '2024-01-01' AND '2024-03-01';

-- 고. 문제 2
DELETE od
FROM orderdetails od
JOIN (
  SELECT productCode
  FROM products
  ORDER BY quantityInStock ASC
  LIMIT 5
) AS sub
ON od.productCode = sub.productCode;

-- 고. 문제 3
DELETE FROM payments WHERE amount < 200;

-- 고. 문제 4
DELETE FROM productlines WHERE productLine NOT IN (SELECT DISTINCT productLine FROM products);

-- 고. 문제 5
DELETE c 
FROM customers c
JOIN (
	SELECT orderNumber
    FROM orders
    WHERE orderDate < '2022-01-01'
) AS o
ON c.customerNumber = o.customerNumber;
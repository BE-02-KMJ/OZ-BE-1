USE classicmodels;
-- SELECT o.orderNumber, c.customerName
-- FROM orders o
-- JOIN customers c ON o.customerNumber = c.customerNumber;

-- SELECT p.productName, p.productLine, pl.textDescription
-- FROM products p
-- JOIN productlines pl ON p.productLine = pl.productLine;

-- SELECT e1.employeeNumber, e1.firstName, e1.lastName, e2.firstName 
-- AS 'ManagerFirstname', e2.lastName AS 'ManagerLastName'
-- FROM employees e1
-- LEFT JOIN employees e2 ON e1.reportsTo = e2.employeeNumber;

SELECT e.employeeNumber, e.lastName, e.firstName, e.extension, e.email, e.officeCode, e.reportsTo, e.jobTitle
FROM employees e
JOIN offices o ON e.officeCode = o.officeCode
WHERE o.city = 'San Francisco';
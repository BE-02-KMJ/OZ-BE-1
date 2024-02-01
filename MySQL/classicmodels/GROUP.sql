USE classicmodels;
-- SELECT productLine, COUNT(*) AS productCount
-- FROM products
-- GROUP BY productLine;

-- SELECT customers.customerNumber, 
--        customers.customerName, 
--        SUM(orderdetails.quantityOrdered * orderdetails.priceEach) AS totalAmount
-- FROM customers
-- JOIN orders ON customers.customerNumber = orders.customerNumber
-- JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber
-- GROUP BY customers.customerNumber, customers.customerName
-- ORDER BY totalAmount DESC;

-- SELECT productName, SUM(quantityOrdered) AS totalQuantity
-- FROM orderdetails od
-- JOIN products p ON od.productCode = p.productCode
-- GROUP BY productName
-- ORDER BY totalQuantity DESC
-- LIMIT 1;

SELECT o.city, SUM(od.quantityOrdered * od.priceEach) AS totalSales
FROM orders ord
JOIN orderdetails od ON ord.orderNumber = od.orderNumber
JOIN customers c ON ord.customerNumber = c.customerNumber
JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber
JOIN offices o ON e.officeCode = o.officeCode
GROUP BY o.city
ORDER BY totalSales DESC
LIMIT 1;
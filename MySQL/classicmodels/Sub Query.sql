USE classicmodels;
-- SELECT orderNumber, SUM(quantityOrdered * priceEach) AS totalAmount
-- FROM orderdetails
-- GROUP BY orderNumber
-- HAVING totalAmount > 500;

-- SELECT customerNumber, SUM(amount) AS totalPayment
-- FROM payments
-- GROUP BY customerNumber
-- HAVING totalPayment > (SELECT AVG(amount) FROM payments) 
-- ORDER BY totalPayment DESC;

-- SELECT customerName
-- FROM customers
-- WHERE customerNumber NOT IN (SELECT customerNumber FROM orders);

SELECT c.customerName, SUM(od.quantityOrdered * od.priceEach) AS totalSpent
FROM customers c
JOIN orders o ON c.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
GROUP BY c.customerName
ORDER BY totalSpent DESC
LIMIT 1;
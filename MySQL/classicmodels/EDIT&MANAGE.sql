USE classicmodels;
-- INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, 
-- addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)
-- VALUES (497, 'New Customer', 'Lastname', 'Firstname', '123-456-7890', 
-- '123 Street', 'Suite 1', 'City', 'State', 'PostalCode', 'Country', 1002, 50000.00);
-- SELECT ROW_COUNT();

-- UPDATE products
-- SET buyPrice = buyPrice * 1.10
-- WHERE productLine = 'Classic Cars';

-- UPDATE customers
-- SET email = 'newemail@example.com'
-- WHERE customerNumber = 103;

UPDATE employees
SET officeCode = '2'
WHERE employeeNumber = 1002;
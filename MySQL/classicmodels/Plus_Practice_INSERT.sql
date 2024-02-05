-- USE classicmodels;

-- -- 1-초. 문제 1
-- INSERT INTO customers (customerNumber, customerName, phone, addressLine1, city, postalCode, country)
-- VALUES (500, 'John Doe', '+82 123 4567', '123 Main St', 'Seoul', '12345', 'Korea');

-- -- 1-초. 문제 2
-- INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
-- VALUES ('S10_1500', 'Toy Car', 'Classic Cars', '1:100', 'Autoart Studio Design', 'example', '100', '19.99', '100');

-- -- 1-초. 문제 3
-- INSERT INTO employees (employeeNumber, lastName, firstName, extension, email, officeCode, jobTitle) 
-- VALUES ('2425', 'Johnson', 'Alice', '1500', 'example@email.com', '5', 'Sales Rep');

-- -- 1-초. 문제 4
-- INSERT INTO offices (officeCode, city, phone, addressLine1, country, postalCode, territory)
-- VALUES ('8', 'Seoul', '+82 02 123 4567', '123 Main Park St', 'Korea', '12345', 'S.Korea');

-- -- 1-초. 문제 5
-- INSERT INTO orders (orderNumber, orderDate, requiredDate, status, customerNumber)
-- VALUES ('10500', '2023-01-01', '2024-02-29', 'In Process', '500');

-- -- 1-초. 문제 6
-- INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber)
-- VALUES (10500, 'S10_1500', 5, 20.00, 13);

-- -- 1-초. 문제 7
-- INSERT INTO payments (customerNumber, checkNumber, paymentDate, amount) 
-- VALUES (500, 'MJ240205', '2023-01-01', 178);

-- -- 1-초. 문제 8
-- INSERT INTO productlines (productLine, textDescription) 
-- VALUES ('Classic Cars_ex', 'Various classic cars models');

-- -- 1-초. 문제 9
-- INSERT INTO customers (customerNumber, customerName, phone, addressLine1, city, state, postalCode, country) 
-- VALUES (499, 'Jane Smith', '2125551512', '456 Elm St', 'NYC', 'NY', 10030, 'USA');

-- -- 1-초. 문제 10
-- INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP) 
-- VALUES ('S10_1501', 'Vintage Train', 'Trains', '1:50', 'Classic Metal Creations', 'Miniature Train', 135, 34.99, 168.6);

-- -- 1-중. 문제 1
-- INSERT INTO customers (customerNumber, customerName, phone, addressLine1, city, postalCode, country)
-- VALUES (501, 'Jane Smith', '987-654-3210', '456 Elm Street', 'Los Angeles', '90001', 'USA'), 
-- 	(502, 'Michael Johnson', '555-123-4567', '789 Oak Avenue', 'Chicago', '60601', 'USA');

-- -- 1-중. 문제 2
-- INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP) 
-- VALUES ('S10_1510', 'Model Ship', 'Classic Cars', '1:18', 'Ships', 'Detailed replica of a ship', 50, 99.99, 149.99),
-- 	('S10_1515', 'Vintage Motorcycle', 'Motorcycles', '1:24', 'Exoto Designs', 'Miniature replica of a vintage motorcycle', 30, 49.99, 79.99);
  
-- -- 1-중. 문제 3
-- INSERT INTO employees (employeeNumber, lastName, firstName, extension, email, officeCode, jobTitle) 
-- VALUES (1801, 'Smith', 'John', 1234, 'john.smith@email.com', 1, 'Manager'),
-- 	(1802, 'Johnson', 'Emma', 2345, 'emma.johnson@email.com', 2, 'Sales Rep');
  
-- -- 1-중. 문제 4
-- INSERT INTO orders (orderNumber, orderDate, requiredDate, status, customerNumber) 
-- VALUES (10501, '2023-02-05', '2023-02-15', 'Pending', 501);
-- INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber) 
-- VALUES (10501, 'S10_1510', 2, 99.99, 1), (10501, 'S10_1515', 3, 49.99, 2);

-- -- 1-중. 문제 5
-- INSERT INTO payments (customerNumber, checkNumber, paymentDate, amount) 
-- VALUES (501, 'CK240206', '2023-02-02', 250.99), (501, 'CK240207', '2023-02-03', 150.50);

-- -- 1-중. 문제 6
-- INSERT INTO customers (customerNumber, customerName, phone, addressLine1, city, postalCode, country)
-- VALUES (503, 'XYZ Corp', '987-654-3210', '123 Main Street', 'Seoul', '12345', 'Korea');
-- INSERT INTO orders (orderNumber, orderDate, requiredDate, status, customerNumber)
-- VALUES (10502, '2023-02-10', '2023-02-20', 'Pending', 503);

-- -- 1-중. 문제 7
-- INSERT INTO employees (employeeNumber, lastName, firstName, extension, email, officeCode, jobTitle) 
-- VALUES (1803, 'Smith', 'John', 'x1234', 'jsmith@example.com', 1, 'Sales Rep');
-- UPDATE employees SET jobTitle = 'Manager' 
-- WHERE employeeNumber = LAST_INSERT_ID(); 

-- -- 1-증. 문제 8
-- INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP) 
-- VALUES ('S10_1520', 'Vintage Wood Rocking Horse', 'Vintage Cars', '1:10', 'Red Start Diecast', 'Hand crafted wooden toy', 10, 50.00, 100.00);
-- UPDATE products SET quantityInStock = 30 WHERE productCode = LAST_INSERT_ID();

-- -- 1-중. 문제 9
-- SET SQL_SAFE_UPDATES = 0;
-- INSERT INTO offices (officeCode, city, phone, addressLine1, country, postalCode, territory) 
-- VALUES (9, 'Berlin', '+49 30 12345678', '123 Hauptstrasse', 'Germany', 54321, 'EMEA');
-- UPDATE employees SET officeCode = 9 WHERE lastName = 'Smith';

-- -- 1-중. 문제 10
-- INSERT INTO productlines (productLine, textDescription)
-- VALUES ('Sports Cars', 'Various sports car models');
-- INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP) 
-- VALUES ('S10_1530', 'Porsche 911', 'Sports Cars', '1:18', 'Exquisite Cars', '1:18 scale diecast model of a Porsche 911', 50, 79.99, 99.99), 
-- ('S10_1531', 'Ferrari 488', 'Sports Cars', '1:18', 'Exquisite Cars', '1:18 scale diecast model of a Ferrari 488', 40, 89.99, 119.99);

-- -- 1-고. 문제 1
-- INSERT INTO customers (customerNumber, customerName, phone, addressLine1, city, postalCode, country)
-- VALUES (504, 'Emily Davis', '555-987-6543', '321 Pine St', 'Seattle', '98101', 'USA');
-- INSERT INTO orders (orderNumber, orderDate, requiredDate, status, customerNumber) 
-- VALUES (10503, '2024-02-05', '2024-02-10', 'In Progress', 504);
-- INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber)
-- VALUES (10503, 'S10_1530', 2, 79.99, 7);

-- -- 1-고. 문제 2
-- INSERT INTO employees (employeeNumber, lastName, firstName, extension, email, officeCode, jobTitle) 
-- VALUES (1804, 'Johnson', 'Emily', 'x5678', 'emily.johnson@example.com', 2, 'Sales Rep'); 
-- UPDATE employees SET reportsTo = (SELECT employeeNumber FROM employees WHERE lastName = 'Johnson') 
-- WHERE lastName = 'Smith';

-- -- 1-고. 문제 3
-- INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
-- VALUES ('S10_1540', 'Widget', 'Classic Cars_ex', '1:10', 'ABC Company', 'A fun and interactive toy', 50, 19.99, 29.99);
-- INSERT INTO orders (orderNumber, orderDate, requiredDate, status, customerNumber) 
-- VALUES (10504, '2024-02-05', '2024-02-10', 'In Process', 499); 
-- INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber) 
-- VALUES (10504, 'S10_1540', 2, 19.99, 3);

-- 1-고. 문제 4
-- INSERT INTO orders (orderNumber, orderDate, requiredDate, status, customerNumber) 
-- VALUES (10505, '2024-02-06', '2024-02-11', 'Pending', 504); 
-- INSERT INTO payments (customerNumber, checkNumber, paymentDate, amount) 
-- VALUES (504, 'CHK123456', '2024-02-07', 99.99);

-- 1-고. 문제 5
INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber) 
VALUES (10502, 'S10_1520', 3, 25.00, 6);
UPDATE products SET quantityInStock = quantityInStock - 3 
WHERE productCode = 'S10_1520';
-- create database testdatabase;
-- use testdatabase;
-- create table users (
-- 	id int auto_increment primary key,
--     username varchar(30) not null,
--     email varchar(100) unique,
--     is_business varchar(10) default false,
--     age int check (age >= 18)
-- );
use testdatabase;

-- CREATE TABLE users (
-- 	user_id int primary key,
--     name varchar(100),
--     age int
-- );

-- insert into users (user_id, name, age)
-- values (1, 'Alice', 25),
--        (2, 'Bob', 30),
--        (3, 'Charlie', 22),
--        (4, 'David', 33),
--        (5, 'Eve', 28);

-- create table orders (
-- 	order_id int primary key,
--     user_id int,
--     order_date date
-- );

insert into orders (order_id, user_id, order_date)
values (101, 1, '2023-01-01'),
       (102, 2, '2023-02-01'),
       (103, 1, '2023-02-15'),
       (104, 3, '2023-03-01'),
       (105, 4, '2023-03-10');
USE kream;
create table kream (
	img text,
	brand text,
	product_name text,
	price text
);
ALTER TABLE kream CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
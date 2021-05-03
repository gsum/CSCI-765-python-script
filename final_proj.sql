-- users table
select id, first_name, last_name, email into outfile '/tmp/mysql-files/users.csv' fields terminated by ',' optionally enclosed by '"' lines terminated by '\n' from users;

-- orders table
show taid, user_id, date into outfile '/tmp/mysql-files/orders.csv' fields terminated by ',' optionally enclosed by '"' lines terminated by '\n' from orders;

-- deals table
select id, name, price into outfile '/tmp/mysql-files/deals.csv' fields terminated by ',' optionally enclosed by '"' lines terminated by '\n' from deals;

-- order_items table
select id, order_id, deal_id into outfile '/tmp/mysql-files/order_items.csv' fields terminated by ',' optionally enclosed by '"' lines terminated by '\n' from order_items;
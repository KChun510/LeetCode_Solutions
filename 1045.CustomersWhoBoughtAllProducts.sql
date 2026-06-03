# Write your MySQL query statement below
with prod_count as (select count(product_key) as count from Product),
user_count as (select c.customer_id, count(distinct c.product_key) as count_u from Customer c group by c.customer_id)
select u.customer_id from user_count u, prod_count p 
where u.count_u >= p.count;

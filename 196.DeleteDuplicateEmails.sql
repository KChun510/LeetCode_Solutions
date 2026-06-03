# Write your MySQL query statement below
with real_email as (select min(id) as id, email from Person group by email)
delete from Person
where Person.id not in (select real_email.id from real_email)

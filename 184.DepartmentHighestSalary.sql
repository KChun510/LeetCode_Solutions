# Write your MySQL query statement below
# First get a table with the max sals,
# Then take any other employees with == to sals,  but diff employ id
with max_table as (
    select e.name, max(e.salary) as salary, d.id
    from Employee e left join Department d on e.departmentId = d.id
    group by d.name
) select distinct d.name as Department, e.name as Employee, e.salary as Salary 
    from Employee e left join Department d on e.departmentId = d.id, max_table mt
    where d.id = (select mt1.id from max_table mt1 where d.id = mt1.id and e.salary >= mt1.salary);





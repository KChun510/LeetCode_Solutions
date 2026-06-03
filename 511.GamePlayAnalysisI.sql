# Write your MySQL query statement below
select a.player_id, a.event_date as first_login 
from Activity a
where a.event_date = (select min(a1.event_date) from Activity a1 where a1.player_id = a.player_id group by a1.player_id)

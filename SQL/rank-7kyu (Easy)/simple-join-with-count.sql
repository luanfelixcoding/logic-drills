/*
Codewars Challenge: SQL Basics: Simple JOIN with COUNT
Rank: 7 kyu
URL: https://www.codewars.com/kata/580918e24a85b05ad000010c
*/

-- Create your SELECT statement here
select p.id,
       p.name,
      COUNT(t.people_id) as "toy_count"
from people p
left join toys t on t.people_id = p.id
group by p.id, p.name;
/*
Codewars Challenge: SQL Basics: Simple HAVING
Rank: 6 kyu
URL: https://www.codewars.com/kata/58164ddf890632ce00000220
*/

-- Create your SELECT statement here
SELECT age,
      COUNT(*) as "total_people"
FROM people p
GROUP BY age
HAVING COUNT(*) >= 10;
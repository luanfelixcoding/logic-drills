/*
Codewars Challenge: Easy SQL: Counting and Grouping
Rank: 7 kyu
URL: https://www.codewars.com/kata/594633020a561e329a0000a2
*/

SELECT 
  demographics.race,
  COUNT(*) as count_races
FROM demographics
GROUP BY demographics.race
ORDER BY count_races DESC;
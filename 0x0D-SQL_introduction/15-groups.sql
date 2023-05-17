-- This script lists the number of records with the same score in the table second_table.
-- This also makes sure the records are ordered by descending count.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;

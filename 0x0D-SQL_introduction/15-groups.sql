-- script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in MySQL server
-- The result display the score and the number of records this score with tha label number
-- the list is sorted by the number of records (descending)
-- the database is passed as argument of mysql command
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score HAVING number >= 1
ORDER BY number DESC;

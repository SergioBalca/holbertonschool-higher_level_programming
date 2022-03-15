-- script that lists all records with a score >= 10 in the second_table of database hbtn_0c_0 in MySQL server
-- Results show score and name
-- Records are ordered by score (top first)
-- the database name is passed as argument of mysql command
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

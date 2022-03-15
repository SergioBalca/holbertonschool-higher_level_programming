-- script that lists all records of the table second_table of the database hbtn_0c_0 in MySQL server
-- results display the score and the name
-- Records are ordered by score (top first)
-- the database name is passed as an argument to mysql command
SELECT score, name
FROM second_table
ORDER BY score DESC;

-- script that lists all records of the table second_table of the database hbtn_0c_0 in MySQL server
-- Rows without name value are not listed
-- Results display the score and the name
-- Records are listed by descending score
-- The database name is passed as argumento of mysql command
SELECT score, name
FROM second_table
WHERE name IS NOT NULL;

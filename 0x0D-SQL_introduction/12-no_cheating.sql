-- script that updates the score of Bob to 10 in the second_table
-- the database name is passed as argument to mysql command
UPDATE second_table
SET score = 10
WHERE name = 'Bob';

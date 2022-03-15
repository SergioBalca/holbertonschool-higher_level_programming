-- script that converts hbtn_0c_0 database to UTF-8 (utf8mb4, collate utf8mb4_unicode_ci) in MySQl server
-- The conversion is for the database, first_table and field name in first_table
USE hbtn_0c_0
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

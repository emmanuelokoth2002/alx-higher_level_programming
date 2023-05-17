-- Script: Create Table force_name
SET @database_name = 'your_database_name';
CREATE TABLE IF NOT EXISTS @database_name.force_name (
  id INT,
  name VARCHAR(256) NOT NULL
);

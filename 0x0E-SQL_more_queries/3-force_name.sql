-- Script: Create Table force_name
SET @database_name = 'your_database_name';
SELECT COUNT(*) INTO @table_exists
FROM information_schema.tables
WHERE table_schema = @database_name
AND table_name = 'force_name';

-- Create the table only if it doesn't already exist
IF @table_exists = 0 THEN
    CREATE TABLE @database_name.force_name (
        id INT,
        name VARCHAR(256) NOT NULL
    );
END IF;

-- Write a script that creates the table id_not_null on your MySQL server.
IF @table_exists = 0 THEN
    CREATE TABLE id_not_null (
        id INT DEFAULT 1,
        name VARCHAR(256)
    );

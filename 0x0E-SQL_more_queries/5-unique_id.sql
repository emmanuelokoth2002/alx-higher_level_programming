-- creates the table unique_id on your MySQL server
IF @table_exists = 0 THEN
    CREATE TABLE unique_id (
        id INT DEFAULT 1,
        name VARCHAR(256),
        UNIQUE (id)
    );

-- script that creates the database hbtn_0d_usa and the table states
IF @table_exists = 0 THEN
    CREATE TABLE states (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(256) NOT NULL
    );

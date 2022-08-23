
-- creating a database
CREATE DATABASE IF NOT EXISTS todos;

-- dropping
DROP DATABASE IF EXISTS todos;

-- select the database to use
USE todos;

-- showing available databases
SHOW DATABASES;

-- Create a table todos

CREATE TABLE IF NOT EXISTS todos(
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    completed TINYINT(1) NOT NULL DEFAULT 0, -- 0 OR 1
--    completed BIT NOT NULL DEFAULT 0, 0 OR 1
    PRIMARY KEY(id)
);
-- 1, 0

-- showing tables
SHOW TABLES;

-- describing tables
DESCRIBE todos;
DESC todos;



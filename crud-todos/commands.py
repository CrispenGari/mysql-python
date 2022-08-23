

CREATE_TABLE_COMMAND = """
CREATE TABLE IF NOT EXISTS todos(
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    completed TINYINT(1) NOT NULL DEFAULT 0, -- 0 OR 1
--    completed BIT NOT NULL DEFAULT 0, 0 OR 1
    PRIMARY KEY(id)
);
"""

INSERT_COMMAND      = "INSERT INTO todos(title) VALUES('{}');"
DELETE_COMMAND      = "DELETE FROM todos WHERE id={};"
UPDATE_COMMAND      = "UPDATE todos SET completed={} WHERE id={};"
ALL_TODOS_COMMAND   = "SELECT * FROM todos;"
SINGLE_TODO_COMMAND = "SELECT * FROM todos WHERE id={} LIMIT 1;"
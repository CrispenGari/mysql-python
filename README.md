### MySQL Python
In this one we are going to learn how we can configure python to connect with mysql server.

### Installing MSQL Connector

```shell
pip install mysql-connector-python
```

### Testing the connection.
To test the connection create a python file and add the following code in it:

```python
from mysql import connector

config ={
    'host': '127.0.0.1' or 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'todos',
    'port': 3306
}
conn = connector.connect(**config)
# closing the connection
conn.close()
```

### Refs

1. [w3schools](https://www.w3schools.com/python/python_mysql_getstarted.asp)
2. [dev.mysql.com](https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html)
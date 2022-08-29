
```shell
"""
    USER - > PROFILE
         - > POSTS  -> TAGS  
         
1. 1-1 relationship (user, profile)
    user (username, email, password, id, profileId)
    profile(id, phoneNumber, photoURL)

2. 1-M relationship (user, posts)
3. N-M relationship (posts, tags)
"""
```
1. create a database
```shell
CREATE DATABASE IF NOT EXISTS relations;
```
2. select the database
```sql
USE relations;
```
3. create a profile table.

```sql
CREATE TABLE IF NOT EXISTS profiles(
	id INT NOT NULL AUTO_INCREMENT,
    phoneNumber VARCHAR(15),
    photoURL VARCHAR(1000),
    PRIMARY KEY(id)
);
```

````shell
+-------------+---------------+------+-----+---------+----------------+
| Field       | Type          | Null | Key | Default | Extra          |
+-------------+---------------+------+-----+---------+----------------+
| id          | int           | NO   | PRI | NULL    | auto_increment |
| phoneNumber | varchar(15)   | YES  |     | NULL    |                |
| photoURL    | varchar(1000) | YES  |     | NULL    |                |
+-------------+---------------+------+-----+---------+----------------+
````

4. create the user table:
````sql
CREATE TABLE IF NOT EXISTS users(
	id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(1000) NOT NULL,
    profileId INT UNIQUE,
    PRIMARY KEY(id),
    FOREIGN KEY(profileId) REFERENCES profiles(id) ON DELETE SET NULL
);
````

```shell
+-----------+---------------+------+-----+---------+----------------+
| Field     | Type          | Null | Key | Default | Extra          |
+-----------+---------------+------+-----+---------+----------------+
| id        | int           | NO   | PRI | NULL    | auto_increment |
| username  | varchar(20)   | NO   | UNI | NULL    |                |
| email     | varchar(255)  | NO   | UNI | NULL    |                |
| password  | varchar(1000) | NO   |     | NULL    |                |
| profileId | int           | YES  | UNI | NULL    |                |
+-----------+---------------+------+-----+---------+----------------+
```
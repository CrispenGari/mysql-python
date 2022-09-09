
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

5. create table posts

````sql
CREATE TABLE IF NOT EXISTS posts(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    url VARCHAR(255),
    userId INT NOT NULL,
    FOREIGN KEY(userId) REFERENCES users(id) ON DELETE CASCADE
);
````

````shell
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int          | NO   | PRI | NULL    | auto_increment |
| title  | varchar(255) | NO   |     | NULL    |                |
| url    | varchar(255) | YES  |     | NULL    |                |
| userId | int          | NO   | MUL | NULL    |                |
+--------+--------------+------+-----+---------+----------------+
````

### Many To Many
* posts and tags

````sql
CREATE TABLE IF NOT EXISTS tags(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    tag VARCHAR(255) NOT NULL UNIQUE
);
````

````shell
+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| id    | int          | NO   | PRI | NULL    | auto_increment |
| tag   | varchar(255) | NO   |     | NULL    |                |
+-------+--------------+------+-----+---------+----------------+
````

1. associate table - these table allows us to create many to many relationships between two tables.

````sql
CREATE TABLE IF NOT EXISTS posts_tags(
    tagId INT,
    postId INT,
    FOREIGN KEY(tagId) REFERENCES tags(id) ON DELETE SET NULL,
    FOREIGN KEY(postId) REFERENCES posts(id) ON DELETE CASCADE
);
````

````shell
+--------+------+------+-----+---------+-------+
| Field  | Type | Null | Key | Default | Extra |
+--------+------+------+-----+---------+-------+
| tagId  | int  | YES  | MUL | NULL    |       |
| postId | int  | YES  | MUL | NULL    |       |
+--------+------+------+-----+---------+-------+
````

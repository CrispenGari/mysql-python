

CREATE_USER = "INSERT INTO users(username, email, password, profileId) VALUES(%s, %s, %s, %s);"
CREATE_USER_PROFILE = "INSERT INTO profiles(phoneNumber, photoURL) VALUES(%s, %s);"
GET_PROFILE_MODEL = "SELECT MAX(id) FROM profiles;"

LOGIN_USER = "SELECT id, password FROM users WHERE email=%s OR username=%s;"
GET_USER = "SELECT users.id, username, email, photoURL, phoneNumber FROM users LEFT JOIN profiles ON profiles.id = users.profileId WHERE users.id=%s;"


# POSTS

CREATE_POST = "INSERT INTO posts(title, url, userId) VALUES(%s, %s, %s);"
CREATE_TAG = "INSERT INTO tags(tag) VALUES(%s);"
GET_TAG_ID = "SELECT MAX(id) FROM tags;"
GET_TAG_BY_NAME = "SELECT id FROM tags WHERE tag=%s;"

POST_TAGS_CREATE = "INSERT INTO posts_tags(postId, tagId) VALUES(%s, %s);"

GET_POST = """
SELECT posts.id, username, email, profileId, title, url, userId, photoURL, phoneNumber FROM 
posts LEFT JOIN users ON users.id = posts.userId LEFT JOIN profiles ON profiles.id = users.profileId
WHERE users.id=%s;
"""
GET_RECENT_POST = "SELECT MAX(id) FROM posts;"

GET_POST_TAGS = """SELECT tagId, tag, id from posts_tags LEFT JOIN tags ON tags.id = posts_tags.tagId WHERE postId = %s"""
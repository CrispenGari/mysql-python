

CREATE_USER = "INSERT INTO users(username, email, password, profileId) VALUES(%s, %s, %s, %s);"
CREATE_USER_PROFILE = "INSERT INTO profiles(phoneNumber, photoURL) VALUES(%s, %s);"
GET_PROFILE_MODEL = "SELECT MAX(id) FROM profiles;"

LOGIN_USER = "SELECT id, password FROM users WHERE email=%s OR username=%s;"
GET_USER = "SELECT users.id, username, email, photoURL, phoneNumber FROM users LEFT JOIN profiles ON profiles.id = users.profileId WHERE users.id=%s;"


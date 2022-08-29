

CREATE_USER = "INSERT INTO users(username, email, password, profileId) VALUES(%s, %s, %s, %s);"
CREATE_USER_PROFILE = "INSERT INTO profiles(phoneNumber, photoURL) VALUES(%s, %s);"
GET_PROFILE_MODEL = "SELECT MAX(id) FROM profiles;"

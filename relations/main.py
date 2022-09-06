
from mysql import connector
from config import config
from commands import *
from helperfns.tables import tabulate_data
import bcrypt

conn = connector.connect(**config)
cursor = conn.cursor()

def register():
    username = input("Username: \n").strip()
    email = input("Email: \n").strip()
    password = input("Password: \n").strip()
    phoneNumber = input("Phone Number: \n").strip()
    photoURL = input("Photo URL: \n").strip()
    #  CREATING THE PROFILE
    cursor.execute(CREATE_USER_PROFILE, (phoneNumber, photoURL))
    conn.commit() # saving changes
    # GET THE PROFILE ID
    cursor.execute(GET_PROFILE_MODEL)
    profileId = cursor.fetchone()[0]
    # CREATE THE USER WITH HASHED PASSWORD
    hashedPassword = bcrypt.hashpw(password.encode(), bcrypt.gensalt(12))
    cursor.execute(CREATE_USER, (username, email, hashedPassword, profileId))
    conn.commit()
    print("You are registered")


def login():
    usernameOrEmail = input("Username or Email: \n").strip()
    password = input("Password: \n").strip()
    cursor.execute(LOGIN_USER, (usernameOrEmail, usernameOrEmail))
    _user = cursor.fetchone()
    if _user is None:
        print("Invalid username or email")
        return
    _id, _pass = _user
    if bcrypt.checkpw(password.encode(), _pass.encode()):
        cursor.execute(GET_USER, (_id, ))
        user = cursor.fetchone()
        tabulate_data(["id", "username", "email", "photoURL", "phoneNumber"], [user], "Logged In User.")
    else:
        print("Invalid password")

def create_post(userId:int):
    title = input("Enter Post Title: ").strip()
    url = input("Photo URL: ").strip()
    cursor.execute(CREATE_POST, (title, url, userId))
    conn.commit()
    print("Post Created!!")

def get_post():
    id = int(input("User ID: ").strip())
    cursor.execute(GET_POST, (id, ))
    data = [row for row in cursor]
    tabulate_data(["postId"] + "username, email, profileId, title, url, userId, photoURL, phoneNumber".split(", "), data, "Post of User.")

if __name__ == "__main__":
    # get_post()
    # register()
    # create_post()
    # login()
    # close connection
    conn.close()

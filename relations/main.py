
from mysql import connector
from config import config
from commands import *
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

if __name__ == "__main__":
    register()
    # close connection
    conn.close()

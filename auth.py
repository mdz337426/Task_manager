from sqlite3 import IntegrityError
import time
import getpass

    
def login(username,cursor):
    password = getpass.getpass("Enter password: ")
    cursor.execute("SELECT password FROM user WHERE username=?", (username,))
    time.sleep(1)
    user = cursor.fetchone()
    try:
        if not user:
            raise Exception(f"❌ username '{username}' not found.")
        userp = user[0]
        if userp != password:
            print("❌ Incorrect password.")
            login(username,cursor)
        return True
    except Exception as e:
        print(f"{e}")
        exit(-1)      


def signup(username,cursor,db):
    try:
        if not username.islower():
            raise Exception("Error '{username}' Only lowercase letters are allowed !!!")
        password = getpass.getpass("Enter password: ")
        cursor.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, password))
        db.commit()
    except IntegrityError:
        print("❌ Username already exists! Try a different one.")
        exit(-1)
    except Exception as e:
        print(f'{e}')
        exit(-1)

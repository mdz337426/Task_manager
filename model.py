
def model_setup(cursor, db):
    # Usser Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
    userid INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
    )
    """)


    # List Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS list (
        listId INTEGER PRIMARY KEY AUTOINCREMENT,
        userid INTEGER NOT NULL,
        listname TEXT NOT NULL,
        FOREIGN KEY (userid) REFERENCES user(userid) ON DELETE CASCADE
    )
    """)

    # Task Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS task (
        taskid INTEGER PRIMARY KEY AUTOINCREMENT,
        listid INTEGER NOT NULL,
        taskname TEXT NOT NULL,
        status TEXT DEFAULT 'pending',
        FOREIGN KEY (listid) REFERENCES list(listid) ON DELETE CASCADE
    )
    """)
    db.commit()




    



import sqlite3

user_struct = "(username, password)"
list_struct = "(userid, listname)"
task_struct = "(listid, taskname, status)"

def get_userID(username, cursor):
    cursor.execute("SELECT userid FROM user WHERE username=?", (username,))
    user = cursor.fetchone()
    return int(user[0])

def get_listid(cursor, userid, listname):
    cursor.execute("SELECT listId FROM list WHERE userid=? and listname=?", (userid,listname))
    listid = cursor.fetchone()
    return int(listid[0])


class crud_list:
    def __init__(self, username, cursor, db):
        self.userid = str(get_userID(username, cursor)) 
        self.cursor = cursor
        self.db = db

    def show_list(self):
        try:
            self.cursor.execute("SELECT listname FROM list WHERE userid=?", (self.userid,))
            response = self.cursor.fetchall()
            lists = []
            for item in response:
                for z in item:
                    lists.append(z)
            return lists
        except:
            print("something went wrong")

    def Add_list(self, listnames):
        for name in listnames:
            try:
                self.cursor.execute("SELECT listname FROM list  where listname=? AND userid=?", (name,self.userid))
                response = self.cursor.fetchall()
                if len(response)>0:
                    raise Exception(f"{name} already exist")
                self.cursor.execute("INSERT INTO list (userid, listname) VALUES (?, ?)", (self.userid, name))
                self.db.commit()
                print(f"{name} added successfully")
            except Exception as e:
                print(f"{e}")

    def update_list(self, listname, newname):
        try:
            self.cursor.execute("SELECT listname FROM list  where listname=?AND userid=?", (newname,self.userid))
            response = self.cursor.fetchone()
            if response is not None:
                raise Exception(f"{listname} already exist")
            self.cursor.execute("UPDATE list SET listname =? WHERE listname=? AND userid=?", (newname, listname, self.userid))
            self.db.commit()
        except Exception as e:
            print(f"{e}")
            

    def remove_list(self, listnames):
        for x in listnames:
            try:
                self.cursor.execute("DELETE FROM list WHERE  userid=? AND listname=?", (self.userid, x))
                self.db.commit()
            except:
                print(f"something went wrong , {x} cannot be deleted")


class crudtask:
    def __init__(self,cursor, db, username, listname):
        self.userid = get_userID(username, cursor)
        self.listid = get_listid(cursor, self.userid, listname)
        self.cursor = cursor
        self.db=db

    def show_task(self):
        try:
            self.cursor.execute("SELECT taskname, status FROM task WHERE listid=?", (self.listid,))
            response = self.cursor.fetchall()
            lists = []
            for item in response:
                li=[]
                for z in item:
                    li.append(z)
                lists.append(li)
            return lists
        except:
            print("something went wrong")

    def Add_task(self, tasks):
        for task in tasks:
            try:
                self.cursor.execute("SELECT taskname FROM task  where listid=? AND taskname=?", (self.listid,task))
                response = self.cursor.fetchall()
                if len(response)>0:
                    raise Exception(f"{task} already exist")
                self.cursor.execute("INSERT INTO task (listid, taskname) VALUES (?, ?)", (self.listid, task))
                self.db.commit()
                print(f"{task} added successfully")
            except Exception as e:
                print(f"{e}")

    def update_task(self, taskname, newname):
        try:
            self.cursor.execute("SELECT taskname FROM task where listid=? AND taskname=?", (self.listid, newname))
            response = self.cursor.fetchone()
            if len(response)>0:
                raise Exception(f"{newname} already exist")
            self.cursor.execute("UPDATE task SET taskname =? WHERE listid=?  AND taskname=?", (newname, self.listid, taskname))
            self.db.commit()
        except Exception as e:
            print(f"{e}")
            
    def update_status(self, taskname, status):
        try:
            self.cursor.execute("SELECT taskname FROM task where listid=? AND taskname=?", (self.listid, taskname))
            response = self.cursor.fetchone()
            if len(response)==0:
                raise Exception(f"{taskname} does not exist")
            
            self.cursor.execute("UPDATE task SET status=? WHERE listid=?  AND taskname=?", (status, self.listid, taskname))
            self.db.commit()
        except Exception as e:
            print(f"{e}")

    def remove_task(self, tasks):
        for task in tasks:
            try:
                self.cursor.execute("DELETE FROM task WHERE listid=? AND taskname=?", ( self.listid, task ))
                self.db.commit()
            except:
                print(f"something went wrong, {task} cannot be deleted")

    


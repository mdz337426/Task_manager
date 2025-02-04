from tabulate import tabulate

def draw_table(cursor, table):
    try:
        cursor.execute("""
        SELECT user.username, list.listname, task.taskname, task.status 
        FROM user
        JOIN list ON user.userid = list.userid
        JOIN task ON list.listid = task.listid
        """)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        print(tabulate(rows, headers=columns, tablefmt="fancy_grid"))
    except:
        print("some error occured in printing the table")

def printlist(lst):
    print(tabulate([[value] for value in lst], headers=["List"], tablefmt='fancy_grid'))

def printtask(lst):
    print(tabulate([[value for value in z] for z in lst], headers=["task", "status"], tablefmt='fancy_grid'))




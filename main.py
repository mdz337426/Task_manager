import crud
import sys
import fmt
import manual
import model
import argparse
import subprocess
import sqlite3
import auth

# DB setup
db_name = "mydb.db"
db = sqlite3.connect(db_name)
cursor = db.cursor()

# Model Tune
model.model_setup(cursor,db)

# Argument Parser 
parser = argparse.ArgumentParser(description="Secure CLI Login")
parser.add_argument("command", choices=["signup", "login"], help="Choose to signup or login")
parser.add_argument("--username", required=True, help="Your username")
args = parser.parse_args()

# Auth setup
if args.command == "signup":
    auth.signup(args.username,cursor,db)
    print(f"\n✅ Signup successful! Welcome, {args.username}.")
elif args.command == "login":
    auth.login(args.username, cursor)
    print(f"\n✅ Login successful! Welcome back, {args.username}.!!!\n")

# crud operation setup
crudlist = crud.crud_list(args.username, cursor, db)


listname = None
crud_task = None

# REPL console
manual.welcome_msg(args.username)
while True:
    print(">>> ", end="")
    userInput = input().split()
    if len(userInput)==0:
        continue
    command = userInput[0]

    if command=="clear":
        subprocess.run(["clear"])
    elif command == "help":
        manual.Help_for_user()
    elif command == "Show_list":
        fmt.printlist(crudlist.show_list())
    elif command == "Add_list":
        crudlist.Add_list(userInput[1:])
    elif command == "Update_list":
        crudlist.update_list(userInput[1], userInput[2])
    elif command == "Remove_list":
        crudlist.remove_list(userInput[1:])
    elif command == "use":
        listname = userInput[1]
        crud_task = crud.crudtask(cursor, db, args.username, listname)
    elif command == "Show_task":
        if listname is None:
            print("please select the list first")
            continue
        lst = crud_task.show_task()
        fmt.printtask(lst)
    elif command == "Add_task":
        if listname is None:
            print("please select the list first")
            continue
        crud_task.Add_task(userInput[1:])
    elif command == "Update_task":
        if listname is None:
            print("please select the list first")
            continue
        crud_task.update_task(userInput[1], userInput[2])
    elif command == "Remove_task":
        if listname is None:
            print("please select the list first")
            continue
        crud_task.remove_task(userInput[1:])
    elif command == "Update_status":
        if listname is None:
            print("please select the list first")
            continue
        crud_task.update_status(userInput[1], userInput[2])
    elif command == 'exit':
        print("Byee..")
        break
    else:
        print(f"ERROR: {userInput[0]}: command not found")

db.close()
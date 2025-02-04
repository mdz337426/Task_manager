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
model.model_setup(cursor, db)

# Argument Parser 
parser = argparse.ArgumentParser(description="Secure CLI Login")
parser.add_argument("command", choices=["signup", "login"], help="Choose to signup or login")
parser.add_argument("--username", required=True, help="Your username")
argg = parser.parse_args()

# Auth setup
if argg.command == "signup":
    auth.signup(argg.username, cursor, db)
    print(f"\n✅ Signup successful! Welcome, {argg.username}.")
elif argg.command == "login":
    auth.login(argg.username, cursor)
    print(f"\n✅ Login successful! Welcome back, {argg.username}.!!!\n")

# crud operation setup
crudlist = crud.crud_list(argg.username, cursor, db)

listname = None
crud_task = None

# Command functions
def clear_screen(args):
    subprocess.run(["clear"])

def show_list(args):
    fmt.printlist(crudlist.show_list())

def add_list(args):
    crudlist.Add_list(args)

def update_list(args):
    crudlist.update_list(args[0], args[1])

def remove_list(args):
    crudlist.remove_list(args)

def use_list(args):
    global listname, crud_task
    listname = args[0]
    crud_task = crud.crudtask(cursor, db, argg.username, listname)

def show_task(args):
    if listname is None:
        print("please select the list first")
        return
    lst = crud_task.show_task()
    fmt.printtask(lst)

def add_task(args):
    if listname is None:
        print("please select the list first")
        return
    crud_task.Add_task(args)

def update_task(args):
    if listname is None:
        print("please select the list first")
        return
    crud_task.update_task(args[0], args[1])

def remove_task(args):
    if listname is None:
        print("please select the list first")
        return
    crud_task.remove_task(args)

def update_status(args):
    if listname is None:
        print("please select the list first")
        return
    crud_task.update_status(args[0], args[1])

def exit_app(args):
    print("Byee..")
    global running
    running = False

# Command map
commands = {
    "clear": clear_screen,
    "help": manual.Help_for_user,
    "Show_list": show_list,
    "Add_list": add_list,
    "Update_list": update_list,
    "Remove_list": remove_list,
    "use": use_list,
    "Show_task": show_task,
    "Add_task": add_task,
    "Update_task": update_task,
    "Remove_task": remove_task,
    "Update_status": update_status,
    "exit": exit_app
}

# REPL console
manual.welcome_msg(argg.username)
running = True
while running:
    print(">>> ", end="")
    userInput = input().split()
    if len(userInput) == 0:
        continue
    command = userInput[0]
    args = userInput[1:]

    if command in commands:
        commands[command](args)
    else:
        print(f"ERROR: {command}: command not found")

db.close()
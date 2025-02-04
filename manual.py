
def welcome_msg(username):
    print(f"""Welcome to the Task Manager. 
Server version: 1.0.0 
Task Manager is a Command line tool to manage tasks and other functionalities

Type 'help' for help. Type 'clear' to clear the current input console.
""")
    
def Help_for_user(args):
    print("""
    Commands:
    - Add_list <List names...>: Add one or more lists.
    - Show_list: Display all lists.
    - Update_list <Current name> <New name>: Update the name of a list.
    - Remove_list <List names...>: Remove one or more lists.
    - Use <List name>: Select a list to work with.
    - Add_task <Task names...>: Add one or more tasks to the selected list.
    - Show_task: Display all tasks in the selected list.
    - Update_task <Current name> <New name>: Update the name of a task.
    - Remove_task <Task names...>: Remove one or more tasks from the selected list.
    - exit: Exit the Task Manager.
    """) 


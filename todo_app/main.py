""" 1. In a new folder, todo_app, create the following modules to build a basic to-do list
application:
○ main.py: Handles user interaction with the app.
○ todo_operations.py: Contains functions to add, delete, and view tasks.
○ utils.py: Contains utility functions, like clearing the screen and reading user input.
2. Features to implement:
○ Display a menu for the user to:
■ Add a new to-do item.
■ View all to-do items.
■ Delete an item by its index.
○ Use if and while loops to keep the menu active until the user chooses to exit.
○ Test your app by adding a few items and deleting one.
 """

import todo_operations
import utils

tasks=[]
print("Welcome to Your Todo App")
print("________________________")

while True:
    print("1. Add Task \n2.Delete Task by index \n3.View Tasks \n4.Clear Screen \n5.Exit ")
    choice=input('Your Choice: ')
    match choice:
        case '1':
            new_task=input("Enter a new task: ")
            todo_operations.add_task(tasks,new_task)
        case '2':
            index=input("Enter the index of task to delete: ")
            todo_operations.delete_task(tasks,index)
        case '3':
                todo_operations.view_task(tasks)
        case '4':
            utils.clear_screen()
        case '5':
            print("Exiting the application")
            break
        case _:
            print("Invalid Choice, Please Try Again")

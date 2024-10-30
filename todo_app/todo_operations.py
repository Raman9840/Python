

def add_task(tasks,task):
    tasks.append(task)
    print(f"Task {task} added successfully")


def delete_task(tasks,index):
    try:
        index=int(index)
        if 0<=index < len(tasks):
            removed_task=tasks.pop(index)
            print(f"Task {removed_task} removed Successfully")
        else:
            print("Invalid index, Please enter valid index\n")
    except ValueError:
        print("Invalid input. Please enter valid value\n")
    
def view_task(tasks):
    if tasks:
        print("Your Tasks: ")
        for i,task in enumerate(tasks):
            print(f"{i}. {task}")
        print()
    else:
        print("No tasks to view\n")
    
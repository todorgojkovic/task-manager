import json
from pathlib import Path
from datetime import datetime

tasks_file = Path(__file__).parent / "tasks.json"

def load_tasks():
    try:
        with tasks_file.open("r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]

def save_tasks():
    with tasks_file.open("w") as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks()

def show_menu():
    print("\n-- TO DO LIST --")
    print("1. Add task")
    print("2. View task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Edit task")
    print("6. Search")
    print("7. Statistics")
    print("8. Exit")

def add_task():
    task = input("\nEnter a new task: ")

    print("\nChoose priority:")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    priority_choice = input("\nChoose priority(1-3): \n")

    if priority_choice == "1":
        priority = "Low"
    elif priority_choice == "2":
        priority = "Medium"
    elif priority_choice == "3":
        priority = "High"
    else:
        priority = "Medium"
        print("\nInvalid choice. Priority set to Medium.")

    created_at = datetime.now().strftime("%Y-%m-%d")

    tasks.append({"task" : task, "done": False, "priority" : priority, "created_at" : created_at})
    save_tasks()
    print(f"\nTask '{task}' added with {priority} priority!")

def view_task():
    if not tasks:
        print("\nNo tasks yet.")
        return
    
    print("\nYour Tasks:")

    for index, task in enumerate(tasks, start = 1):
        status = "Done" if task["done"] else "Not done"
        priority = task.get("priority", "Medium")
        created_at = task.get("created_at", "Unknown")

        print(f"{index}. {task['task']} [{status}] [Priority : {priority}] [Created: {created_at}]")

def mark_done():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("\nEnter the task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks()
            print("\nMark as done!")
        else:
            print("\nInvalid task number.")
    except ValueError:
        print("\nPlease enter a valid number.")

def delete_task():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("\nEnter the task number to delete:")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks()
            print(f"\nDelete task: {removed['task']}")
        else:
            print("\nInvalid number!")
    except ValueError:
        print("\nPlease enter a valid number.")

def edit_task():
    view_task()

    if not tasks:
        return

    try:
        index = int(input("Enter the task number to edit: ")) - 1

        if 0 <= index < len(tasks):
            current_task = tasks[index]["task"]
            print(f"\nCurrent task: {current_task}")
            new_task = input("\nEnter the new task name: ").strip()

            if not new_task:
                print("Task name cannot be empty.")
                return

            tasks[index]["task"] = new_task
            save_tasks()

            print(f"\nTask '{current_task}' changed to '{new_task}'!")
        else:
            print("\nInvalid task number.")

    except ValueError:
        print("\nPlease enter a valid number.")

def search_task():
    if not tasks:
        print("No tasks available.")
        return

    search = input("\nSearch: ").strip().lower()
    found = False

    for index, task in enumerate(tasks, start=1):
        if search in task["task"].lower():
            status = "Done" if task["done"] else "Not done"
            priority = task.get("priority", "Medium")
            created_at = task.get("created_at", "Unknown")

            print(f"\n{index}. {task['task']} [{status}] [Priority : {priority}] [Created : {created_at}]")

            found = True

    if not found:
        print("\nNo matching tasks found.")

def statistics():
    total = len(tasks)
    completed = 0

    for task in tasks:
        if task["done"]:
            completed += 1

    remaining = total - completed

    print("\n-----Statistics-----")
    print(f"Total tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Remaining: {remaining}")
    print("--------------------")

while True:
    show_menu()
    choice = input("Choose an option (1-8): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        edit_task()
    elif choice == "6":
        search_task()
    elif choice == "7":
        statistics()
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("\nInvalid choice. Try again.")
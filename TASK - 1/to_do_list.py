import json
from datetime import datetime

# Function to load existing tasks from a file
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    return tasks

# Function to save tasks to a file
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=2)

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['title']} - {task['due_date']}")

# Function to add a new task
def add_task(tasks, title, due_date):
    new_task = {'title': title, 'due_date': due_date}
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully.")

# Function to update the status of a task
def update_task_status(tasks, task_index, status):
    if 0 < task_index <= len(tasks):
        tasks[task_index - 1]['status'] = status
        save_tasks(tasks)
        print(f"Status of task '{tasks[task_index - 1]['title']}' updated to '{status}'.")
    else:
        print("Invalid task index.")

# Function to remove a task
def remove_task(tasks, task_index):
    if 0 < task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' removed successfully.")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\n==== To-Do List ====")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Update Task Status")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            title = input("Enter task title: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, title, due_date)
        elif choice == '3':
            display_tasks(tasks)
            task_index = int(input("Enter the task index to update status: "))
            status = input("Enter the new status (e.g., 'In Progress', 'Completed'): ")
            update_task_status(tasks, task_index, status)
        elif choice == '4':
            display_tasks(tasks)
            task_index = int(input("Enter the task index to remove: "))
            remove_task(tasks, task_index)
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

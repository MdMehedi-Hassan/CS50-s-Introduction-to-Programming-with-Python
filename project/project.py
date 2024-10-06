import json
from datetime import datetime

# Persistent file for tasks
TASKS_FILE = "tasks.json"

# Main function
def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            add_task(description, deadline)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            new_description = input("Enter new description: ")
            new_deadline = input("Enter new deadline (YYYY-MM-DD): ")
            update_task(task_id, new_description, new_deadline)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '5':
            task_id = int(input("Enter task ID to mark complete: "))
            mark_task_complete(task_id)
        elif choice == '6':
            save_tasks_to_file()
            break
        else:
            print("Invalid option. Please choose again.")

# Add a new task
def add_task(description, deadline):
    tasks = load_tasks_from_file()
    task_id = len(tasks) + 1
    tasks.append({
        "id": task_id,
        "description": description,
        "deadline": deadline,
        "completed": False
    })
    print(f"Task added successfully with ID {task_id}")
    save_tasks_to_file(tasks)

# View all tasks
def view_tasks():
    tasks = load_tasks_from_file()
    if tasks:
        for task in tasks:
            status = "Completed" if task["completed"] else "Incomplete"
            print(f"{task['id']}. {task['description']} (Deadline: {task['deadline']}) - {status}")
    else:
        print("No tasks available.")

# Update task details
def update_task(task_id, new_description, new_deadline):
    tasks = load_tasks_from_file()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['deadline'] = new_deadline
            print(f"Task {task_id} updated successfully.")
            save_tasks_to_file(tasks)
            return
    print(f"Task {task_id} not found.")

# Delete a task
def delete_task(task_id):
    tasks = load_tasks_from_file()
    tasks = [task for task in tasks if task['id'] != task_id]
    print(f"Task {task_id} deleted successfully.")
    save_tasks_to_file(tasks)

# Mark a task as complete
def mark_task_complete(task_id):
    tasks = load_tasks_from_file()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            print(f"Task {task_id} marked as complete.")
            save_tasks_to_file(tasks)
            return
    print(f"Task {task_id} not found.")

# Save tasks to a file
def save_tasks_to_file(tasks=None):
    if tasks is None:
        tasks = load_tasks_from_file()
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

# Load tasks from a file
def load_tasks_from_file():
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    main()

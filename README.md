# CS50-s-Introduction-to-Programming-with-Python
## Task Manager
# The Details Based on Project that have been done.
#### Description:

The **Task Manager** is a Python-based terminal application designed to help users efficiently manage their tasks. The program allows users to add tasks with descriptions and deadlines, view a list of their tasks, update task details, delete tasks, and mark tasks as complete. To ensure task data is not lost between sessions, the program uses a simple file-based persistence system by saving tasks to a JSON file.

This project was created as part of a final Python course assignment, showcasing the use of functions, file handling, and automated testing using `pytest`.

### Project Files

- **project.py**:  
  This is the main file containing the core logic of the task manager. It includes a series of functions to handle task operations such as adding, updating, deleting, and marking tasks as complete. Additionally, it handles loading and saving tasks from a file to provide persistence across sessions. The `main()` function serves as the entry point for the application, displaying a menu that allows users to perform these tasks.

    Key functions:
    - `main()`: Displays the menu and allows user interaction with the task manager.
    - `add_task(description, deadline)`: Adds a new task with a description and deadline.
    - `view_tasks()`: Displays a list of all tasks, along with their status.
    - `update_task(task_id, new_description, new_deadline)`: Updates the details of an existing task.
    - `delete_task(task_id)`: Deletes a task based on the provided task ID.
    - `mark_task_complete(task_id)`: Marks a task as complete.
    - `save_tasks_to_file()`: Saves the task list to a JSON file.
    - `load_tasks_from_file()`: Loads the task list from a JSON file.

- **test_project.py**:  
  This file contains unit tests for the key functions in `project.py`, implemented using `pytest`. The tests ensure that critical operations like adding tasks, deleting tasks, and marking tasks as complete work as expected.

    Key tests:
    - `test_add_task()`: Verifies that a task is correctly added to the list.
    - `test_delete_task()`: Ensures that a task is properly deleted.
    - `test_mark_task_complete()`: Confirms that a task can be marked as completed.

- **requirements.txt**:  
  Lists the external dependencies required by the project. In this case, it only includes `pytest`, which is used for running the tests.

### Design Decisions

Several design choices were made to keep the application simple and easy to use:

1. **JSON File Persistence**:  
   Tasks are stored in a JSON file to allow for persistent storage across multiple sessions. This format was chosen for its simplicity and human-readability, making it easy to load, modify, and save tasks without the need for a database.

2. **Command-Line Interface**:  
   The project was designed to run in a terminal-based environment for simplicity and to demonstrate proficiency in Python programming. A terminal-based menu system provides an intuitive way for users to interact with their tasks.

3. **Automated Testing**:  
   Testing is an integral part of software development. `pytest` was used to write unit tests for key functions, ensuring that they behave correctly under different conditions. This helps catch potential bugs and ensures the program remains stable as new features are added.

### Future Improvements

There are several enhancements that could be made to improve the project:
- **Task Prioritization**: Add the ability to assign priorities to tasks (e.g., High, Medium, Low).
- **Sorting**: Implement a sorting feature that allows users to sort tasks by deadline or priority.
- **Recurring Tasks**: Allow users to set recurring tasks that automatically regenerate at regular intervals.
- **Graphical User Interface (GUI)**: While the current version is terminal-based, a future version could include a GUI built with a library like `Tkinter` or `PyQt` for a more user-friendly experience.

### Conclusion

The **Task Manager** is a simple yet functional project that demonstrates key concepts of Python programming, including function design, file handling, and automated testing. It meets the course’s requirements and provides a foundation that can be expanded with additional features in the future.

import project
import pytest

def test_add_task():
    project.add_task("Test task", "2024-12-31")
    tasks = project.load_tasks_from_file()
    assert tasks[-1]['description'] == "Test task"
    assert tasks[-1]['deadline'] == "2024-12-31"
    assert tasks[-1]['completed'] == False

def test_delete_task():
    project.add_task("Task to delete", "2024-12-31")
    task_id = len(project.load_tasks_from_file())
    project.delete_task(task_id)
    tasks = project.load_tasks_from_file()
    assert all(task['id'] != task_id for task in tasks)

def test_mark_task_complete():
    project.add_task("Task to complete", "2024-12-31")
    task_id = len(project.load_tasks_from_file())
    project.mark_task_complete(task_id)
    tasks = project.load_tasks_from_file()
    assert tasks[task_id - 1]['completed'] == True


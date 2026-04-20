import pytest
import json
import os
from ..task_manager import Task, TaskManager

class TestTask:
    def test_task_creation(self):
        task = Task(1, "Test task")
        assert task.id == 1
        assert task.description == "Test task"
        assert task.completed == False

    def test_task_str_pending(self):
        task = Task(1, "Test task")
        assert str(task) == "[Pending] #1: Test task"

    def test_task_str_completed(self):
        task = Task(1, "Test task", True)
        assert str(task) == "[Completed] #1: Test task"

class TestTaskManager:
    def setup_method(self):
        # Use a temporary file for testing
        self.temp_file = "test_tasks.json"
        # Ensure no file exists
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

    def teardown_method(self):
        # Clean up
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

    def test_add_task(self):
        tm = TaskManager()
        tm.FILENAME = self.temp_file  # Override filename
        tm.load_tasks()  # Reload from temp file
        tm.add_task("New task")
        assert len(tm._tasks) == 1
        assert tm._tasks[0].description == "New task"
        assert tm._tasks[0].id == 1
        assert tm._next_id == 2

    def test_list_tasks_empty(self, capsys):
        tm = TaskManager()
        tm.FILENAME = self.temp_file
        tm.load_tasks()
        tm.list_tasks()
        captured = capsys.readouterr()
        assert "No pending tasks" in captured.out

    def test_list_tasks_with_tasks(self, capsys):
        tm = TaskManager()
        tm.FILENAME = self.temp_file
        tm.load_tasks()
        tm.add_task("Task 1")
        tm.add_task("Task 2")
        tm.list_tasks()
        captured = capsys.readouterr()
        assert "[Pending] #1: Task 1" in captured.out
        assert "[Pending] #2: Task 2" in captured.out

    def test_complete_task(self, capsys):
        tm = TaskManager()
        tm.FILENAME = self.temp_file
        tm.load_tasks()
        tm.add_task("Task to complete")
        tm.complete_task(1)
        captured = capsys.readouterr()
        assert "Completed task:" in captured.out
        assert tm._tasks[0].completed == True

    def test_complete_task_not_found(self, capsys):
        tm = TaskManager()
        tm.FILENAME = self.temp_file
        tm.load_tasks()
        tm.complete_task(99)
        captured = capsys.readouterr()
        assert "Task not found: #99" in captured.out

    def test_delete_task(self, capsys):
        tm = TaskManager()
        tm.FILENAME = self.temp_file
        tm.load_tasks()
        tm.add_task("Task to delete")
        tm.delete_task(1)
        captured = capsys.readouterr()
        assert "Task deleted: #1" in captured.out
        assert len(tm._tasks) == 0

    def test_delete_task_not_found(self, capsys):
        tm = TaskManager()
        tm.FILENAME = self.temp_file
        tm.load_tasks()
        tm.delete_task(99)
        captured = capsys.readouterr()
        assert "Task not found: #99" in captured.out

    def test_save_and_load_tasks(self):
        tm = TaskManager()
        tm.FILENAME = self.temp_file
        tm.load_tasks()
        tm.add_task("Task 1")
        tm.add_task("Task 2")
        tm.complete_task(1)
        tm.save_tasks()

        # Create new instance and load
        tm2 = TaskManager()
        tm2.FILENAME = self.temp_file
        tm2.load_tasks()

        assert len(tm2._tasks) == 2
        assert tm2._tasks[0].description == "Task 1"
        assert tm2._tasks[0].completed == True
        assert tm2._tasks[1].description == "Task 2"
        assert tm2._tasks[1].completed == False
        assert tm2._next_id == 3
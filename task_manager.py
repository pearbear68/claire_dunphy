import argparse
import json
from datetime import datetime

class Task:
    def __init__(self, description, deadline=None, category=None, completed=False, created_at=None):
        self.description = description
        self.deadline = deadline
        self.category = category
        self.completed = completed
        self.created_at = created_at



class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                tasks_data = json.load(file)
                self.tasks = [Task(description=task.get("description"),
                                deadline=task.get("deadline"),
                                category=task.get("category"),
                                completed=task.get("completed", False),
                                created_at=task.get("created_at")) for task in tasks_data]
                print("Tasks loaded successfully:", [task.description for task in self.tasks])
        except (json.JSONDecodeError, FileNotFoundError):
            self.tasks = []





    def save_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                tasks_data = json.load(file)

        # Update tasks_data with new task
            new_task = {
            "description": self.tasks[-1].description,
            "deadline": self.tasks[-1].deadline,
            "category": self.tasks[-1].category,
            "completed": self.tasks[-1].completed,
            "created_at": self.tasks[-1].created_at,
            }
            tasks_data.append(new_task)

            with open("tasks.json", "w") as file:
                json.dump(tasks_data, file, indent=2)
        except Exception as e:
            print(f"An error occurred while saving tasks: {e}")



    def add_task(self, description, deadline=None, category=None):
        existing_tasks = [task.description.lower() for task in self.tasks]
        if description.lower() not in existing_tasks:
            new_task = Task(description=description, deadline=deadline, category=category)
            self.tasks.append(new_task)
            print(f"Task added successfully: {new_task.description}")
            self.save_tasks()
            print("After adding:", [task.description for task in self.tasks])
        else:
            print(f"Task with description '{description}' already exists.")


    def remove_task(self, index):
        try:
            print("Before removal:", [task.description for task in self.tasks])
            removed_task = self.tasks.pop(index - 1)
            print(f"Task removed: {removed_task.description}")
            print("After removal:", [task.description for task in self.tasks])
            self.save_tasks()
        except IndexError:
            print("Invalid index. No task removed.")
            return


    def list_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"Debug: i={i}, task.description={task.description}")
                print(f"{i}. {task.description}")



    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            print(f"Task completed: {self.tasks[task_index].description}")
            self.save_tasks()
        else:
            print("Invalid task index.")



def main():
    task_manager = TaskManager()

    parser = argparse.ArgumentParser(description="Command Line Task Manager")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Add sub-parser for the "add" command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")
    add_parser.add_argument("--deadline", help="Task deadline (YYYY-MM-DD)")
    add_parser.add_argument("--category", help="Task category")

    # Add sub-parser for the "remove" command
    remove_parser = subparsers.add_parser("remove", help="Remove a task")
    remove_parser.add_argument("index", type=int, help="Index of the task to remove")

    # Add sub-parser for the "list" command
    subparsers.add_parser("list", help="List all tasks")

    # Add sub-parser for the "complete" command
    complete_parser = subparsers.add_parser("complete", help="Complete a task")
    complete_parser.add_argument("index", type=int, help="Index of the task to complete")

    args, _ = parser.parse_known_args()

    if args.command == "add":
        task_manager.add_task(args.description, args.deadline, args.category)
    elif args.command == "remove":
        task_manager.remove_task(args.index)
    elif args.command == "list":
        task_manager.list_tasks()
    elif args.command == "complete":
        task_manager.complete_task(args.index)

if __name__ == "__main__":
    main()





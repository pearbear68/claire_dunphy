# claire_dunphy
claire_dunphy is a lightweight, command line-based task manager built with Python. 

Features:
Add Tasks: Add tasks with descriptions, deadlines, and categories.
Remove Tasks: Remove tasks by specifying their index.
List Tasks: View a list of all tasks.
Complete Tasks: Mark tasks as completed to track your progress.

Requirements:
Python 3


Usage:

1. Add a Task

python task_manager.py add --description "Your task description" --deadline "YYYY-MM-DD" --category "Your category"
Replace the placeholders with your task details.

2. Remove a Task

python task_manager.py remove 1
Replace 1 with the index of the task you want to remove.

3. List Tasks

python task_manager.py list
This command lists all tasks.

4. Complete a Task

python task_manager.py complete 1
Replace 1 with the index of the task you want to mark as completed.


Setup:

Clone the repository:
git clone https://github.com/your-username/your-repository.git

Navigate to the project directory:
cd your-repository

Run the task manager:
python task_manager.py

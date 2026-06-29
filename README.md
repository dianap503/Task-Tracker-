# Task-Tracker

INSTRUCTIONS

1. Adding a new task
   python3 task_cli.py add "Your task description"

2. Updating and deleting tasks
   python3 task_cli.py update 1 "New task description" 
   python3 task_cli.py delete 1

3. Marking a task as in progress or done
   python3 task_cli.py mark-in-progress 1
   python3 task_cli.py mark-done 1

4. Listing all tasks
   python3 task_cli.py list

5. Listing tasks by status
   python3 task_cli.py list done
   python3 task_cli.py list in-progress

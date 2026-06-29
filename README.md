# Task Tracker CLI

A simple tool for managing your tasks directly from the terminal.

## Usage

| Action | Command |
| :--- | :--- |
| **Add** | `python3 task_cli.py add "Description"` |
| **Update** | `python3 task_cli.py update 1 "New description"` |
| **Delete** | `python3 task_cli.py delete 1` |
| **List all** | `python3 task_cli.py list` |

### Changing Status
* `python3 task_cli.py mark-in-progress 1`
* `python3 task_cli.py mark-done 1`

### Filtering
* `python3 task_cli.py list done`
* `python3 task_cli.py list in-progress`

import sys # sys.argv[0] title, sys.argv[1] command, sys.argv[2] description
import os # checking if the file exists
import json # handling the data formatting
import datetime

file_name = "tasks.json"

if not os.path.exists(file_name) :
    with open(file_name, 'w') as file :
        json.dump([], file) # dump takes an object (in this case []) and translates it into a JSON-formatted string of text

if len(sys.argv) <2 :
    print("Usage: python3 tak_cli.py <command> [arguments]")
    sys.exit(1) # the program closed due to an error
command = sys.argv[1]
if command == "add" :
    if len(sys.argv) <3 :
        print("Error: Please provide a task description")
    else :
        task_description = sys.argv[2]
        with open(file_name, 'r') as file:
            tasks = json.load(file) # converts the JSON text into a Python list
        now = datetime.datetime.now().isoformat()
        new_id = len(tasks) + 1
        new_task = {
            "id" : new_id ,
            "description" : task_description ,
            "status" : "todo" ,
            "createdAt" : now ,
            "updatedAt" : now
        }
        tasks.append(new_task) # adds new task to the current list 
        with open(file_name, 'w') as file : # when you open the json file into write mode, it deletes everything that the file contained before
            json.dump(tasks, file, indent=4) # converts the updated list back into a JSON format
        print(f"Task added successfully (ID: {new_id})")
elif command == "list" :
    with open(file_name, 'r') as file :
        tasks = json.load(file)
    if len(sys.argv) == 2 :
        for t in tasks:
            print(f"ID: {t['id']} | Task: {t['description']} | Status: {t['status']}")
    elif len(sys.argv) == 3 :
        filter = sys.argv[2]
        for t in tasks :
            if t["status"] == filter :
                print(f"ID: {t['id']} | Task: {t['description']} | Status: {t['status']}")
elif command == "update" :
    if len(sys.argv) == 2 :
        print("Error: Not given task ID!")
    elif len(sys.argv) == 3 :
        print("Error: No explicit description for the updated task!")
    elif len(sys.argv) == 4 :
        task_id = int(sys.argv[2])
        updated_description = sys.argv[3]
        with open(file_name, 'r') as file :
            tasks = json.load(file)
        now = datetime.datetime.now().isoformat()
        task_found = False
        for t in tasks :
            if t["id"] == task_id :
                t["description"] = updated_description
                t["updatedAt"] = now
                task_found = True
                break
        if not task_found:
            print(f"Error: Task with ID {task_id} not found!")
        else :
            with open(file_name, 'w') as file:
                json.dump(tasks, file, indent=4)
            print(f"Task {task_id} updated successfully!")
elif command == "mark-in-progress" :
    with open(file_name, 'r') as file:
        tasks = json.load(file)
    if len(sys.argv) < 3 :
        print("Error: Not given task ID!")
    elif len(sys.argv) == 3 :
        task_id = int(sys.argv[2])
        task_found = False
        now = datetime.datetime.now().isoformat()
        for t in tasks :
            if t["id"] == task_id :
                t["status"] = "in-progress"
                t["updatedAt"] = now
                task_found = True
                break
        if not task_found :
            print(f"Task {task_id} not found!")
        else :
            with open(file_name, 'w') as file :
                json.dump(tasks, file, indent=4)
            print(f"Task {task_id} marked in progress!")
elif command == "delete" :
    if len(sys.argv) == 2 :
        print("Error: Not given task ID!")
        sys.exit(1)
    elif len(sys.argv) == 3 :
        task_id = int(sys.argv[2])
        with open(file_name, 'r') as file:
            tasks = json.load(file)
        new_tasks = [t for t in tasks if t["id"] != task_id]
        if len(tasks) == len(new_tasks) :
            print(f"Task {task_id} not found!")
        else :
            with open(file_name, 'w') as file :
                json.dump(new_tasks, file, indent=4)
            print(f"Task {task_id} deleted successfully.")   
elif command == "mark-done" :
    with open(file_name, 'r') as file:
        tasks = json.load(file)
    if len(sys.argv) < 3 :
        print("Error: Not given task ID!")
    elif len(sys.argv) == 3 :
        task_id = int(sys.argv[2])
        task_found = False
        now = datetime.datetime.now().isoformat()
        for t in tasks :
            if t["id"] == task_id :
                t["status"] = "done"
                t["updatedAt"] = now
                task_found = True
                break
        if not task_found :
            print(f"Task {task_id} not found!")
        else :
            with open(file_name, 'w') as file :
                json.dump(tasks, file, indent=4)
            print(f"Task {task_id} marked done!")
else :          
    print(f"Unknown command {command}")

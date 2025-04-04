import sys
import json
import os
from datetime import datetime
FILE_NAME="tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME,"w") as f:
            json.dump([],f)
    with open(FILE_NAME,"r") as f:
        return json.load(f)
def save_tasks(tasks):
    with open(FILE_NAME,"w") as f:
        json.dump(tasks,f,indent=2)
def generate_id(tasks):
    return max([task["id"] for task in tasks],default=0)+1
def add_task(description):
    tasks=load_tasks()
    task={
        "id":generate_id(tasks),
        "description":description,
        "status":"todo",
        "createdAt":datetime.now().isoformat(),
        "updatedAt":datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")
def list_tasks(status=None):
    tasks=load_tasks()
    filtered=[task for task in tasks if status is None or task["status"]==status]
    if not filtered:
        print("No tasks found.")
    else:
        for task in filtered:
            print(f'{task["id"]}.{task["description"]} [{task["status"]}]')
def update_task(task_id,new_description):
    tasks=load_tasks()
    for task in tasks:
        if task["id"]==task_id:
            task["description"]=new_description
            task["updatedAt"]=datetime.now().isoformat()
            save_tasks(tasks)
            print("Task updated successfully.")
            return
    print("Task not found.")
def delete_task(task_id):
    tasks=load_tasks()
    new_tasks=[task for task in tasks if task["id"]!=task_id]
    if len(tasks)==len(new_tasks):
        print("Task not found.")
    else:
        save_tasks(new_tasks)
        print("Task deleted successfully.")
def mark_task(task_id,new_status):
    if new_status not in ["todo","in-progress","done"]:
        print("Invalid status. Use: todo, in-progress, or done.")
        return
    tasks=load_tasks()
    for task in tasks:
        if task["id"]==task_id:
            task["status"]=new_status
            task["updatedAt"]=datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task marked as {new_status}")
            return
    print("Task not found.")
def main():
    if len(sys.argv)<2:
        print("Please provide a command.")
        return
    command=sys.argv[1]
    if command=="add":
        description=" ".join(sys.argv[2:])
        if not description:
            print("Please provide a task description")
            return
        add_task(description)
    elif command=="list":
        if len(sys.argv)==2:
            list_tasks()
        else:
            status=sys.argv[2]
            list_tasks(status)
    elif command=="update":
        if len(sys.argv)<4:
            print("Usage: update <id> <new description>")
            return
        try:
            task_id=int(sys.argv[2])
        except ValueError:
            print("Invalid ID.")
            return
        new_description=" ".join(sys.argv[3:])
        update_task(task_id,new_description)

    elif command=="delete":
        if len(sys.argv) != 3:
            print("Usage: delete <id>")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Invalid ID.")
            return
        delete_task(task_id)

    elif command == "mark":
        if len(sys.argv) != 4:
            print("Usage: mark <id> <status>")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Invalid ID.")
            return
        new_status = sys.argv[3]
        mark_task(task_id, new_status)

    else:
        print("Unknown command.")


if __name__ == "__main__":
    main()

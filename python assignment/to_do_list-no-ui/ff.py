# to-do-functions

task_list = []
p = "pending"

c = "completed"

def add_task(id, task, status = 'pending'):
    task_list.append({"id": id, "task": task, "status": status})

def view_tasks():
    for task in task_list:
        print(f"ID: {task['id']}, Task: {task['task']}, Status: {task['status']}")
    if not task_list:
        print("No tasks available.")   

def update_task(id, new_task, new_status):
    for task in task_list:
        if task['id'] == id:
            task['task'] = new_task
            if new_status.lower() == 'p':
             task['status'] = p
            elif new_status.lower() == 'c':
             task['status'] = c
            return True
        else:
            print(f"Task with ID {id} not found.")
    return False        

def complete_task(id):
    for task in task_list:
        if task['id'] == id:
            task['status'] = 'completed'
            return True
    return False

def delete_task(id):
    for task in task_list:
        if task['id'] == id:
            task_list.remove(task)
            print(f"Task with ID {id} has been deleted.")
            return True
    return False
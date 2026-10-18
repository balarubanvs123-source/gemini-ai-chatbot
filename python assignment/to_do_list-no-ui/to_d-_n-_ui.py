import ff
# import random as rand
from itertools import count



id_gen = count(1)
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        id = int(next(id_gen))  # Generate a sequential ID for the task
        task = input("Enter task description: ")
        ff.add_task(id, task)
        print("Task added successfully.")

    elif choice == '2':
        ff.view_tasks()

    elif choice == '3':
        id = int(input("Enter task ID to update: "))
        new_task = input("Enter new task description: ")
        new_status = input("Enter new status (type p for pending or c for completed): ")
        if new_status.lower() == 'p' or new_status.lower() == 'c':
           
         if ff.update_task(id, new_task, new_status):
            print("Task updated successfully.")
         else:
            print("Task not found.")
        else:
            print("Invalid status. Please enter 'p' for pending or 'c' for completed.") 

    elif choice == '4':
        id = int(input("Enter task ID to mark as completed: "))
        if ff.complete_task(id):
            print("Task marked as completed.")
        else:
            print("Task not found.")

    elif choice == '5':
        id = int(input("Enter task ID to delete: "))
        if ff.delete_task(id):
            print("Task deleted successfully.")
        else:
            print("Task not found.")

    elif choice == '6':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
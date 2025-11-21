from database import engine, metadata_obj
from crud import create_task, get_tasks, delete_task, update_task, change_task_status

metadata_obj.create_all(engine)

def menu():
    print("\n--- TODO App ---")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Change Task Status")
    print("6. Exit")

while True:
    menu()
    choice = input("Select an option: ")

    if choice == "1":
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        task_id = create_task(title, description)
        print("Created task ID:", task_id)

    elif choice == "2":
        tasks = get_tasks()
        print("All tasks:")
        for task in tasks:
            print(task)

    elif choice == "3":
        task_id = int(input("Enter task ID to update: "))
        title = input("Enter new title (leave blank to skip): ")
        description = input("Enter new description (leave blank to skip): ")
        updated = update_task(task_id, title=title if title else None, description=description if description else None)
        print("Updated rows:", updated)

    elif choice == "4":
        task_id = int(input("Enter task ID to delete: "))
        deleted = delete_task(task_id)
        print("Deleted rows:", deleted)

    elif choice == "5":
        task_id = int(input("Enter task ID to change status: "))
        status_changed = change_task_status(task_id)
        print("Status changed:", status_changed)

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid option. Try again.")

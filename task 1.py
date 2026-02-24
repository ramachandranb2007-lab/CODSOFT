def show_menu():
    print("\n====== MY TASK MANAGER ======")
    print("A - Add New Task")
    print("V - View All Tasks")
    print("R - Remove a Task")
    print("Q - Quit Program")


def add_task(task_list):
    new_task = input("Type your task: ").strip()
    if new_task:
        task_list.append(new_task)
        print("✔ Task saved!")
    else:
        print("Empty task not allowed.")


def view_tasks(task_list):
    if len(task_list) == 0:
        print("No tasks added yet.")
    else:
        print("\n--- Current Tasks ---")
        count = 1
        for item in task_list:
            print(f"{count}. {item}")
            count += 1


def remove_task(task_list):
    if not task_list:
        print("Task list is empty.")
        return

    view_tasks(task_list)
    choice = input("Enter task number to remove: ")

    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(task_list):
            deleted_task = task_list.pop(index)
            print(f"Removed: {deleted_task}")
        else:
            print("Invalid number.")
    else:
        print("Please enter a valid number.")


tasks_data = []

while True:
    show_menu()
    user_option = input("Choose an option: ").upper()

    if user_option == "A":
        add_task(tasks_data)

    elif user_option == "V":
        view_tasks(tasks_data)

    elif user_option == "R":
        remove_task(tasks_data)

    elif user_option == "Q":
        print("Closing Task Manager... Bye!")
        break

    else:
        print("Invalid option. Try again.")

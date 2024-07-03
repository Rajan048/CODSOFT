# To-Do List Application

def display_menu():
    print("\nTo-Do List Menu")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_todo_list(todo_list):
    if len(todo_list) == 0:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def add_task(todo_list):
    task = input("\nEnter a new task: ")
    todo_list.append(task)
    print(f"Task '{task}' has been added.")

def remove_task(todo_list):
    if len(todo_list) == 0:
        print("\nYour to-do list is empty. No tasks to remove.")
    else:
        view_todo_list(todo_list)
        try:
            task_num = int(input("\nEnter the number of the task to remove: "))
            if 1 <= task_num <= len(todo_list):
                removed_task = todo_list.pop(task_num - 1)
                print(f"Task '{removed_task}' has been removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")
        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            remove_task(todo_list)
        elif choice == '4':
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()

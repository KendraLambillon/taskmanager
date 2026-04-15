from task_manager import TaskManager

def print_menu():
    print("\n--- Smart Task Manager ---")
    print("1. Add task")
    print("2. List task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

def main():

    manager = TaskManager()

    while True:

        print_menu()

        try:

            choice = int(input("Enter your choice: "))

            match choice:
                case 1:
                    description = input("Enter task description: ")
                    manager.add_task(description)
                case 2:
                    manager.list_tasks()
                case 3:
                    id = int(input("Enter the ID of the task to complete: "))
                    manager.complete_task(id)
                case 4:
                    id = int(input("Enter the ID of the task to delete: "))
                    manager.delete_task(id)
                case 5:
                    print("Exiting...")
                    break
                case _:
                    print("Invalid choice. Please select another one.")

        except ValueError:
            print("Invalid choice. Please select another one.")
    
if __name__ == "__main__":
    main()
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

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                description = input("Enter task description: ")
                manager.add_task(description)
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")
    
if __name__ == "__main__":
    main()
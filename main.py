from task_manager import TaskManager
from ai_service import create_simple_tasks

def print_menu():
    print("\n--- Smart Task Manager ---")
    print("1. Add task")
    print("2. Add complex task (with AI)")
    print("3. List task")
    print("4. Complete task")
    print("5. Delete task")
    print("6. Exit")

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
                    description = input("Enter complex task description: ")
                    subtasks = create_simple_tasks(description)
                    for subtask in subtasks:
                        if not subtask.startswith("Error"):
                            manager.add_task(subtask)
                        else:
                            print(subtask)
                            break
                case 3:
                    manager.list_tasks()
                case 4:
                    id = int(input("Enter the ID of the task to complete: "))
                    manager.complete_task(id)
                case 5:
                    id = int(input("Enter the ID of the task to delete: "))
                    manager.delete_task(id)
                case 6:
                    print("Exiting...")
                    break
                case _:
                    print("Invalid choice. Please select another one.")
        except ValueError:
            print("Invalid choice. Please select another one.")
    
if __name__ == "__main__":
    main()
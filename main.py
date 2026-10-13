tasks = []


def show_tasks():
    if not tasks:
        print("\nNo tasks added yet.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def main():
    while True:
        print("\n-- Student Task Manager --")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            task = input("Enter the task: ").strip()
            if task:
                tasks.append(task)
                print("Task added successfully.")
            else:
                print("Task cannot be empty.")

        elif choice == '2':
            show_tasks()

        elif choice == '3':
            if not tasks:
                print("\nNo tasks added yet.")
                continue

            try:
                number = int(input("Enter the task number to delete: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f"Deleted task: {removed}")
            else:
                print("Invalid task number.")

        elif choice == '4':
            print("Thank you for using the Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
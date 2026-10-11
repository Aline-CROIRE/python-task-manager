
from task_manager import (
    add_task,
    view_tasks,
    mark_task_completed,
    delete_task,
)

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)


def display_tasks(tasks: list[dict[str, str | bool]]) -> None:
    """Display all tasks and their completion status."""
    current_tasks = view_tasks(tasks)

    if not current_tasks:
        print("\nNo tasks found.")
        return

    print("\n  YOUR TASKS    ")

    for index, task in enumerate(current_tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"

        print(f"\nTask {index}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Status: {status}")

    


def main() -> None:
    """Run the Python Personal Task Manager."""
    tasks: list[dict[str, str | bool]] = []

    print("  PYTHON PERSONAL TASK MANAGER")
    

    while True:
        print("\nChoose an option:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as completed")
        print("4. Exit")
        print("5. Delete a task")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")

            if add_task(tasks, title, description):
                print("\nTask added successfully!")
            else:
                print("\nTitle and description cannot be empty.")

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            if not tasks:
                print("\nNo tasks available to complete.")
                continue

            display_tasks(tasks)

            task_input = input(
                "\nEnter the task number to complete: "
            ).strip()

            try:
                task_number = int(task_input)
            except ValueError:
                print("\nPlease enter a valid whole number.")
                continue

            if mark_task_completed(tasks, task_number):
                print("\nTask marked as completed!")
            else:
                print("\nInvalid task number. Please try again.")

        elif choice == "4":
            print("\nThank you for using the Task Manager. Goodbye!")
            break

        elif choice == "5":
            if not tasks:
                print("\nNo tasks available to delete.")
                continue

            display_tasks(tasks)

            task_input = input(
                "\nEnter the task number to delete: "
            ).strip()

            try:
                task_number = int(task_input)
            except ValueError:
                print("\nPlease enter a valid whole number.")
                continue

            if delete_task(tasks, task_number):
                print("\nTask deleted successfully!")
            else:
                print("\nInvalid task number. Please try again.")

        else:
            print(
                "\nInvalid choice. Please select an option from 1 to 5."
            )


if __name__ == "__main__":
    main()


from task_manager import add_task, view_tasks


def main():
    tasks = []


    print("     PYTHON PERSONAL TASK MANAGER")


    title = input("Enter task title: ")
    description = input("Enter task description: ")

    if add_task(tasks, title, description):
        print("\nTask added successfully!")
    else:
        print("\nTitle and description cannot be empty.")

    print("\nCurrent tasks:")

    current_tasks = view_tasks(tasks)

    if not current_tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(current_tasks, start=1):
            print(f"\nTask {index}")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")


if __name__ == "__main__":
    main()

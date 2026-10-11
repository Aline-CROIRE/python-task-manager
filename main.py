
from task_manager import add_task


def main():
    tasks = []


    print("     PYTHON PERSONAL TASK MANAGER   ")
    

    title = input("Enter task title: ")
    description = input("Enter task description: ")

    if add_task(tasks, title, description):
        print("\nTask added successfully!")
    else:
        print("\nTitle and description cannot be empty.")

    print("\nCurrent tasks:")

    for task in tasks:
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")


if __name__ == "__main__":
    main()

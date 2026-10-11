import logging

logger = logging.getLogger(__name__)


def add_task(
    tasks: list[dict[str, str | bool]],
    title: str,
    description: str
) -> bool:
    """Add a task if its title and description are not empty."""
    title = title.strip()
    description = description.strip()

    if not title or not description:
        return False

    task = {
        "title": title,
        "description": description,
        "completed": False
    }

    tasks.append(task)
    logger.info("Task added successfully: %s", title)
    return True



def view_tasks(
    tasks: list[dict[str, str | bool]]
) -> list[dict[str, str | bool]]:
    """Return all tasks."""
    return tasks


def mark_task_completed(
    tasks: list[dict[str, str | bool]],
    task_number: int
) -> bool:
    """Mark a task as completed using its one-based position."""
    if task_number < 1 or task_number > len(tasks):
        return False

    tasks[task_number - 1]["completed"] = True
    logger.info(
    "Task marked as completed: %s",
    tasks[task_number - 1]["title"],
)
    return True



def delete_task(
    tasks: list[dict[str, str | bool]],
    task_number: int
) -> bool:
    """Delete a task using its one-based position."""
    if task_number < 1 or task_number > len(tasks):
        return False
    
    logger.info(
    "Task deleted: %s",
    tasks[task_number - 1]["title"],
)

    tasks.pop(task_number - 1)
    return True


def health_check() -> bool:
    """Check that the task manager's core functions are available."""
    return all(
        callable(function)
        for function in (
            add_task,
            view_tasks,
            mark_task_completed,
            delete_task,
        )
    )
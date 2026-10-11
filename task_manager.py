
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
    return True

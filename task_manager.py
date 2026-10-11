
def add_task(
    tasks: list[dict[str, str]],
    title: str,
    description: str
) -> bool:
    """Add a task if its title and description are valid."""
    title = title.strip()
    description = description.strip()

    if not title or not description:
        return False

    task = {
        "title": title,
        "description": description
    }

    tasks.append(task)
    return True


def view_tasks(tasks: list[dict[str, str]]) -> list[dict[str, str]]:
    """Return all tasks for display."""
    return tasks


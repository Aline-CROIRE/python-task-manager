
from task_manager import add_task, view_tasks


def test_add_task_with_valid_title_and_description():
    tasks = []

    result = add_task(
        tasks,
        "Study Python",
        "Practice functions and type hints"
    )

    assert result is True
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Study Python"
    assert tasks[0]["description"] == "Practice functions and type hints"


def test_add_task_rejects_empty_title():
    tasks = []

    result = add_task(tasks, "", "Study Python functions")

    assert result is False
    assert tasks == []


def test_add_task_rejects_empty_description():
    tasks = []

    result = add_task(tasks, "Study Python", "   ")

    assert result is False
    assert tasks == []


def test_view_tasks_returns_existing_tasks():
    tasks = [
        {
            "title": "Study Python",
            "description": "Practice functions"
        }
    ]

    result = view_tasks(tasks)

    assert result == tasks

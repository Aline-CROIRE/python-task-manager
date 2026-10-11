# Python Personal Task Manager

A simple Python command-line task manager built as an individual Agile &
DevOps Practices assessment. The project demonstrates incremental
delivery, automated tests, Git version control, and continuous
integration with GitHub Actions.

## Features

-   Add tasks with a title and description.
-   View tasks and their completion status.
-   Mark tasks as completed.
-   Delete tasks.
-   Validate blank fields, menu choices, and task numbers.
-   Log important task-management events.
-   Run a basic internal health check.

## Requirements

-   Python 3.10 or newer recommended
-   Git (optional, for cloning the repository)
-   `pytest` to run the automated tests

## Getting started

Clone the repository and enter the project directory:

``` bash
git clone https://github.com/Aline-CROIRE/python-task-manager.git
cd python-task-manager
```

Run the application:

``` bash
python main.py
```

## Run the tests

Install pytest if it is not already installed:

``` bash
python -m pip install pytest
```

Run the test suite:

``` bash
python -m pytest -v
```

The test suite covers core task-management behavior and the basic health
check.

## Continuous integration

The GitHub Actions workflow is located at `.github/workflows/tests.yml`.
It automatically runs the tests on configured repository events.

View workflow runs:
<https://github.com/Aline-CROIRE/python-task-manager/actions>

## Project structure

``` text
python-task-manager/
├── .github/
│   └── workflows/
│       └── tests.yml
├── docs/
│   ├── product-planning.md
│   ├── product-backlog.md
│   ├── sprint-1-plan.md
│   ├── sprint-1-review-retrospective.md
│   ├── sprint-2-plan.md
│   └── sprint-2-review-retrospective.md
├── tests/
│   ├── test_health.py
│   └── test_task_manager.py
├── main.py
└── task_manager.py
```

## Agile documentation

The `docs/` directory contains the product vision, prioritized backlog,
Definition of Done, sprint plans, and sprint review/retrospective
documents.

## Known limitation and future work

Tasks are stored in memory and are lost when the application exits. A
planned improvement is to add local JSON persistence so tasks can be
saved and restored between sessions.

## Repository

<https://github.com/Aline-CROIRE/python-task-manager>

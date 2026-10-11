# Sprint 1 Review and Retrospective

## 1. Sprint Goal

Deliver the first usable version of the Python Personal Task Manager, allowing users to add tasks and view their task list.

## 2. Sprint Review

### Delivered Product Backlog Items

| Item | Expected Outcome | Evidence |
|---|---|---|
| US1 — Add a Task | Users can add tasks with a title and description. Empty fields are rejected. | `main.py`, `task_manager.py`, automated tests |
| US2 — View Tasks | Users can view task titles and descriptions. An empty list displays a helpful message. | `main.py`, `task_manager.py`, automated tests |

### Quality and DevOps Evidence

- Automated tests are written with pytest.
- GitHub Actions is configured to run tests on pushes to `main` and pull requests targeting `main`.
- Git records incremental development through commits.
- Product planning and sprint documents are maintained in `docs/`.

**CI result:** Record the actual result from the latest GitHub Actions run.

**Test result:** Record the actual number of passing and failing tests.

### Review Outcome

The application provides an initial foundation for managing tasks. Tasks are currently held in memory, and the application does not yet support completing or deleting tasks.

## 3. Sprint Retrospective

### What Went Well?

- The product vision and backlog were documented before implementation.
- Development was divided into small changes.
- Task creation and viewing logic were separated from the application entry point.
- Automated tests and a CI workflow were introduced.

### What Was Difficult?

- Defining task requirements clearly before implementation.
- Understanding how automated tests verify behavior.

### Improvements for Sprint 2

1. **Improve usability:** introduce a repeating menu so users can perform multiple operations without restarting the application.
2. **Improve test coverage:** add tests for task completion, deletion, invalid selections, and edge cases as these features are implemented.
3. **Improve maintainability:** keep task operations in reusable functions and avoid duplicating business logic.
4. **Plan for persistence:** save tasks locally so they remain available after the application restarts.

## 4. Sprint 2 Follow-up

Sprint 2 will focus on marking tasks as complete and deleting tasks. We will also apply the retrospective improvements where appropriate and continue using automated tests and CI.

## 5. Personal Reflection

Complete after reviewing the sprint:

- **The most important thing I learned was:** How to apply Agile principles by breaking a project into small user stories, organizing work into sprints, and using Git, automated testing, and GitHub Actions to improve software quality.

- **The biggest challenge I faced was:** Understanding how to structure the application properly, validate user input, write automated tests, and connect the development process with Git and CI.

- **One thing I would do differently next time is:** Define the requirements and acceptance criteria more clearly before coding, write tests earlier, and plan smaller tasks to make development and debugging easier.
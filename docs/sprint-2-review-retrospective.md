# Sprint 2 Review and Retrospective

## 1. Sprint Overview

**Project:** Python Personal Task Manager

**Sprint:** Sprint 2

**Sprint Goal:** Extend the task manager by implementing task completion and deletion, improving input validation, introducing application logging and a health check, and strengthening automated testing and continuous integration.

**Development Approach:** Incremental development using Python, Git, automated tests, and GitHub Actions.

## 2. Sprint Review

### 2.1 Features Implemented

The following features were implemented and saved during Sprint 2.

#### 1. Interactive Task Management Menu

The application provides a command-line menu that allows users to:

- Add a task.
- View all tasks.
- Mark a task as completed.
- Exit the application.
- Delete a task.

The menu allows users to perform multiple operations during a single application session.

#### 2. Add Tasks

Users can add tasks by entering a title and description.

The application validates the input and rejects tasks with empty titles or descriptions. Valid tasks are added with an initial status of Pending.

#### 3. View Tasks

Users can display all tasks and view their titles, descriptions, and completion statuses.

Each task is assigned a number to make it easier to select for completion or deletion.

#### 4. Mark Tasks as Completed

Users can select a task by its number and mark it as completed.

The application validates the selected task number and updates the task status from Pending to Completed.

#### 5. Delete Tasks

Users can select a task by its number and remove it from the task list.

The application checks that the selected number is valid before deleting the task.

#### 6. Input Validation

The application includes validation for:

- Empty task titles and descriptions.
- Invalid menu choices.
- Non-numeric task numbers.
- Task numbers outside the valid range.
- Attempts to complete or delete tasks when the task list is empty.

These checks help prevent invalid operations from interrupting the application.

#### 7. Application Logging

Python's built-in logging module was introduced to record important task-management events, including successful task additions, completions, and deletions.

Logging supports debugging by providing information about application activity.

#### 8. Basic Health Check

A health-check function was added to verify that the core task-management functions are callable.

This is a basic internal check rather than a full system monitoring endpoint.

#### 9. Automated Testing

Automated tests were prepared for task-management operations and the health check.

The test suite is intended to verify expected behavior, including valid operations and invalid task numbers.

#### 10. Continuous Integration

A GitHub Actions workflow was prepared in `.github/workflows/tests.yml` to run automated tests.

This supports the DevOps practice of automatically checking code changes for regressions.

### 2.2 Sprint Review Demonstration

The following steps demonstrate the application's functionality:

1. Start the application using `python main.py`.
2. Add a task with a title and description.
3. View the task and confirm that its status is Pending.
4. Mark the task as completed.
5. View the task again and confirm that its status is Completed.
6. Add another task and delete it using its task number.
7. Enter an invalid menu choice and an invalid task number.
8. Attempt an operation when there are no tasks.
9. Run the automated tests using `python -m pytest -v`.
10. Demonstrate application log messages and the health-check test.
11. Open GitHub Actions and review the latest workflow result.
12. Review the Git commit history to demonstrate incremental development.

### 2.3 Testing Results

**Automated Testing**

Test files were saved for task-management operations and the health check. The final test outcome should be recorded after executing:

```powershell
python -m pytest -v
```

**Continuous Integration**

The GitHub Actions workflow file was saved. Its latest execution should be checked in the repository's Actions tab to confirm whether the workflow passed.

**Manual Testing**

The application code was saved with the interactive menu, task completion, deletion, and input validation. The demonstration steps above should be used to verify the behavior of each feature.

**Known Limitations**

- Tasks are stored in memory and disappear when the application exits.
- The health check verifies the availability of core functions but does not test every aspect of the application.
- Automated test and CI success must be established by reviewing their actual results.

## 3. Sprint Retrospective

### 3.1 What Went Well?

- The application was developed incrementally by adding features to an existing project.
- Task-management logic was separated from the command-line interface.
- Functions were used to make operations reusable and easier to maintain.
- Automated tests were prepared to check important behavior.
- Git was used to manage the project's development history.
- GitHub Actions was introduced to support continuous integration.
- The project provided practical experience with user stories, sprint goals, testing, and DevOps practices.

### 3.2 What Could Be Improved?

- Automated tests should be written and run alongside each feature.
- Test results should be checked before declaring a feature complete.
- GitHub Actions should be verified after every important push.
- Acceptance criteria should be reviewed before marking user stories as completed.
- Manual testing should cover both valid operations and edge cases.
- The application should support persistent storage so tasks remain available after restarting it.
- Documentation and implementation evidence should be maintained throughout each sprint.

### 3.3 Action Items for the Next Sprint

1. Implement persistent storage so tasks remain available after application restarts.
2. Expand automated test coverage to include additional edge cases and invalid input.
3. Confirm that the GitHub Actions workflow passes consistently.
4. Review code quality, type hints, documentation, and error handling.
5. Continue making small, meaningful Git commits.
6. Verify acceptance criteria and record evidence before declaring user stories complete.

## 4. Sprint Outcome

### 4.1 Completed Stories and Implemented Features

The following features were implemented and saved:

- Interactive command-line task-management menu.
- Adding tasks with titles and descriptions.
- Viewing tasks and their statuses.
- Marking tasks as completed.
- Deleting tasks by task number.
- Input validation for empty values and invalid choices or task numbers.
- Application logging for task operations.
- Basic health-check function.
- Automated test files for task management and the health check.
- GitHub Actions workflow for automated testing.

These items describe the implementation work. Successful test execution and CI results must be confirmed separately.

### 4.2 Incomplete or Unverified Work

The following items remain incomplete or require final verification:

- Confirm that the full automated test suite passes.
- Confirm that the latest GitHub Actions workflow succeeds.
- Complete and record the manual demonstration.
- Verify the final Git commit history and repository contents.
- Implement persistent storage so tasks survive application restarts.

### 4.3 Evidence

**GitHub Repository**

[Python Personal Task Manager](https://github.com/Aline-CROIRE/python-task-manager)

**Commit History**

[View repository commits](https://github.com/Aline-CROIRE/python-task-manager/commits/main/)

**Continuous Integration**

[View GitHub Actions workflow runs](https://github.com/Aline-CROIRE/python-task-manager/actions)

**Project Files**

| File | Purpose |
|---|---|
| `main.py` | Command-line interface and interactive menu |
| `task_manager.py` | Task-management logic, logging, and health check |
| `tests/test_task_manager.py` | Task-management automated tests |
| `tests/test_health.py` | Health-check test |
| `.github/workflows/tests.yml` | GitHub Actions workflow |
| `docs/sprint-2-plan.md` | Sprint 2 plan |
| `docs/sprint-2-review-retrospective.md` | Sprint 2 review and retrospective |

**Pull Requests:** No pull request is claimed as evidence because one has not been confirmed.

The repository links identify where the evidence can be reviewed. Confirm that the files are present in the remote repository and that the latest CI run succeeded before submission.

## 5. Final Reflection

Sprint 2 provided practical experience in improving a Python application through incremental development. Implementing task completion and deletion strengthened understanding of functions, list operations, input validation, and separation of concerns.

Preparing automated tests and a GitHub Actions workflow introduced important software quality and DevOps practices. Logging and the basic health check also demonstrated how developers can make application behavior easier to inspect.

The project still has opportunities for improvement, particularly persistent storage, broader test coverage, and final verification of continuous integration. Addressing these areas will improve reliability and maintainability.

Overall, the sprint helped connect Agile planning and retrospective practices with practical software development, testing, version control, and continuous integration.

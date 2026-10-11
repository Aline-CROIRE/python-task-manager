# Sprint 2 Plan

## Sprint Goal

Improve the Python Personal Task Manager by allowing users to complete and delete tasks while improving usability, testing, and application reliability.

## Selected Product Backlog Items

| ID | User Story | Estimate |
|---|---|---:|
| US3 | Mark a Task as Complete | 2 story points |
| US4 | Delete a Task | 2 story points |
| **Total** | | **4 story points** |

## Improvements Carried Forward from Sprint 1

1. Improve usability by introducing a repeating menu so users can perform multiple operations without restarting the application.
2. Expand automated test coverage for new features and invalid input.
3. Keep task-management logic in reusable functions.
4. Plan for local JSON persistence and basic application logging.

## Sprint Scope

### Included
- Add a completion status to each task.
- Implement marking a task as complete.
- Implement deleting a task.
- Introduce a repeating command-line menu.
- Write automated tests for the new features.
- Keep GitHub Actions running tests automatically.
- Add basic logging and a simple application status check.
- Implement local JSON persistence if capacity permits.

### Acceptance Conditions

- Users can mark an existing task as complete.
- Users can delete an existing task.
- Invalid task selections are handled gracefully.
- The menu allows users to perform multiple operations until they choose to exit.
- Automated tests pass.
- GitHub Actions runs the test suite.
- Basic logging and an application status check are available.
- Tasks are saved locally if persistence is implemented during this sprint.

## Sprint Review Plan

Demonstrate creating, viewing, completing, and deleting tasks. Show automated test results, the GitHub Actions workflow, and any implemented persistence and logging.

## Sprint Retrospective Plan

At the end of Sprint 2, reflect on the improvements made since Sprint 1, identify remaining limitations, and record at least two practical improvements for future work.
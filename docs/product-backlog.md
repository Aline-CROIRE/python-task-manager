# Product Backlog

## Prioritization and Estimation

Priority indicates the order in which features should be developed. Story points represent relative effort and complexity, not hours.

We use a simple scale of 1, 2, 3, and 5 points.

## User Stories

### US1 — Add a Task
**Priority:** High  
**Estimate:** 2 story points

As a user, I want to add a task so that I can remember activities I need to complete.

**Acceptance Criteria**
- The user can enter a task description.
- A valid task is added to the task list.
- Empty task descriptions are rejected with a helpful message.

### US2 — View Tasks
**Priority:** High  
**Estimate:** 1 story point

As a user, I want to view my tasks so that I can see what I need to do.

**Acceptance Criteria**
- The application displays all existing tasks.
- Each task shows its description and completion status.
- A helpful message appears when there are no tasks.

### US3 — Mark a Task as Complete
**Priority:** High  
**Estimate:** 2 story points

As a user, I want to mark a task as complete so that I can track my progress.

**Acceptance Criteria**
- The user can select an existing task.
- Its completion status changes to completed.
- Invalid task selections are handled gracefully.

### US4 — Delete a Task
**Priority:** Medium  
**Estimate:** 2 story points

As a user, I want to delete a task so that I can remove activities I no longer need.

**Acceptance Criteria**
- The user can select an existing task to delete.
- The selected task is removed from the list.
- Invalid selections produce a helpful message.

### US5 — Save Tasks Between Sessions
**Priority:** Medium  
**Estimate:** 3 story points

As a user, I want my tasks to be saved so that I can access them after restarting the application.

**Acceptance Criteria**
- Tasks are saved locally in a JSON file.
- Saved tasks are loaded when the application starts.
- Missing or invalid saved data is handled safely.

### US6 — Application Status and Logging
**Priority:** Medium  
**Estimate:** 2 story points

As a maintainer, I want useful application logs and a status check so that I can identify problems more easily.

**Acceptance Criteria**
- Important application actions and errors are logged.
- A simple status command or menu option confirms that the application is running.
- Error messages help users understand what went wrong without exposing unnecessary technical details.

## Definition of Done

A user story is considered done when:

- The feature works according to its acceptance criteria.
- The code is readable and organized.
- Relevant automated tests pass.
- Invalid input and expected errors are handled.
- The change is committed to Git and pushed to GitHub.
- The feature is documented when necessary.

## Sprint 1 Candidate Stories

The initial Sprint 1 plan is to deliver:

- US1 — Add a Task
- US2 — View Tasks

**Initial estimate:** 3 story points.

These features provide a small, usable foundation. The team will review progress and adjust future plans based on what is learned.

## Sprint 2 Candidate Stories

The initial Sprint 2 plan is to deliver:

- US3 — Mark a Task as Complete
- US4 — Delete a Task

Saving tasks and adding status checks and logging will be considered in subsequent work, depending on progress and capacity.
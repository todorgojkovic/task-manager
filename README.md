# Task Manager

A command-line task manager built with Python.

The application allows users to create, view, edit, search, complete, and delete tasks. Tasks are stored locally in a JSON file, so they remain saved after the program is closed.

## Features

- Add new tasks
- Choose task priority:
  - Low
  - Medium
  - High
- View all tasks
- Mark tasks as completed
- Edit task names
- Delete tasks
- Search tasks by name
- Display task statistics
- Store the creation date of each task
- Save task data in a JSON file

## Technologies Used

- Python
- JSON
- `pathlib`
- `datetime`

## Project Structure

```text
task-manager/
├── main.py
├── tasks.json
├── README.md
└── .gitignore
```

## How to Run

### 1. Make sure Python is installed

Check your Python version:

```bash
python3 --version
```

### 2. Open the project folder in the terminal

```bash
cd task-manager
```

### 3. Run the program

```bash
python3 main.py
```

If the Python file has a different name, replace `main.py` with the correct filename.

## Application Menu

```text
-- TO DO LIST --

1. Add task
2. View task
3. Mark task as done
4. Delete task
5. Edit task
6. Search
7. Statistics
8. Exit
```

## Task Data Structure

Each task is stored as a Python dictionary and saved in `tasks.json`.

Example:

```json
{
    "task": "Learn Python",
    "done": false,
    "priority": "High",
    "created_at": "2026-07-31"
}
```

Each task contains:

- `task` — the task name
- `done` — whether the task is completed
- `priority` — Low, Medium, or High
- `created_at` — the date when the task was created

## Example Output

```text
1. Learn Python [Not done] [Priority: High] [Created: 2026-07-31]
2. Finish project [Done] [Priority: Medium] [Created: 2026-07-31]
```

## Statistics

The application displays:

```text
----- Statistics -----
Total tasks: 5
Completed: 2
Remaining: 3
----------------------
```

## Data Persistence

Tasks are saved automatically in the `tasks.json` file after the user:

- adds a task
- edits a task
- deletes a task
- marks a task as completed

When the program starts, existing tasks are loaded from the JSON file.

## Future Improvements

Possible future improvements include:

- Add task deadlines
- Edit task priority
- Sort tasks by priority
- Filter completed and unfinished tasks
- Add colored terminal output
- Add confirmation before deleting a task
- Add automated tests
- Create a graphical user interface

## Author

Created as a Python learning and portfolio project.
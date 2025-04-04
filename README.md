# 📝 Task Tracker CLI
Project URL:https://github.com/joshnasatwika/Task-Tracker-CLI

A simple command-line Python application to manage your to-do list using a JSON file.

## 📦 Features

- ✅ Add new tasks
- 🔄 Update task descriptions
- 🚫 Delete tasks
- 🚧 Mark tasks as `in-progress` or `done`
- 📋 List:
  - All tasks
  - Only done tasks
  - Only not-done (todo) tasks
  - Only in-progress tasks
- 📂 Data stored locally in a `tasks.json` file

---

## ⚙️ How to Use

Run this from your terminal in the project directory:

```bash
python task_tracker.py <command> <arguments>

📌 Example Commands
python task_tracker.py add "Buy groceries"
python task_tracker.py update 1 "Buy groceries and fruits"
python task_tracker.py delete 1
python task_tracker.py mark 2 in-progress
python task_tracker.py mark 2 done
python task_tracker.py list
python task_tracker.py list done
python task_tracker.py list todo
python task_tracker.py list in-progress

🧱 Task Structure
Each task in the JSON file looks like this:
{
  "id": 1,
  "description": "Buy groceries",
  "status": "todo",
  "createdAt": "2025-04-04 14:30:00",
  "updatedAt": "2025-04-04 14:30:00"
}

🛠 Requirements
Python 3.x
No external libraries required — only built-in modules used
Works entirely from the command line

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.

📄 License
This project is open-source and free to use under the MIT License.

---

### 📤 3. Save → Commit → Push

Open your terminal in PyCharm and run:

```bash
git add README.md
git commit -m "Add README with usage instructions"
git push
git clone https://github.com/joshnasatwika/Task-Tracker-CLI.git










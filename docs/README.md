# 👾 CLI ToDo Tool by tinchosalvatore (V2 Nexus)

[![Leer en Español](https://img.shields.io/badge/Lang-Español-red)](docs/README.es.md)

### *A KISS philosophy task manager for the terminal*

An ultra-lightweight, fast, and aesthetic Command Line Interface (CLI) tool, designed for computer scientists who live in the terminal. Based on simplicity, it uses **JSON** for persistence, **Rich** for a modern UI, and **Nerd Fonts** for a superior visual experience.

**V2 New Feature:** It is now **Context Aware**. Tasks are saved linked to the specific directory you are working in.

---

## 📚 Features

This tool follows the **KISS** (*Keep It Simple, Stupid*) principle:

* **Contextual (Multitenancy)**: Manages independent task lists per project/directory.
* **Omni View**: A "God Mode" to see all your tasks from all projects in a single list.
* **No Overhead**: No heavy databases; just a structured JSON file.
* **Dynamic IDs**: Task numbers are automatically recalculated to avoid gaps when deleting.

---

## 🧰 Installation

### Prerequisites

* **Python 3.10+**
* **Nerd Fonts** (Recommended: *JetBrainsMono Nerd Font*) to render icons correctly.

### Steps

1. Clone this repository or download the files.
2. Grant execution permissions to the installer:
```bash
chmod +x setup.sh

```

3. Run the setup (it will create the virtual environment and the symbolic link):

```bash
./setup.sh

```

4. **Restart your terminal** or reload your configuration (`source ~/.zshrc` or `.bashrc`).

---

## ⌨️ Command Usage

The base command is `todo`. Remember that **tasks now depend on the directory** you are in.

| Command | Description | Example |
| --- | --- | --- |
| `todo` | Shows tasks for the **current directory**. | `todo` |
| `todo -a <task>` | Adds a task to the current directory. | `todo -a Deploy to prod` |
| `todo -t <id>` | **Toggle**: Marks/Unmarks a task as done. | `todo -t 1` |
| `todo -d <id>` | **Delete**: Removes the task and readjusts IDs. | `todo -d 2` |
| `todo -u` | Shows only **Pending** tasks (if empty, celebrate!). | `todo -u` |
| `todo -r` | **Wipeout**: DELETES all tasks in this directory (total cleanup). | `todo -r` |
| `todo -o` | **Omni View**: Shows ALL tasks from ALL directories. | `todo -o` |

---

## ⚙️ Uninstallation

The new uninstaller is smart and protects your data:

1. Run the uninstallation script:

```bash
chmod +x uninstall.sh && ./uninstall.sh

```

> **Note:** The script will interactively ask you if you wish to delete the configuration and saved tasks in `~/.config/cli_ToDo/tasks.json` or if you prefer to keep them for the future.

---

## 👨‍💻 Credits

Developed by **tinchosalvatore**.
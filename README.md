# datafun-02-automation
02-Project Initialization
 Setup and Workflow Guide
This repository provides a clear, concise guide to help set up a machine for Python projects, initialize a new Python project, and follow a repeatable project workflow when developing professional Python projects.

The instructions are divided into three parts.

Part 1: Set Up Machine & Sign up for GitHub #comment forgit pull
Go to 🟢 Machine Setup to prepare for Python projects. Start here to set up a machine for the first time (or to upgrade or verify professional tools).

This section contains one-time tasks including:

View file extensions and hidden files and folders.
Optional: Install (or verify) a package manager for your operating system.
Install Python, Git, and Visual Studio (VS) Code for your operating system.
Configure Git
Install common VS Code extensions.
Create a folder on your machine to hold your GitHub projects.
Create a GitHub account (join 100 Million Developers!)
Part 2: Initialize a Project
Go to 🟠 Project Initialization when starting a new project.

This section walks you through the steps to either:

Copy an existing project OR start a new project from scratch.
Clone your new GitHub repo to your machine.
Add common files such as .gitignore and requirements.txt.
Git add-commit-push the changes to GitHub.
Create a local project virtual environment for Python.
Part 3: Work on the Project Over Time
Go to 🔵 Repeatable Workflow for ongoing project development.

This section provides the repeatable steps for working on Python projects. These steps are typically followed whenever we make changes to a project. The workflow includes:

Pull any recent changes from GitHub.
Activate the virtual environment.
Install dependencies.
Run scripts and/or Jupyter notebooks.
Make updates, verify the code still runs, and git add-commit-push to GitHub.
Important
Follow the instructions carefully.
Follow the instructions in the recommended order.
Verify each step before proceeding.
Celebrate
Follow each step carefully. We have helped hundreds of new analysts get started with professional Python. Verify you can run both a script and a notebook successfully. Then, celebrate - that's a big iceberg needed to get started with Professional Python.

Follow The Proven Path Provided
Hopefully, each step is not too bad and things go well. When they don't - that's to be expected. Part of the reason we get hired is to "figure things out" and we are here to help you do that. Learn to do a web search, and experiment with free AI assistants to help explain and provide any additional details needed. Remember, YOU are in charge. This is the process we support and these instructions work. Do NOT deviate unless you agree to invest time and energy to ensure any of the many alternate paths work for you throughout the program.

Explore
AFTER that is where the power and joy of working with Python begins. Keep good notes. Save the working versions and then, change things. For example:

Rename a variable.
Add a new statement.
Comment things out.
Rename a function.
View the logs. Log something new (e.g., every function when called and before returning a value).
Working with code is a fun, safe, rewarding way to learn. If you enjoy puzzles, getting value from Python is a great way to earn a living.

CheatSheet: Commands to Manage Virtual Environment
For Windows PowerShell (change if using Mac/Linux). Keep these notes in every project README.md.

py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -r requirements.txt
CheatSheet: Commands to Run Python Scripts
Remember to activate your .venv (and install packages if they haven't been installed yet) before running files. Verify that all external packages imported into a file are included in requirements.txt (and have NOT been commented out).

py demo_script.py
py do_stats.py
py draw_chart.py
py greet_user.py
CheatSheet: Commands to Git add-commit-push
git add .
git commit -m "custom message"
git push -u origin main
OPTIONAL/EXPERIMENTAL: Google NotebookLLM AI-Generated Guides
AI generated audio, video, summary, and chat for each of the recommended workflows. These AI generated chats should support the recommended workflow. Caution: they are experiemental. Use printed instructions from the repo for best results.

Part 1 of 3: 🟢 Set Up Machine
Part 2 of 3: 🟠 Project Initialization
Part 3 of 3: 🔵 Repeatable Workflow
Listen to the NotebookLLM Audio Guides
If you prefer listening while following the written steps above, optional Audio Guides are available. These are AI-generated two-person podcasts.

The audio is supplementary and not a replacement for the written instructions. The guides are not necessarily recommended. They may be distracting, and the speakers mispronounce key files and commands. They are mostly interesting from a state-of-the-art perspective.

OPTIONAL: Share Feedback
Feel free to ask questions in the GitHub Discussions or raise a GitHub Issue if you have suggestions or need additional clarification.

# Project README

## Introduction

Welcome to our project! This guide will walk you through setting up and running the project code.

Our project uses Python, a powerful programming language, and Visual Studio Code (VSCode), a free source-code editor, to analyze data fetched from a database and clean it up for further exploration.

## Table of Contents

- [Project README](#project-readme)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Check Python Installation](#check-python-installation)
  - [Setting up VSCode](#setting-up-vscode)
  - [Clone the Repository](#clone-the-repository)
  - [Set up Virtual Environment and Install Dependencies](#set-up-virtual-environment-and-install-dependencies)
  - [Grant Full Disk Access to Visual Studio Code on macOS](#grant-full-disk-access-to-visual-studio-code-on-macos)
  - [Running the Code](#running-the-code)

## Check Python Installation

To begin, ensure that Python 3 is installed on your system. To verify this, open a terminal (Command Prompt on Windows, Terminal on Mac/Linux) and type:

```bash
python --version
```

This should return a version number. Make sure the version starts with `3.`. If Python isn't installed or you have a version older than 3, visit the [Python download page](https://www.python.org/downloads/) to download and install Python. 

## Setting up VSCode

Next, install Visual Studio Code (VSCode). You can download it [here](https://code.visualstudio.com/download). 

Once VSCode is installed, you'll also need to install the Python extension:

1. Open VSCode.
2. Click on the Extensions view icon on the Sidebar (or press `Ctrl+Shift+X`).
3. Search for `Python`.
4. Click on the first result to install the Python extension for VSCode.

## Clone the Repository

Now we need to get the project code onto your local machine. This is done through a process called "cloning". To clone the repository:

1. Navigate to the project's GitHub page.
2. Click the `Code` button.
3. Click the `clipboard` icon to copy the URL.
4. Open VSCode.
5. Press `Ctrl+Shift+P` to open the Command Palette.
6. Type `git clone` and press `Enter`.
7. Paste the URL you copied and press `Enter`.

You have now cloned the repository onto your local machine.

## Set up Virtual Environment and Install Dependencies

To isolate our project and its dependencies, we will create a virtual environment and install all necessary Python packages:

1. Open a terminal in VSCode by clicking `Terminal > New Terminal`.
2. Navigate to the directory where you cloned the repository (use `cd your_project_folder`).
3. Create a new virtual environment by running `python -m venv venv`.
4. Activate the virtual environment: 
    - On Windows, run `.\venv\Scripts\activate`.
    - On Unix or MacOS, run `source venv/bin/activate`.
5. Once the virtual environment is activated, install the necessary packages by running `pip install -r requirements.txt`.

You have now set up your virtual environment and installed all required Python packages.

## Grant Full Disk Access to Visual Studio Code on macOS

To grant "read all files on disk" permission to Visual Studio Code, you need to provide VSCode with Full Disk Access on your Mac. Please follow the steps below:

1. Open `System Preferences` on your Mac.
2. Click on `Security & Privacy`.
3. Switch to the `Privacy` tab.
4. Scroll down the list on the left and click on `Full Disk Access`.
5. You will see a list of applications that have requested full disk access. 
6. If your settings are locked, click the lock at the bottom left to unlock them. You'll need to enter your admin password.
7. Now, click on the `+` sign to add an application to the list.
8. In the file chooser that pops up, press `Cmd+Shift+G` to open the "Go to the folder" dialog.
9. Enter the following path to access VSCode: `/Applications/Visual Studio Code.app` and click `Go`.
10. Visual Studio Code should now appear in the file chooser. Click `Open` to add it to the list of applications with Full Disk Access.
11. Ensure that the checkbox next to `Visual Studio Code` in the list is checked.
12. If you previously unlocked the settings, remember to click the lock again to prevent further changes.

VSCode now has Full Disk Access. You might need to restart VSCode for these changes to take effect. If you're still experiencing issues, try restarting your Mac.

Remember to be cautious when giving applications Full Disk Access, as they'll have access to all data on your disk. Only grant this access to trusted applications like Visual Studio Code.

## Running the Code

Now you are ready to run the code:

1. In VSCode, open the file `analyzer.ipynb`.
2. You will see the file divided into sections, each with a "Run" icon at the top-left corner.
3. Click the "Run" icon on each section to execute the code in that section.

You should now see the output of the code.

Thank you for using our project! If you have any issues, feel free to raise an issue in the GitHub repository.
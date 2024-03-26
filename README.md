# Phase 3 Project: Car Rental System With CLI and ORM

## Requirements

You need to implement a Python CLI Application that meets the following requirements.

### ORM Requirements

- The application must include a database created and modified with Python ORM methods that you write.
- The data model must include at least 3 model classes.
- The data model must include at least 1 one-to-many relationships.
- Property methods should be defined to add appropriate constraints to each model class.
- Each model class should include ORM methods (create, delete, get all, and find by id at minimum).

### CLI Requirements

- The CLI must display menus with which a user may interact.
- The CLI should use loops as needed to keep the user in the application until they choose to exit.
- For EACH class in the data model, the CLI must include options: to create an object, delete an object, display all objects, view related objects, and find an object by attribute.
- The CLI should validate user input and object creations/deletions, providing informative errors to the user.
- The project code should follow OOP best practices.
- Pipfile contains all needed dependencies and no unneeded dependencies.
- Imports are used in files only where necessary.
- Project folders, files, and modules should be organized and follow appropriate naming conventions.
- The project should include a README.md that describes the application.

### Introduction

- Start with the project template (provided in the following lesson). You are free to adapt the template structure, as long as you adhere to the project requirements.
- Think about the user interaction. How will you prompt the user? What information will the user enter? How will you provide feedback to the user?
- Think about your data model. How will you organize and store the information received from the user?
- If you get stuck trying to accomplish a specific task, check online to see if there's a Python library that will make it easier.

### Getting Started
- Clone the repository:
git clone <repository_url>

- Navigate to the project directory:
cd car-rental-system-cli

- Install dependencies:
pipenv install

- Activate the virtual environment:
pipenv shell

- Run the CLI application:
python lib/cli.py

### Directory Structure

Certainly! Below is the content formatted as a README.md file:

markdown
Copy code
# Car Rental System CLI with ORM

## Requirements

You need to implement a Python CLI Application that meets the following requirements.

### ORM Requirements

- The application must include a database created and modified with Python ORM methods that you write.
- The data model must include at least 2 model classes.
- The data model must include at least 1 one-to-many relationships.
- Property methods should be defined to add appropriate constraints to each model class.
- Each model class should include ORM methods (create, delete, get all, and find by id at minimum).

### CLI Requirements

- The CLI must display menus with which a user may interact.
- The CLI should use loops as needed to keep the user in the application until they choose to exit.
- For EACH class in the data model, the CLI must include options: to create an object, delete an object, display all objects, view related objects, and find an object by attribute.
- The CLI should validate user input and object creations/deletions, providing informative errors to the user.
- The project code should follow OOP best practices.
- Pipfile contains all needed dependencies and no unneeded dependencies.
- Imports are used in files only where necessary.
- Project folders, files, and modules should be organized and follow appropriate naming conventions.
- The project should include a README.md that describes the application.

### How to Begin?

- Start with the project template (provided in the following lesson). You are free to adapt the template structure, as long as you adhere to the project requirements.
- Think about the user interaction. How will you prompt the user? What information will the user enter? How will you provide feedback to the user?
- Think about your data model. How will you organize and store the information received from the user?
- If you get stuck trying to accomplish a specific task, check online to see if there's a Python library that will make it easier.

## Introduction

You now have a basic idea of what constitutes a CLI. Fork and clone this lesson for a project template for your CLI.

### Directory Structure

.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
├── models
│ ├── init.py
│ └── model_1.py
├── cli.py
├── debug.py
└── helpers.py

### Generating Your Environment

- Install any additional dependencies you know you'll need for your project by adding them to the Pipfile.
- Then run the commands:

```bash
pipenv install
pipenv shell


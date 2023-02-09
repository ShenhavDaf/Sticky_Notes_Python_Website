## About:

This app is my first Python project - a sticky notes web app with the option to register & login to the site, add new notes and delete them. [Guide](https://www.youtube.com/watch?v=dam0GPOAvVI&ab_channel=TechWithTim).

## Libraries & Installations:

- Jinja - a fast, expressive, extensible templating engine. Special placeholders in the template allow writing code similar to Python syntax. Then the template is passed data to render the final document.

##### Install in CMD: `pip install Jinja2`

- Flask - provides configuration and conventions, with sensible defaults, to get started.

#### `pip install flask`

- Flask-Login - provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time.

#### `pip install flask-login`

- Flask-SQLAlchemy (sqlite)- an extension for Flask that adds support for SQLAlchemy to the application.\
  SQLAlchemy provides tools for managing connectivity to a database, interacting with database queries and results, and programmatic construction of SQL statements.

#### `pip install flask-sqlalchemy`

## Screenshots:

#### Login & Register:

<img src="/public/1.png" style="height: 450px;">

#### Homepage:

<img src="/public/2.png" style="height: 350px;">

#### Addition new notes:

<img src="/public/3.png" style="height: 450px;">

#### Delete notes no.2 & no.6:

<img src="/public/4.png" style="height: 450px;">
<img src="/public/5.png" style="height: 450px;">

## Run flask development server:

In the project directory, you can run:

#### `main.py`

In vscode with Python extension:

- Go to 'main.py' file.
- Right-click anywhere in the editor and select Run Python File in Terminal

This is runs the app in the development mode.\
Open [http://127.0.0.1:5000](http://127.0.0.1:5000) to view it in your browser.

# Flask CRUD API

### Create a Flask API

#### Perform CRUD Operation
1. **Create**: `POST /data`
2. **Read**: `GET /data` and `GET /data/<int:user_id>`
3. **Update**: `PUT /data/<int:user_id>`
4. **Delete**: `DELETE /data/<int:user_id>`

## Project Overview

This project is a simple backend API built with Flask to perform CRUD operations. It is designed to help understand basic functionality and structure of a Flask application. The API interacts with a database and provides endpoints to create, read, update, and delete data.

## Files in the Repository

- **`app/`**: Contains the main application code, including blueprints for different modules.
- **`.gitignore`**: Specifies files and directories to be ignored by Git.
- **`README.md`**: Project documentation.
- **`app.py`**: Main application file to run the Flask app.

## Installation

To set up the project, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/subham-behera/flask_crud.git
    cd flask_crud
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the root directory and add your database configuration and other environment variables**:
    ```env
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'project'
    ```

## Running the App

To run the Flask application, execute the following command in your terminal:
```bash
flask run

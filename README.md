# Flask Application
## Overview

This repository contains three tasks prepared for the [Purkiáda](https://purkiada.sspbrno.cz/) school competition:
- Task 1: Hashing and cryptography
- Task 2: Minimal Flask base setup that later evolved into a follow-up task
- Task 3: IT tech quiz



## Quick Start

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation

```bash
pip install flask flask-login flask-sqlalchemy
```

## Running the Application

1. Navigate to the project directory
2. Set the Flask app environment variable:

   **Windows PowerShell:**
   ```powershell
   $env:FLASK_APP="main"
   ```

   **Linux/Mac:**
   ```bash
   export FLASK_APP=main
   ```

3. Start the Flask server:
   ```bash
   flask run --host 0.0.0.0 --port <port_number>
   ```

   > **Note:** You'll need to set the `FLASK_APP` environment variable again after closing the terminal.

### Port Configuration

| Task | Port |
|------|------|
| Robin (Task 2) | 7722 |
| Valon (Task 4) | 7724 |
| Adam (Task 7) | 7727 |

## Database Setup

### Importing Data to SQLite Database

1. Open SQLite console:
   ```bash
   sqlite3 db.sqlite
   ```

2. Set import mode (e.g., for CSV files):
   ```sql
   .mode csv
   ```

3. Import your data file:
   ```sql
   .import data.csv user
   ```

   > **Important:** The database table is named `user`. Please maintain this naming convention to avoid configuration issues.

### Default Login Credentials

For testing purposes, a default account is available:
- **Username:** `aaaaa`
- **Password:** `asd`

## Notes

- The database file should always be named `db.sqlite`
- Make sure to keep the `user` table name when importing data
- The application runs on Flask with SQLAlchemy for database operations and Flask-Login for authentication

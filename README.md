# Project Setup Guide

This guide will help you set up and run the project on your local machine. Follow the steps below based on your operating system.

## Prerequisites

- Ensure Python (3.8 or higher) is installed on your machine. You can download it from [python.org](https://www.python.org/).
- Install `pip` (Python package installer) if not already installed.
- Install MySQL if not already installeed

## Setup Instructions

### Step 1: Create Database and Import SQL File

First, create a new database in MySQL. You can do this using the MySQL command line or a database management tool like phpMyAdmin.

#### Using MySQL Command Line:

```bash
mysql -u root -p
CREATE DATABASE your_database_name;
EXIT;
```

Next, import the provided SQL file from the GitHub repository into your newly created database:

```bash
mysql -u root -p your_database_name < path/to/your/responsi_5230411121.sql
```

Replace `your_database_name` with the name of your database and `path/to/your/responsi_5230411121.sql` with the path to the SQL file.

#### Using phpMyAdmin:

1. Open phpMyAdmin and log in.
2. Create a new database.
3. Select the new database and go to the "Import" tab.
4. Choose the SQL file from the GitHub repository and click "Go".

Once the database is set up and the SQL file is imported, proceed to the next steps.

### Step 2: Create a Virtual Environment

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### On Linux/Mac OS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Requirements

Install the necessary dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Copy the `.env.example` file to `.env`:

```bash
cp .env.example .env
```

Edit the `.env` file and set up the environment variables as needed.

### Step 5: Run the Application

Finally, start the main application:

```bash
python main.py
```

---

## Notes

- Make sure to activate the virtual environment before running any commands.
- If you encounter issues, ensure all dependencies are properly installed and the `.env` file is correctly configured.
- When configuring the `.env` file, use `127.0.0.1` instead of `localhost` for `DB_HOST` to avoid potential bugs.
- For additional help, consult the project documentation or contact the maintainer.

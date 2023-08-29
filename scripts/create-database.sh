#!/bin/bash

# Path to the database file inside the container
DATABASE_PATH="/app/data/database.sqlite"

# Check if the database file exists
if [ ! -e "$DATABASE_PATH" ]; then
  echo "Creating SQLite database..."

  # Create the database file
  touch "$DATABASE_PATH"

  # Run any necessary database initialization commands
  sqlite3 "$DATABASE_PATH" "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT);"

  echo "SQLite database created and initialized."
else
  echo "SQLite database already exists. Skipping initialization."
fi

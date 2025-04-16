import sqlite3
import os

# Setup
DB_NAME = 'TextEditor.db'
STORAGE_DIR = './TextFiles'

# Ensure storage dir exists
os.makedirs(STORAGE_DIR, exist_ok=True)

# Function: Upload file and its content to STORAGE_DIR
def upload_file(filename:str):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Prepare filename and destination
        filename = os.path.basename(filename)
        destination_path = os.path.join(STORAGE_DIR, filename)

        # Save content to new file in the storage directory, or update it if already exists
        with open(destination_path, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        raise e

def create_textfiles_table():
    # Connecting to the database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Creating textfiles table
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS textfiles (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                filename TEXT NOT NULL,
                created_at TEXT DEFAULT (DATETIME('now')),
                author TEXT NOT NULL DEFAULT 'lollocenne'
            );
        """)

        conn.commit()
    except sqlite3.Error as e:
        raise e
    finally:
        cursor.close()
        conn.close()

# Function: Insert new textfile row
def insert_textfile_row(filename:str, author:str = 'lollocenne') -> None:
    """
        Insert a new row with textfile content and related data into 'textfiles' table and add the file on TextFiles directory.

        Args:
        - filename(str): Name of the text file.
        - author(str): Name of the author of the file (repository author by default in case of not provided value).
        
        Returns:
        - None
    """
    # Connecting to the database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        filepath = os.path.join(STORAGE_DIR, os.path.basename(filename)) # Joining filename with directory of destination
        cursor.execute("""
            INSERT INTO textfiles (filename, author) 
            VALUES (?, ?);
        """, (filepath, author))

        conn.commit() # Save changes on DB

        upload_file(filename) # Save file and its content on the directory
    except sqlite3.Error as e:
        raise e
    finally:
        cursor.close()
        conn.close()
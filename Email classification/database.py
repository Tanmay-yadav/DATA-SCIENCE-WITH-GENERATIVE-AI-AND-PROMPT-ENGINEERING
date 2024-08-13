import sqlite3

def connect_db():
    conn = sqlite3.connect('database.db')
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            actual_class TEXT,
            predicted_class TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_data(actual_class, predicted_class):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO results (actual_class, predicted_class)
        VALUES (?, ?)
    ''', (actual_class, predicted_class))
    conn.commit()
    conn.close()

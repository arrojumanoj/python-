
import sqlite3

class SQLiteHandler:
    def __init__(self, db_path="log_analysis.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip TEXT,
                datetime TEXT,
                request TEXT,
                status INTEGER,
                size INTEGER
            );
        """)
        self.conn.commit()

    def insert_log(self, log_entry):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO logs (ip, datetime, request, status, size)
            VALUES (?, ?, ?, ?, ?)
        """, log_entry)
        self.conn.commit()

    def close(self):
        self.conn.close()

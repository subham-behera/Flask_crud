# db.py

import mysql.connector
from app.config import get_db_config

class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        db_config = get_db_config()
        self.connection = mysql.connector.connect(**db_config)

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def get_cursor(self):
        if not self.connection:
            self.connect()
        return self.connection.cursor()

db = Database()

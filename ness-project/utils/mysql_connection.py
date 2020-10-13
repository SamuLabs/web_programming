import mysql.connector
import os

DATABASE_HOST=os.getenv("DATABASE_HOST")
DATABASE_USER=os.getenv("DATABASE_USER")
DATABASE_PASSWORD=os.getenv("DATABASE_PASSWORD")
DATABASE_NAME=os.getenv("DATABASE_NAME")

class MysqlConnection():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=DATABASE_HOST,user=DATABASE_USER,
            password=DATABASE_PASSWORD,database=DATABASE_NAME
        )

        self.cursor = self.connection.cursor()
        
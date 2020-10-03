import mysql.connector
import random
import unittest
import os

from utils.mysql_connection import MysqlConnection
from app.models import Users

class TestDatabase(unittest.TestCase):
    def setUp(self):
        DATABASE_HOST=os.getenv("DATABASE_HOST")
        DATABASE_USER=os.getenv("DATABASE_USER")
        DATABASE_PASSWORD=os.getenv("DATABASE_PASSWORD")
        DATABASE_NAME=os.getenv("DATABASE_NAME")

        self.connection = MysqlConnection(
            DATABASE_HOST,
            DATABASE_USER,
            DATABASE_PASSWORD,
            DATABASE_NAME
        )
        self.cursor = self.connection.cursor
    
    def test_connection_successful(self):
        connection = self.connection.connection
        self.assertIsNotNone(connection)
        self.assertIsInstance(connection, mysql.connector.connection.MySQLConnection)

    def test_set_cursor(self):
        self.assertIsNotNone(self.cursor)
        self.assertIsInstance(self.cursor, mysql.connector.cursor.MySQLCursor)

    def test_execute_select_query(self):
        for x in self.cursor:
            self.assertIsNone(x)

    def test_create_user(self):
        user = self.cursor.execute("INSERT INTO users ... ")
        self.assertIsNone(user)
        self.assertIsInstance(user, Users)

    def test_select_users(self):
        user = self.cursor.execute("SELECT * from users")
        self.assertIsNone(user)
        self.assertIsInstance(user, list)
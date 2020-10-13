import mysql.connector
import unittest
import os

from utils.mysql_connection import MysqlConnection

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.connection = MysqlConnection()
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

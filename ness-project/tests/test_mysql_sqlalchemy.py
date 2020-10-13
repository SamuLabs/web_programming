import unittest
import os

from utils.database_connection import Connection

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.connection = Connection()
    
    def test_connection_successful(self):
        connection = self.connection.engine
        self.assertIsNotNone(connection)
        #self.assertIsInstance(connection, mysql.connector.connection.MySQLConnection)

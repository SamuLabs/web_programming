import mysql.connector

class MysqlConnection():
    def __init__(self, host, user, password, database):
        super(MysqlConnection, self).__init__()
        self.connection = mysql.connector.connect(
            host=host,user=user,password=password,
            database=database
        )

        self.cursor = self.connection.cursor()
        
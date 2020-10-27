from sqlalchemy import create_engine

import os

DATABASE_DRIVER=os.getenv("DATABASE_DRIVER")
DATABASE_HOST=os.getenv("DATABASE_HOST")
DATABASE_USER=os.getenv("DATABASE_USER")
DATABASE_PASSWORD=os.getenv("DATABASE_PASSWORD")
DATABASE_NAME=os.getenv("DATABASE_NAME")
DATABASE_PORT=os.getenv("DATABASE_PORT")

class Connection():
    def __init__(self):
        self.engine = create_engine('{driver}://{username}:{password}@\
            {host}:{port}/{database}'.format(driver=DATABASE_DRIVER,
            username=DATABASE_USER, password=DATABASE_PASSWORD,
            host=DATABASE_HOST, port=DATABASE_PORT, database=DATABASE_NAME))
        #self.connection = self.engine.connect()
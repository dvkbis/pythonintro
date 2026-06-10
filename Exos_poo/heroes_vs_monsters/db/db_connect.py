import psycopg2 as pg

class DBConnect:
    _instance = None

    ## SINGLETON
    def __new__(cls):
        if cls._instance is None:

            cls._instance = super().__new__(cls)
            cls._instance.conn = pg.connect(
                dbname="heromonster",
                user= "postgres",
                password= "postgres",
                host= "localhost",
                port= "5432"
            )

        return cls._instance

import psycopg2


class DatabaseConnection:
    def __init__(self, db_name, db_user, db_password, db_host, db_port):
        self.__db_name = db_name
        self.__db_user = db_user
        self.__db_password = db_password
        self.__db_host = db_host
        self.__db_port = db_port

    def get_connection(self):
        try:
            conn = psycopg2.connect(
                dbname=self.__db_name,
                user=self.__db_user,
                password=self.__db_password,
                host=self.__db_host,
                port=self.__db_port
            )
            cursor = conn.cursor()
            return cursor
        except (Exception, psycopg2.Error) as error:
            print(error)

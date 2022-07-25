from dotenv import load_dotenv

import pymysql
import os
import logging



class Mysql:
    def __init__(self):
        load_dotenv()



    @staticmethod
    def __connect():

        connection = pymysql.connect(
            host=os.getenv("HOST_NAME"),
            user=os.getenv("DB_USERNAME"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection


    def make_request(self, sql_request : str, is_need_data : bool):
        try:
            connection = Mysql.__connect()
            if (connection is None):
                raise Exception
                return False

            with connection.cursor() as cursor:
                response = cursor.execute(sql_request)
                connection.commit()
                if (is_need_data):
                    return cursor.fetchall()

                return True if response else False

        except Exception as exception:
            logger = logging.getLogger()
            logger.error(f"Failed to make request: {exception}")

        finally:
            connection.close()
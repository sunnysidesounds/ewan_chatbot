
import pymysql
import logging
from config import settings


class MysqlAdapter:

    def __init__(self):
        print("MysqlAdapter")

    def get(self, query):
        try:
            connection = pymysql.connect(host=settings.DB_HOST, port=3306, user=settings.DB_USER,
                                         passwd=settings.DB_PASS, db=settings.DB_NAME)
            cursor = connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            rows_set = []
            for row in rows:
                rows_set.append(row)

            return rows_set

        except Exception, e:
            logging.log(logging.ERROR, e)
            logging.log(logging.ERROR, " - query error : " + query)

    def set(self, query, data):
        try:
            connection = pymysql.connect(host=settings.DB_HOST, port=3306, user=settings.DB_USER,
                                         passwd=settings.DB_PASS, db=settings.DB_NAME)
            cursor = connection.cursor()
            cursor.execute(query, data)
            connection.commit()
        except Exception, e:
            logging.log(logging.ERROR, e)
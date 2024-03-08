import contextlib
import mysql.connector
from mysql.connector import errorcode

@contextlib.contextmanager
def connect(data_connection : dict):
    try:
        
        with mysql.connector.connect(**data_connection) as cnx:
            yield cnx.cursor()
 
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        cnx.close()
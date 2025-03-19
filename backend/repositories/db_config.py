import mysql.connector
from  contextlib import contextmanager

@contextmanager
def db_connection_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="expense_manager"
    )

    if not connection.is_connected():
        print("Failed To Connect")

    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()
    cursor.close()
    connection.close()



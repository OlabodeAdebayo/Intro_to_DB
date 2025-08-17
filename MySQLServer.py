import mysql.connector
from getpass import getpass
from mysql.connector import connect, Error

def create_database();
    try:
        with connect(
            host = "localhost",
            user = input("Enter username: "),
        ) as connection:
            alx_book_store = "Database 'alx_book_store' created successfully!"
            with connection.cursor() as cursor:
                cursor.execute(alx_book_store)
    
    except Error as e:
        print(e)

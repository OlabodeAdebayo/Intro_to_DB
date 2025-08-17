import mysql.connector
from getpass import getpass
from mysql.connector import connect, Error

def create_database();
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = input("Enter username: "),
            password =  input("Enter password: ")
        ) 

        if connection.is_connected():
            cursor = connection.cursor()

            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
                           
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        print(e)

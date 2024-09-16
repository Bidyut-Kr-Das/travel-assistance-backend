import sqlite3

def create_connection():
    try:
        connection = sqlite3.connect('./database/travel_assistance.db')
        cursor = connection.cursor()
        return connection,cursor
    except sqlite3.Error as e:
        print(e)
        return None
    
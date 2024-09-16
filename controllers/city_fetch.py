from database.connection import create_connection


def get_all_cities():
    conn,cursor = create_connection()
    query = '''Select distinct destination_city from flights'''
    cursor.execute(query)

    cities = [row[0] for row in cursor.fetchall()]
    return cities
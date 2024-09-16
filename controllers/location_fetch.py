from database.connection import create_connection

def fetch_coords(airport_code):
    conn,cursor = create_connection()
    airport_code = airport_code.upper()

    cursor.execute("SELECT * FROM airports where iata_code = ? OR gps_code = ? OR local_code = ?",(airport_code,airport_code,airport_code))
    result = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    airports_list = [dict(zip(column_names, airport)) for airport in result]

    conn.close()
    return airports_list[0]
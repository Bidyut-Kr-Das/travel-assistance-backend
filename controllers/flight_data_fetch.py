from database.connection import create_connection


def get_flight_data(user_data,predicted_price):
    conn,cursor = create_connection()
    where_clauses = []
    params = []

    if user_data.get('source_city'):
        where_clauses.append("source_city = ?")
        params.append(user_data['source_city'])

    if user_data.get('destination_city'):
        where_clauses.append("destination_city = ?")
        params.append(user_data['destination_city'])

    if user_data.get('stops'):  # 0 is a valid value, so check for None
        where_clauses.append("stops = ?")
        params.append(user_data['stops'])

    if user_data.get('class'):
        where_clauses.append("class = ?")
        params.append(user_data['class'])

    #create the where clause from the clause list
    where_clause = " AND ".join(where_clauses)

    # Query to fetch top 3 flights closest to the predicted price
    query = f'''
    SELECT * FROM flights WHERE {where_clause}
    Order by ABS(price - ?) ASC LIMIT 3
    '''
    
    #add the predicted price to the params list
    params.append(predicted_price)

    cursor.execute(query, tuple(params))
    top_3_flights = cursor.fetchall()

    #get the column names 
    column_names = [description[0] for description in cursor.description]

    flights_list = [dict(zip(column_names, flight)) for flight in top_3_flights]
    
    conn.close()

    return flights_list
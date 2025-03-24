def insert_in_database(conn, table, columns, data):
    coluns = data.keys()
    values = tuple(data.values())

    placeholders = ", ".join(["%s"] * len(columns))
    columns = ", ".join(columns)

    query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

    try:
        conn.execute(query, values)
        conn.commit()
        print("Inserted into {table} successfully".format(table=table))
    except Exception as e:
        conn.rollback()
        print("Failed to insert into {table}: {e}".format(table=table, e=e))

import sqlite3
import json
def get_db_connection():
    """Establishes a connection to the SQLite database file."""
    # Connect to a database file named 'tutorial.db'
    # If the file does not exist, it will be created automatically.
    # Using the 'with' statement ensures the connection is closed automatically.
    try:
        conn = sqlite3.connect('database.db')
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None
conn = get_db_connection()
def set_value(database: str, id: int, variable: str, value):
    if conn:
        guildConf = get_value(database,id,variable)
        if guildConf != None:
            insert_value(database,id,variable,value)
        else:
            insert_value(database,id,variable,value)
def get_value(database: str, id: int,variable: str):
    if conn:
        create_database(database)
        query = "SELECT EXISTS(SELECT 1 FROM " +database+" WHERE id = ?)"
        cursor = conn.cursor()
        cursor.execute(query, (str(id),)) # The ID must be passed as a tuple

        # Fetch the result and unpack the value
        # fetchone() returns a tuple, e.g., (1,) or (0,)
        result_tuple = cursor.fetchone()
        if result_tuple:
            pass
        else:
            insert_value(database,id,variable,None)
        query = "SELECT * FROM "+database+" WHERE id = ?"
        cursor.execute(query, (str(id),))
        user = cursor.fetchone()
        if user:
            if variable in json.loads(user[1]):
                return json.loads(user[1])[variable]
        else:
            return None
def create_database(name: str):
    if conn:
        cursor = conn.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS """+name +"""(
            id TEXT,
            config TEXT
        );
        """
        cursor.execute(create_table_query)
        # Commit the changes to save the table creation
        conn.commit()
def insert_value(database: str, id: int, variable: str, value):
    if conn:
        cursor = conn.cursor()
        query = "SELECT EXISTS(SELECT 1 FROM " +database+" WHERE id = ?)"
        cursor = conn.cursor()
        cursor.execute(query, (str(id),)) # The ID must be passed as a tuple

            # Fetch the result and unpack the value
            # fetchone() returns a tuple, e.g., (1,) or (0,)
        result_tuple = cursor.fetchone()
        if result_tuple:
            pass
        else:
            insert_value(database,id,variable,None)
        query = "SELECT * FROM "+database+" WHERE id = ?"
        cursor.execute(query, (str(id),))
        user = cursor.fetchone()
        
        if user == None: 
            insert_query = """
            INSERT INTO """+ database +""" (id, config) VALUES (?, ?)
            """
            # Using a tuple of parameters is the recommended way to insert data safely
            cursor.execute(insert_query, ( str(id), json.dumps({variable: value})))
            # Commit the changes
            conn.commit()
        else:
            if user:
                user = json.loads(user[1])
                user[variable] = value
                insert_query = """
                UPDATE """+database+"""
                        SET config = ? 
                        WHERE id = ?
                """
                # Using a tuple of parameters is the recommended way to insert data safely

                cursor.execute(insert_query, (json.dumps(user), str(id)))
                # Commit the changes
                conn.commit()
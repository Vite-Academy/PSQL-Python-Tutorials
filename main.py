import psycopg

# Connect to your postgres DB
conn = psycopg.connect(
    dbname="postgres", 
    user="postgres",
    host="localhost",
    password="080199")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM accounts")

# Retrieve query results
records = cur.fetchall()

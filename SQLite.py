import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('mydatabase.db')

# Connect to in-memory database
# conn = sqlite3.connect(':memory:')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")

# Insert data into the table
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('John Doe', 'john@example.com'))

# Commit the changes
conn.commit()

# Query the database
cursor.execute("SELECT * FROM users")
cursor.execute("DROP TABLE users")
print(cursor.fetchall())

# Close the cursor and connection
cursor.close()
conn.close()
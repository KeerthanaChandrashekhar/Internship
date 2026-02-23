import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("school.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE students (
    id INTEGER,
    name TEXT,
    marks INTEGER
)
""")

# Insert data
cursor.execute("INSERT INTO students VALUES (1, 'Amit', 85)")

# Save changes
conn.commit()

# Fetch data
cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

# Close connection
conn.close()

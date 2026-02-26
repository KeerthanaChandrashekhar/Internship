import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# DROP old table (IMPORTANT FIX)
cursor.execute("DROP TABLE IF EXISTS interns")

# Create new table with stipend column
cursor.execute("""
CREATE TABLE interns (
    intern_id INTEGER PRIMARY KEY,
    intern_name TEXT,
    track TEXT,
    stipend INTEGER
)
""")

# Insert data
cursor.executemany("""
INSERT INTO interns (intern_id, intern_name, track, stipend)
VALUES (?, ?, ?, ?)
""", [
    (1, "Keerthana", "Data Science", 7000),
    (2, "Arjun", "Web Development", 4000),
    (3, "Priya", "Data Science", 6000),
    (4, "Rahul", "Cyber Security", 5500),
    (5, "Sneha", "Data Science", 4500),
    (6, "Kiran", "Web Development", 6500)
])

conn.commit()

# Test query
df = pd.read_sql_query("SELECT * FROM interns", conn)

print(df)

conn.close()
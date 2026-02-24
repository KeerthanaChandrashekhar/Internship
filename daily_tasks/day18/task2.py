# Step 1: Import libraries
import sqlite3
import pandas as pd

# Step 2: Create connection to SQLite database
# This will create internship.db file if it doesn't exist
conn = sqlite3.connect("internship.db")

# Step 3: Create cursor
cursor = conn.cursor()

# Step 4: Create interns table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    intern_id INTEGER PRIMARY KEY,
    intern_name TEXT,
    track TEXT
)
""")

# Step 5: Create mentors table
cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    mentor_id INTEGER PRIMARY KEY,
    mentor_name TEXT,
    track TEXT
)
""")

# Step 6: Insert data into interns table
cursor.execute("DELETE FROM interns")  # optional: clears old data

cursor.executemany("""
INSERT INTO interns (intern_id, intern_name, track)
VALUES (?, ?, ?)
""", [
    (1, "Keerthana", "Data Science"),
    (2, "Arjun", "Web Development"),
    (3, "Priya", "Data Science"),
    (4, "Rahul", "Cyber Security")
])

# Step 7: Insert data into mentors table
cursor.execute("DELETE FROM mentors")  # optional: clears old data

cursor.executemany("""
INSERT INTO mentors (mentor_id, mentor_name, track)
VALUES (?, ?, ?)
""", [
    (101, "Dr. Sharma", "Data Science"),
    (102, "Mr. Kumar", "Web Development"),
    (103, "Ms. Patel", "Cyber Security")
])

# Step 8: Save changes
conn.commit()

# Step 9: INNER JOIN query
query = """
SELECT interns.intern_id,
       interns.intern_name,
       interns.track,
       mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track;
"""

# Step 10: Load result into Pandas DataFrame
df = pd.read_sql_query(query, conn)

# Step 11: Display result
print("Interns and their mentors:\n")
print(df)

# Step 12: Close connection
conn.close()
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    year INTEGER
)
""")

cursor.execute("""
CREATE TABLE subjects (
    subject_id INTEGER PRIMARY KEY,
    subject_name TEXT,
    department TEXT
)
""")

cursor.execute("""
CREATE TABLE marks (
    student_id INTEGER,
    subject_id INTEGER,
    marks INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
)
""")

# -----------------------------
# 2. Insert Sample Data
# -----------------------------
students_data = [
    (1, 'Alice', 'Computer Science', 1),
    (2, 'Bob', 'Computer Science', 2),
    (3, 'Charlie', 'Mathematics', 1),
    (4, 'David', 'Mathematics', 2),
    (5, 'Eva', 'Physics', 1),
    (6, 'Frank', 'Physics', 2),
    (7, 'Grace', 'Computer Science', 3),
    (8, 'Helen', 'Mathematics', 3),
    (9, 'Ian', 'Physics', 3),
    (10, 'Jack', 'Computer Science', 4)
]

subjects_data = [
    (101, 'Data Structures', 'Computer Science'),
    (102, 'Algorithms', 'Computer Science'),
    (201, 'Linear Algebra', 'Mathematics'),
    (202, 'Statistics', 'Mathematics'),
    (301, 'Quantum Mechanics', 'Physics'),
    (302, 'Thermodynamics', 'Physics')
]

marks_data = [
    (1, 101, 85),(1, 102, 90),
    (2, 101, 78),(2, 102, 82),
    (3, 201, 88),(3, 202, 92),
    (4, 201, 75),(4, 202, 70),
    (5, 301, 95),(5, 302, 89),
    (6, 301, 60),(6, 302, 65),
    (7, 101, 99),(7, 102, 97),
    (8, 201, 55),(8, 202, 58),
    (9, 301, 72),(9, 302, 68),
    (10,101, 91),(10,102, 94)
]

cursor.executemany("INSERT INTO students VALUES (?,?,?,?)", students_data)
cursor.executemany("INSERT INTO subjects VALUES (?,?,?)", subjects_data)
cursor.executemany("INSERT INTO marks VALUES (?,?,?)", marks_data)

conn.commit()

# -----------------------------
# 3. JOIN Strategy
# -----------------------------
query = """
SELECT s.student_id, s.name, s.department, sub.subject_name, m.marks
FROM students s
JOIN marks m ON s.student_id = m.student_id
JOIN subjects sub ON m.subject_id = sub.subject_id
"""
df = pd.read_sql_query(query, conn)

print("\n--- Joined Data ---")
print(df)

# -----------------------------
# 4. Statistical Calculations
# -----------------------------
mean_marks = df['marks'].mean()
count_marks = df['marks'].count()
variance_marks = df['marks'].var()
std_marks = df['marks'].std()

print("\n--- Overall Statistics ---")
print("Mean:", mean_marks)
print("Count:", count_marks)
print("Variance:", variance_marks)
print("Standard Deviation:", std_marks)

# -----------------------------
# 5. Top 5% Students (by Average)
# -----------------------------
student_avg = df.groupby(['student_id','name'])['marks'].mean().reset_index()
student_avg = student_avg.sort_values(by='marks', ascending=False)

top_5_percent_count = max(1, int(len(student_avg) * 0.05))
top_students = student_avg.head(top_5_percent_count)

print("\n--- Top 5% Students ---")
print(top_students)

# -----------------------------
# 6. Abnormal Performance (Z-score)
# -----------------------------
df['z_score'] = (df['marks'] - mean_marks) / std_marks
outliers = df[np.abs(df['z_score']) > 2]

print("\n--- Abnormal Performance (|Z| > 2) ---")
print(outliers[['student_id','name','marks','z_score']])

# -----------------------------
# 7. Compare Distribution by Department
# -----------------------------
dept_stats = df.groupby('department')['marks'].agg(
    mean='mean',
    count='count',
    variance='var',
    std_dev='std'
).reset_index()

print("\n--- Department Comparison ---")
print(dept_stats)

conn.close()
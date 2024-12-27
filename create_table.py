import sqlite3

# Connect to database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create interviews table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_name TEXT NOT NULL,
    company_name TEXT NOT NULL,
    application_date TEXT NOT NULL,
    status TEXT,
    notes TEXT
)
""")

conn.commit()
conn.close()


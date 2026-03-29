import sqlite3

conn = sqlite3.connect("database/sales.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    region TEXT,
    category TEXT,
    sales REAL
)
""")

# Insert sample data
cursor.execute("DELETE FROM sales")  # clear old data

cursor.executemany("""
INSERT INTO sales (product, region, category, sales)
VALUES (?, ?, ?, ?)
""", [
    ("Laptop", "North", "Electronics", 50000),
    ("Phone", "South", "Electronics", 30000),
    ("Shirt", "East", "Clothing", 10000),
    ("Shoes", "West", "Clothing", 15000),
    ("Tablet", "North", "Electronics", 20000)
])

conn.commit()
conn.close()

print("✅ Database ready!")

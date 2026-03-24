import sqlite3

conn = sqlite3.connect("store.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()

print("📦 PRODUCTS IN DB:\n")

for r in rows:
    print(r)
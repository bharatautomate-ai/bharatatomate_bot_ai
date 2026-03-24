import sqlite3

conn = sqlite3.connect("store.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO products 
(client_id, name, keywords, price, sizes, stock, location, description, link)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "shop1",
    "White Shoes",
    "shoes,white shoes,sneakers,shoe,white sneaker",
    2499,
    "7,8,9",
    1,
    "Mumbai",
    "Stylish white shoes",
    "https://yourstore.com/shoes"
))

conn.commit()
print("✅ White Shoes Added")
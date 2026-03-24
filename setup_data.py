from database import cursor, conn

# 👉 CLIENT ADD (agar nahi hai to)
cursor.execute("INSERT OR IGNORE INTO clients VALUES (?, ?)", (
    "shop1",
    "17841443287829864"
))

# 👉 PRODUCT ADD
cursor.execute("""
INSERT INTO products 
(client_id, name, keywords, price, sizes, stock, location, description, link)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "shop1",
    "Black Hoodie",
    "hoodie,black hoodie,jacket",
    1999,
    "M,L,XL",
    1,
    "Delhi",
    "Warm hoodie",
    "https://yourstore.com/hoodie"
))

conn.commit()

print("✅ Product Added")

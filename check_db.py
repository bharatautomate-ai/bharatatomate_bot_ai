from database import cursor

cursor.execute("SELECT * FROM clients")
rows = cursor.fetchall()

print(rows)
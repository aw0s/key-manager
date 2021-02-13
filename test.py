import sqlite3

conn = sqlite3.connect("passdb.db")
cursor = conn.cursor()

cursor.execute("""SELECT * FROM keymanager""")
data = cursor.fetchall()
print(data)

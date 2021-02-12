import sqlite3


conn = sqlite3.connect('passdb.db')
cursor = conn.cursor()

cursor.execute("""SELECT * FROM login""")
data = cursor.fetchone()
print(data)

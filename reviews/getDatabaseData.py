import sqlite3

conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()
c.execute("SELECT * FROM users")
print(c.fetchall())

c.execute("SELECT * FROM reviews")
print(c.fetchall())

c.execute("SELECT * FROM reviews_review")
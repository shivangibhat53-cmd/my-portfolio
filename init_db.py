import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE projects (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT,
               description TEXT,
               link TEXT)""")

cursor.execute("INSERT INTO projects(title, description, link) VALUES (?,?,?)",("Portfolio Website", "My Personal portofolio built with Flask","#"))
cursor.execute("INSERT INTO projects(title, description, link) VALUES (?,?,?)",("Todo App","A simple task manager app", "#"))

conn.commit()
conn.close()
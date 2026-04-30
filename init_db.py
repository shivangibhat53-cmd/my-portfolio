import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE projects (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT,
              description TEXT,
              link TEXT,
              image TEXT )""")

#cursor.execute("INSERT INTO projects(title, description, link) VALUES (?,?,?)",("Portfolio Website", "My Personal portofolio built with Flask","#"))
#cursor.execute("INSERT INTO projects(title, description, link) VALUES (?,?,?)",("Todo App","A simple task manager app", "#"))
#cursor.execute("UPDATE projects SET image = 'default.jpg' where image is NULL")
#cursor.execute("DELETE from projects where Id IN (5,6)")
conn.commit()
conn.close()

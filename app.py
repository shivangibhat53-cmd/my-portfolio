from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_projects():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("Select* from projects")
    projects = cursor.fetchall()
    conn.close()
    return projects

@app.route("/")
def home():
    projects = get_projects()
    return render_template("index.html", projects = projects)

@app.route("/projects")
def projects():
    projects = get_projects()
    return render_template("projects.html",projects = projects)

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug = True)
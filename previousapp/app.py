from flask import Flask, render_template, request, redirect
import sqlite3
import os,uuid

app = Flask(__name__)

UPLOAD_FOLDER = 'static\images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_projects():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("Select* from projects")
    projects = cursor.fetchall()
    conn.close()
    return projects

@app.route("/")
def home():
    projects = get_projects()
    return render_template("index.html", projects = projects)

@app.route("/projects", methods = ["GET","POST"])

def projects():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        link = request.form["link"]

        file = request.files.get("image")
        filename = str(uuid.uuid4()) + file.filename  ##using uuid so matching filenames doesnt cause any issue
        filepath = os.path.join(app.config['UPLOAD_FOLDER'],filename)
        if file and file.filename !="":
            file.save(filepath)

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO projects(title,description,link,image)VALUES(?,?,?,?)",(title,description,link,filename))
        conn.commit()
        conn.close()
        return redirect("/projects")
    
    projects = get_projects()
    
    return render_template("projects.html",projects = projects)

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug = True)
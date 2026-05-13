from . import projects
import uuid
from pathlib import Path

from flask import render_template, request, current_app, redirect, url_for, flash
from werkzeug.utils import secure_filename
from  app.extensions import db
from app.models import Project
from flask_login import current_user


ALLOWED_EXTENSIONS = {'.png','.jpg','.jpeg','.gif'}

def allowed_file_extension(filename):
    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS  #Pathclass used to get file extension using its method suffix

@projects.route("/", methods = ["GET","POST"])

def project_page():
    if request.method == "POST":
        if not current_user.is_authenticated:
            return redirect(url_for("auth.login"))
        print("Form Submitted")
        title = request.form.get("title")
        print("TITLE: ",title)
        if not title:
            flash("Project title is required","error")
            return redirect(request.url)
        
        description = request.form.get("description")
        print("DESCRIPTION: ",description)
        if not description:
            flash("Project description is required","error")
            return redirect(request.url)
        
        file = request.files.get("image")
        filename = "default.jpg"

        if file and file.filename:
            if allowed_file_extension(file.filename):
                ext = Path(file.filename).suffix.lower()
                filename = f"{uuid.uuid4().hex}{ext}"
                print("FILENAME: ", filename)

                upload_folder = Path(current_app.root_path)/"static"/"uploads"
                upload_folder.mkdir(parents = True, exist_ok = True)
                file.save(upload_folder/filename)
 
            else:
                flash("Invalid file type. Only PNG,JPG, and GIF are allowed","error")
                return redirect(request.url)
        gitlink = request.form.get("repolink")
        tech_stack = request.form.get("tech_stack")
            
        try:
            new_project = Project(title=title, description = description, image = filename, gitlink = gitlink, tech_stack = tech_stack) 
            db.session.add(new_project)
            print("ADDED TO SESSION")
            db.session.commit()
            print("PROJECT SAVED")
            flash("Project added successfully!", "success")
        except Exception as e:
            db.session.rollback()
            flash("An error occurred while saving to the database","error")


        return redirect(url_for("projects.project_page"))

    projects = Project.query.all()
    print(projects)
    return render_template('projects/projects.html', projects= projects)


@projects.route("/<int:project_id>")
def project_detail(project_id):

    project = Project.query.get_or_404(project_id)

    return render_template("projects/project_detail.html", project= project)
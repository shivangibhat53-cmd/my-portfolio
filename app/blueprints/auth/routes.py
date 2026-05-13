from  flask import render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash

from flask_login import login_user, logout_user, login_required

from . import auth_bp

from app.models import User


@auth_bp.route("/login", methods = ["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)

            return redirect(url_for("projects.project_page"))
        
        flash("Invalid credentials")
    
    return render_template("auth/login.html")

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()

    return redirect(url_for("main.home"))
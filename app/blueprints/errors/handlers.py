from . import errors
from flask import render_template

@errors.app_errorhandler(404)
def error_404(error):
    return render_template("errors/404.html"),404

@errors.app_errorhandler(500)
def error_500(error):
    return render_template("errors/500.html",500)
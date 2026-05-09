from flask import Flask



def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)

    app.config.from_object(config_class)

    from .extensions import init_extensions, db
    init_extensions(app)

    from app.models import Project

    with app.app_context():
        db.create_all()
      
    
    from .blueprints.main import main
    from .blueprints.errors import errors
    from .blueprints.projects import projects 
    

    app.register_blueprint(main)
    app.register_blueprint(projects, url_prefix = "/projects")
    app.register_blueprint(errors)

    return app
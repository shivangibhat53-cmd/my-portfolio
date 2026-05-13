from flask import Flask
from app.models import Project
from app.models import User



def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)

    app.config.from_object(config_class)

    from .extensions import init_extensions, db, login_manager
    init_extensions(app)
    

    with app.app_context():
        db.create_all()
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from .blueprints.main import main
    from .blueprints.errors import errors
    from .blueprints.projects import projects
    from .blueprints.auth import auth_bp
    

    app.register_blueprint(main)
    app.register_blueprint(projects, url_prefix = "/projects")
    app.register_blueprint(errors)
    app.register_blueprint(auth_bp)

    return app
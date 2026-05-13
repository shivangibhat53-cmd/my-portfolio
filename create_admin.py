from werkzeug.security import generate_password_hash

from app import create_app
from app.extensions import db
from app.models import User


app = create_app()

with app.app_context():
    admin = User(
        username = "admin",
        password = generate_password_hash("admin123")
    )

    db.session.add(admin)
    db.session.commit()
    print("ADMIN CREATED")

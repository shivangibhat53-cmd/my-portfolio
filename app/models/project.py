from app.extensions import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable= False)
    description = db.Column(db.Text, nullable = False)
    gitlink = db.Column(db.String(400))
    tech_stack = db.Column(db.String(300))
    image = db.Column(db.String(200))


    def __repr__(self):
        return f"<Project {self.title}>"

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    tag = db.Column(db.String(50), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200), nullable=False)
    link = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f'<Article {self.title}>'

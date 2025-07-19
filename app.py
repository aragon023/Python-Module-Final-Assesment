from flask import Flask, render_template
from project_data import projects_list # This imports the projects list
from articles_data import db, Article
import random


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html", projects=projects_list)

@app.route("/tools")
def tools():
    return render_template("tools.html")

@app.route("/articles")
def articles():
    articles_list = Article.query.all()
    return render_template("articles.html", articles=articles_list)

@app.route('/')
def home():
    all_articles = Article.query.all()
    featured_articles = random.sample(all_articles, min(3, len(all_articles)))
    return render_template("index.html", featured_articles=featured_articles)

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

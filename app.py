from flask import Flask, render_template
from project_data import projects_list # This imports the projects list


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=projects_list)

@app.route("/tools")
def tools():
    return render_template("tools.html")

@app.route("/articles")
def articles():
    return render_template("articles.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

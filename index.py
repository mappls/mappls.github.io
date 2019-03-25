
from flask import Flask, render_template
from flask_frozen import Freezer
import json
import sys

app = Flask(__name__)
freezer = Freezer(app)


def get_projects_json(filepath="static/projects/projects.json"):
    with open(filepath, "r") as file:
        pl = json.load(file)
    return pl


@app.route('/')
def get_index():
    pl = get_projects_json()
    return render_template('projects.html', projects=pl)


@app.route('/projects')
def get_projects():
    pl = get_projects_json()
    return render_template('projects.html', projects=pl)


@app.route('/research')
def get_research():
    return "Research"


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Use with 'run' or 'build' argument,")
    if sys.argv[1] == 'run':
        app.run(debug=True)
    elif sys.argv[1] == 'build':
        freezer.freeze()

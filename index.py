
from flask import Flask, render_template
import json

app = Flask(__name__)


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

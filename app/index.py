
from flask import Flask, render_template
from flask_frozen import Freezer
import json
import sys
import os

app = Flask(__name__)
app.config['FREEZER_DESTINATION'] = '../build'
freezer = Freezer(app)


def get_projects_json(filepath="static/projects/projects.json"):
    with open(filepath, "r") as file:
        pl = json.load(file)
    return pl


def get_project_descriptions(title):

    # Get short and long description files
    files = os.listdir("static/projects/")
    mds_short = [file for file in files if file[-9:] == "-short.md"]
    mds_long = [file for file in files if file[-8:] == "-long.md"]

    short = None
    long = None

    for filename in mds_short:
        if title in filename:
            with open("static/projects/%s" % filename) as file:
                short = file.read()

    for filename in mds_long:
        if title in filename:
            with open("static/projects/%s" % filename) as file:
                long = file.read()

    return long, short


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


@app.route('/project/<string:title>')
def get_project(title):
    project = {}
    pl = get_projects_json()
    for p in pl:
        if p['title'] == title:
            project = p
            break

    ldesc, sdesc = get_project_descriptions(title)
    project['sdesc'] = sdesc
    project['ldesc'] = ldesc
    return render_template('project.html', project=project)


@freezer.register_generator
def projects_generator():
    pl = get_projects_json()
    for p in pl:
        yield "/project/%s" % p['title']


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Use with 'run' or 'build' argument,")
    if sys.argv[1] == 'run':
        app.run(debug=True)
    elif sys.argv[1] == 'build':
        freezer.freeze()

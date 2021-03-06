
from flask import Flask, render_template, Markup
from flask_frozen import Freezer
from markdown import markdown
import shutil
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
    projects = []
    pl = get_projects_json()
    for p in pl:
        ldesc, sdesc = get_project_descriptions(p['title'])
        p['sdesc'] = Markup(markdown(sdesc))
        p['ldesc'] = Markup(markdown(ldesc))
        projects.append(p)
    return render_template('projects.html', projects=pl)


@app.route('/projects', methods=['GET', 'POST'])
def get_projects():
    projects = []
    pl = get_projects_json()
    for p in pl:
        ldesc, sdesc = get_project_descriptions(p['title'])
        p['sdesc'] = Markup(markdown(sdesc))
        p['ldesc'] = Markup(markdown(ldesc))
        projects.append(p)

    return render_template('projects.html', projects=pl)


@app.route('/research', methods=['GET', 'POST'])
def get_research():
    with open('static/research/research.md') as file:
        research = file.read()
        research = Markup(markdown(research))
    return render_template('research.html', research=research)


@app.route('/bio', methods=['GET', 'POST'])
def get_bio():
    return render_template('bio.html')


@app.route('/project/<string:title>', methods=['GET', 'POST'])
def get_project(title):
    project = {}
    pl = get_projects_json()
    for p in pl:
        if p['title'] == title:
            project = p
            break

    print('** title', title)
    ldesc, sdesc = get_project_descriptions(title)
    project['sdesc'] = Markup(markdown(sdesc))
    project['ldesc'] = Markup(markdown(ldesc))
    return render_template('project.html', project=project)


@freezer.register_generator
def projects_generator():
    pl = get_projects_json()
    for p in pl:
        yield "/project/%s" % p['title']


def copytree(src, dst, symlinks=False):

    # Remove old files
    for item in os.listdir(src):
        if item in os.listdir(dst):
            try:
                os.remove(dst + "/" + item)
            except PermissionError:
                shutil.rmtree(os.path.join(dst, item))

    # Copy all files
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.move(s, d, symlinks)
        else:
            shutil.copy2(s, d)

    for file in ['../projects', '../research', '../bio', '../project/chatbot-sam', '../project/dl-group',
                 '../project/learnbet', '../project/nlp-chunks', '../project/playfield', '../project/trenddays',
                 '../project/trendmatch recommender']:
        if os.path.isfile(file):
            os.rename(file, file + '.html')

    shutil.rmtree(src)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Use with 'run' or 'build' argument,")
    if sys.argv[1] == 'run':
        app.run(debug=True)
    elif sys.argv[1] == 'build':
        freezer.freeze()

        # Copy all files from build to root folder
        copytree(src=app.config['FREEZER_DESTINATION'], dst="..")

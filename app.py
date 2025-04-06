from os import path
from pathlib import Path

from flask import Flask, render_template
from flask_frozen import Freezer


template_folder = path.abspath('./wiki')

app = Flask(__name__, template_folder=template_folder)
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
freezer = Freezer(app)

# Basic config for flask_frozen
@app.cli.command()
def freeze():
    freezer.freeze()

@app.cli.command()
def serve():
    freezer.run()

# Add the routing for the pages here
@app.route('/')
def home():
    return render_template('index.html')

# Important: remember to add the tailing slash!
@app.route('/pages/<name>/')
def pages(name):
    return render_template(f'pages/{name}.html')
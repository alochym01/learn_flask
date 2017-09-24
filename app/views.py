from app import app
from flask import render_template, request


@app.route('/')
def index():
    return 'Home Page'


@app.route('/home')
def homepage():
    name = request.args.get('name')
    if not name:
        name = '<unknown>'
    return render_template('homepage.html', name=name)

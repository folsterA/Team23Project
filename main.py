'''
Name: Austin Folster
email: folstera@csumb.edu
desc: This is the main python script for running the website and handling redirects 
and templates
'''

from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm

app = Flask(__name__)
bootstrap = Bootstrap(app)

class Recipe(FlaskForm):
    pass

@app.route('/') # index
def index():
    return render_template('index.html')

@app.route('/search') # search
def search():
    return render_template('search.html')

@app.route('/submit') #submit
def submit():
    return render_template('submit.html')
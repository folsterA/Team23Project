'''
Name: Austin Folster
email: folstera@csumb.edu
desc: This is the main python script for running the website and handling redirects 
and templates
'''

from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from image_info import image_info

app = Flask(__name__)
bootstrap = Bootstrap(app)

class Recipe(FlaskForm):
    pass

class Search(FlaskForm):
    search_string = StringField(
        'Search Term', 
        validators=[DataRequired()]
    )

search_term = ""
search_list = 

@app.route('/', methods=('GET', 'POST')) # index
def index():
    form = Search()
    if form.validate_on_submit():
        search_term = form.search_string.data.lower()
        return redirect('/view_playlist')
    return render_template('index.html')

@app.route('/search') # search
def search():
    for i in image_info:
        for k in search_term:
            if (k in i['title'].lower()) or (k in i['tags'].lower()):
                search_list.append(i)
            break

    return render_template('search.html', data = search_list, term = search_term)

@app.route('/submit') #submit
def submit():
    return render_template('submit.html')

@app.route('/recipes/<recipe_name>') # search
def recipe(recipe_name):
    for i in image_info:
        if i['recipeName'] == recipe_name:
            data = i
    return render_template('search.html', data = data, recipe_name = recipe_name)
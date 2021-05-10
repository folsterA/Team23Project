'''
Name: Austin Folster
email: folstera@csumb.edu
desc: This is the main python script for running the website and handling redirects 
and templates
'''

from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from Recipes import Recipes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'team23'
bootstrap = Bootstrap(app)

class Recipe_Search(FlaskForm):
    recipe_keyword = StringField('Search Recipes:', validators = [DataRequired()])

class Recipe_Edit(FlaskForm):
    name = StringField("Recipe Name: ", validators = [DataRequired()])
    user_name = StringField("Submitted by User: ", validators = [DataRequired()])
    ingredients = StringField("Ingredient??: ", validators = [DataRequired()])
    ethnicity = StringField("Where it's from: ", validators = [DataRequired()])
    tags = StringField("Tags (separate by commas): ", validators = [DataRequired()])
    instructions = StringField("Instructions: ", validators = [DataRequired()])
    imageURL = StringField("Instructions: ", validators = [DataRequired()])


@app.route('/', methods=('GET', 'POST')) # index
def index():
    form = Recipe_Search()
    if form.validate_on_submit():
        return redirect('/search', form.recipe_keyword)
    return render_template('index.html', form = form)

@app.route('/search') # 
def search(keyword):
    return render_template('search.html', keyword = keyword)

@app.route('/submit') #submit
def submit():
    form = Recipe_Edit()
    if form.validate_on_submit():
        pass
    return render_template('submit.html')

@app.route('/recipe/<name>')
def recipe(name):
    for recipe in Recipes:
        if (recipe["recipeName"] == name):
            return render_template("recipe.html", name = name)
'''
Name: Austin Folster
email: folstera@csumb.edu
desc: This is the main python script for running the website and handling redirects 
and templates
'''
import json
from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from Recipes import Recipes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'team23'
bootstrap = Bootstrap(app)

recipes = Recipes

class Recipe_Search(FlaskForm):
    recipe_keyword = StringField('Search Recipes:', validators = [DataRequired()])

class Recipe_Edit(FlaskForm):
    name = StringField("Recipe Name: ", validators = [DataRequired()])
    user_name = StringField("Submitted by User: ", validators = [DataRequired()])
    ingredients = StringField("Ingredient: ", validators = [DataRequired()])
    ethnicity = StringField("Where it's from: ", validators = [DataRequired()])
    tags = StringField("Tags (separate by commas): ", validators = [DataRequired()])
    instructions = StringField("Instructions: ", validators = [DataRequired()])
    imageURL = StringField("Instructions: ", validators = [DataRequired()])

@app.route('/', methods=('GET', 'POST')) # index
def index():
    print(recipes)
    form = Recipe_Search()
    if form.validate_on_submit():
        keyword = form.recipe_keyword.data
        return redirect(f'/search/{keyword}')
    return render_template('index.html', form = form)

@app.route('/search/<keyword>') # search
def search(keyword):
    list = []
    for recipe in recipes:
        for term in recipe["recipeName"].split():  
            for key in keyword.split():
                if key.lower() == term.rstrip(',').lower():   
                    if recipe not in list:       
                        list.append(recipe)
        for term in recipe["tags"]:  
            for key in keyword.split():
                if key.lower() == term.lower():   
                    if recipe not in list:       
                        list.append(recipe)
    
    return render_template('search.html', keyword = keyword, data = list)

@app.route('/submit', methods=('GET', 'POST')) #submit
def submit():
    form = Recipe_Edit()
    if form.validate_on_submit():
        recipe = {}
        recipe["recipeName"].append(form.name)
        recipe["userName"].append(form.user_name)
        recipe["ingredients"].append(form.ingredients.split(", "))
        recipe["tags"].append(form.tags.split(", "))
        recipe["instructions"].append(form.instructions)
        recipe["urlFor"].append(form.imageURL)
        recipes.append(recipe)
    return render_template('submit.html', form=form)

@app.route('/recipe/<name>')
def recipe(name):
    for recipe in recipes:
        if (recipe["recipeName"] == name):
            return render_template("recipe.html", name = name, data = recipe)
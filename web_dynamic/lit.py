#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.species import Species
from os import environ
from flask import Flask, render_template
import uuid
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

@app.route('/', strict_slashes=False)
def home():
    """ Serves Homepage """
    return render_template('home.html')

@app.route('/root', strict_slashes=False)
def root():
    """ Serves main Root veg page """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    
    
    return render_template('root_dynamic.html',
                           species=species,
                           cache_id=uuid.uuid4())

@app.route('/flower', strict_slashes=False)
def flower():
    """ Serves main Flower page """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    
    
    return render_template('flower_dynamic.html',
                           species=species,
                           cache_id=uuid.uuid4())

@app.route('/leaf', strict_slashes=False)
def leaf():
    """ Serves main leaf page """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    
    
    return render_template('leaves_dynamic.html',
                           species=species,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

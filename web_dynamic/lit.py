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


@app.route('/root', strict_slashes=False)
def lit():
    """ LIT is alive! """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    
    
    return render_template('root_dynamic.html',
                           species=species,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

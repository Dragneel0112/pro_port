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


@app.route('/root/beetroot', strict_slashes=False)
def beetroot():
    """ Serves beetroot species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "45fd1960-a903-40d8-9729-92b928242f1d"
    image = "Beetroot.jpg"

    return render_template('root_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/root/garlic', strict_slashes=False)
def garlic():
    """ Serves garlic species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "6a8ba1ef-aa3b-4052-9402-07fc1230da99"
    image = "Garlic.jpeg"

    return render_template('root_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/root/ginger', strict_slashes=False)
def ginger():
    """ Serves ginger species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "d0d3f396-22aa-441f-8612-ebf96c0dfd6a"
    image = "Ginger.jpeg"

    return render_template('root_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/root/onions', strict_slashes=False)
def onions():
    """ Serves onion species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "e63ae9fe-dba1-4ec0-aad0-325ef1aee6ae"
    image = "Onion.jpg"

    return render_template('root_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/root/parsnip', strict_slashes=False)
def parsnip():
    """ Serves parsnip species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "2c278749-cd36-4c45-aa32-9866804ab9fb"
    image = "Parsnips.jpeg"

    return render_template('root_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/root/potato', strict_slashes=False)
def potato():
    """ Serves potato species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "4b2525e8-e596-467b-acd5-6a3e86b23404"
    image = "Potato.jpeg"

    return render_template('root_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/root/radish', strict_slashes=False)
def radish():
    """ Serves radish species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "d5339455-ff63-41c7-a59b-e6488925ebb1"
    image = "Radish.jpeg"

    return render_template('root_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/root/sweetpotato', strict_slashes=False)
def Sweet_potato():
    """ Serves Sweet Potato species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "a6c1d812-6e91-4e64-8290-392e6abee6b1"
    image = "Sweet Potato.jpeg"

    return render_template('root_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/root/taro', strict_slashes=False)
def taro():
    """ Serves Taro species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "d03217c1-12bd-4644-924c-b044e6de1797"
    image = "Taro.jpg"

    return render_template('root_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/root/turnip', strict_slashes=False)
def turnip():
    """ Serves Turnip species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "2faa83f6-ac97-4e1d-b8de-806099d65e6a"
    image = "Turnip.jpeg"

    return render_template('root_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

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


@app.route('/leaf/bokchoy', strict_slashes=False)
def Bok_Choy():
    """ Serves Bok Choy species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "0a914435-205c-4d1f-83cc-e2656d84b2ac"
    image = "Bok Choy.jpeg"

    return render_template('leaf_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/leaf/broccoli', strict_slashes=False)
def Broccoli():
    """ Serves Broccoli species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "10210da4-0a3b-4131-bbd8-af145607b3f0"
    image = "Broccoli.jpeg"

    return render_template('leaf_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/leaf/cabbage', strict_slashes=False)
def Cabbage():
    """ Serves Cabbage species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "24817cd6-dbfe-43fd-ac25-ebc02ae78018"
    image = "cabbage.jpeg"

    return render_template('leaf_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/leaf/collardgreen', strict_slashes=False)
def Collard_greens():
    """ Serves Collard greens species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "289220a2-84dd-4a3d-adb9-ef89712889e0"
    image = "Collard green.jpeg"

    return render_template('leaf_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/leaf/kale', strict_slashes=False)
def Kale():
    """ Serves kale species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "36d9c87a-3f5f-4f75-b610-eb69131c89fc"
    image = "Kale.jpeg"

    return render_template('leaf_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/leaf/lettuce', strict_slashes=False)
def Lettuce():
    """ Serves Lettuce species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "1f7589d4-8614-4d71-b943-dc43cd1c1523"
    image = "Lettuce.jpeg"

    return render_template('leaf_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/leaf/mustardgreens', strict_slashes=False)
def Mustard_green():
    """ Serves Mustard Green species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "eefc9cec-6eab-4220-b61d-c5d7c8c63b5e"
    image = "Mustard greens.jpeg"

    return render_template('leaf_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/leaf/rocket', strict_slashes=False)
def Rocket():
    """ Serves Rocket species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "fdfe5ebb-33d1-49a6-8fa2-ce2ac5307227"
    image = "Rocket.jpeg"

    return render_template('leaf_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/leaf/spinach', strict_slashes=False)
def Spinach():
    """ Serves Spinach species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "c3670013-b114-4b14-9076-6079bc0d01a2"
    image = "Spinach.jpeg"

    return render_template('leaf_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/leaf/watercress', strict_slashes=False)
def Watercress():
    """ Serves Watercress species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "38d07752-972a-4d6c-ad3b-75951f62bb63"
    image = "Watercress.jpeg"

    return render_template('leaf_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/flower/carnation', strict_slashes=False)
def Carnation():
    """ Serves Carnations species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "9226f25f-78ab-449f-b2db-600d8a1fa79a"
    image = "Carnations.jpeg"

    return render_template('flower_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/flower/daisy', strict_slashes=False)
def Daisy():
    """ Serves Daisy species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "a2fb989e-39ed-4438-8af0-6a1681e66823"
    image = "Daisy.jpeg"

    return render_template('flower_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/flower/hydrangea', strict_slashes=False)
def Hydrangea():
    """ Serves Hydrangea species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "217c575f-04b5-419a-83a2-a9d5b7b85484"
    image = "Hydrangea.jpeg"

    return render_template('flower_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/flower/lilac', strict_slashes=False)
def Lilac():
    """ Serves lilac species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "b5170399-305c-47aa-ac7f-15de29d7a057"
    image = "Lilac.jpeg"

    return render_template('flower_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/flower/lilly', strict_slashes=False)
def Lilly():
    """ Serves lilly species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "c5ff3c3c-b65e-420b-9661-d7b8597707ca"
    image = "Lilly.jpeg"

    return render_template('flower_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/flower/marigold', strict_slashes=False)
def Marigold():
    """ Serves Marigold species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "c707a85c-b344-438b-b986-42f18c5a6899"
    image = "Marigold.jpg"

    return render_template('flower_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/flower/orchid', strict_slashes=False)
def Orchid():
    """ Serves Orchid species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "7f307d6a-b2db-4d55-b9f4-b7b34cb0b951"
    image = "Orchid.jpeg"

    return render_template('flower_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/flower/rose', strict_slashes=False)
def Rose():
    """ Serves Rose species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "fc1fe744-065d-4b38-8cde-71241d1e878d"
    image = "Rose.jpeg"

    return render_template('flower_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/flower/sunflower', strict_slashes=False)
def Sunflower():
    """ Serves Sunflower species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "0f1c9c52-b40b-41ff-8079-f86240a90e73"
    image = "Sunflower.jpeg"

    return render_template('flower_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


@app.route('/flower/tulip', strict_slashes=False)
def Tulip():
    """ Serves Tulip species """
    species = storage.all(Species).values()
    species = sorted(species, key=lambda k: k.name)
    name_id = "569abbe3-9dab-4496-8ecd-2de449b6c38b"
    image = "Tulip.jpg"

    return render_template('flower_sp.html',
                           species=species,
                           name_id=name_id,
                           image=image,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

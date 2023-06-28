#!/usr/bin/python3
""" objects that handle all default RestFul API actions for States """
from models.plants import Plants
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/plants', methods=['GET'], strict_slashes=False)
def get_plants():
    """
    Retrieves the list of all Plant objects
    """
    all_plants = storage.all(Plants).values()
    list_plants = []
    for plants in all_plants:
        list_plants.append(plants.to_dict())
    return jsonify(list_plants)


@app_views.route('/plants/<plant_id>', methods=['GET'], strict_slashes=False)
def get_plant(plant_id):
    """ Retrieves a specific Plant """
    plant = storage.get(Plants, plant_id)
    if not plant:
        abort(404)

    return jsonify(plant.to_dict())

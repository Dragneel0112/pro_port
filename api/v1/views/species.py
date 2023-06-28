#!/usr/bin/python3
""" objects that handles all default RestFul API actions for cities """
from models.species import Species
from models.plants import Plants
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/plants/<plant_id>/species', methods=['GET'],
                 strict_slashes=False)
def get_species(plant_id):
    """
    Retrieves the list of all species
    of a specific Plant
    """
    list_species = []
    plant = storage.get(Plants, plant_id)
    if not plant:
        abort(404)
    for sp in plant.species:
        list_species.append(sp.to_dict())

    return jsonify(list_species)


@app_views.route('/species/<species_id>/', methods=['GET'],
                 strict_slashes=False)
def get_specific_sp(species_id):
    """
    Retrieves a specific species based on id
    """
    sp = storage.get(Species, species_id)
    if not sp:
        abort(404)
    return jsonify(sp.to_dict())

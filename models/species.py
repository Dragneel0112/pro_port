#!/usr/bin/python3
""" City Class"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Species(BaseModel, Base):
    """Representation of city """
    if models.storage_t == "db":
        __tablename__ = 'species'
        plant_id = Column(String(60), ForeignKey('plant.id'), nullable=False)
        name = Column(String(128), nullable=False)
        
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)

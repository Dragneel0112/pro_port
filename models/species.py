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
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        image_url = Column(String(128), nullable=False)
        plant_id = Column(String(60), ForeignKey('plants.id'), nullable=False)

    else:
        name = ""
        text = ""
        image_url = ""
        plant_id = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)

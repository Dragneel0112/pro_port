#!/usr/bin/python3
""" Plant class"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Plants(BaseModel, Base):
    """ Main plants"""
    if models.storage_t == "db":
        __tablename__ = 'plants'
        name = Column(String(128), nullable=False)
        species = relationship("Species",
                              backref="plant",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def species(self):
            """getter for list of species instances related to the plant"""
            sp_list = []
            all_species = models.storage.all(Species)
            for sp in all_species.values():
                if sp.plant_id == self.id:
                    sp_list.append(sp)
            return sp_list

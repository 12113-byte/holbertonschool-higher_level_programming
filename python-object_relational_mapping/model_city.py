#!/usr/bin/python3
"""Contains class definition of a City and an instance Base - state model"""
#  importing dependencies
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """City class linked to mysql cities table"""
    __tablename__ = 'cities'
    id = Column(
        Integer, primary_key=True, nullable=False, autoincrement=True
    )
    state_id = Column(
        Integer, ForeignKey('states.id'), nullable=False
        )
    name = Column(String(128), nullable=False)

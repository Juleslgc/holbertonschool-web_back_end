#!/usr/bin/env python3
"""
This module provides a function to insert a new document
into a MongoDB collection using PyMongo.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a single document into the given MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection):
            The MongoDB collection where the document will be inserted.
        **kwargs:
            Arbitrary keyword arguments representing the document fields
            and their corresponding values. For example:
            name="UCSF", address="505 Parnassus Ave"

    Returns:
        ObjectId: The unique identifier (_id) of the inserted document.
    """
    new_insert = mongo_collection.insert_one(kwargs)
    return new_insert.inserted_id

#!/usr/bin/env python3
"""
This script defines a function to list all documents from a MongoDB collection
using PyMongo. It returns an empty list if the collection has no documents.
"""


def list_all(mongo_collection):
    """
    Return a list of all documents in a MongoDB collection.
    If the collection is empty, returns an empty list.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The collection to query.

    Returns:
        list: A list of documents (dicts) from the collection.
    """
    new_list = list(mongo_collection.find())
    return new_list

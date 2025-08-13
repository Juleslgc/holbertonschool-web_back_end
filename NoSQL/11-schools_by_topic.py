#!/usr/bin/env python3
"""
This module defines a function to find schools by a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieve all school documents that include a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection to query.
        topic (str): The topic to search for in the
        'topics' field of each document.

    Returns:
        list: A list of documents (dicts) where
        'topics' contains the specified topic.
    """
    doc = mongo_collection.find({"name": topic})
    return list(doc)

#!/usr/bin/env python3

"""
Module: my_module
Description: Example module for demonstration
"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection based on keyword arguments.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo collection object.
        **kwargs: Keyword arguments representing the fields and values for the new document.

    Returns:
        str: The _id of the newly inserted document.
    """
    new_document = kwargs
    result = mongo_collection.insert_one(new_document)
    new_id = result.inserted_id
    return str(new_id)

if __name__ == "__main__":
    my_collection = None  # Replace with your actual PyMongo collection object
    document_data = {"name": "Holberton School", "location": "San Francisco"}
    new_id = insert_school(my_collection, **document_data)
    print(new_id)


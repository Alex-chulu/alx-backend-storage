#!/usr/bin/env python3
"""a Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo collection object.

    Returns:
        list: A list containing all the documents in the collection.
              Returns an empty list if there are no documents.
    """
    documents = list(mongo_collection.find())
    return documents

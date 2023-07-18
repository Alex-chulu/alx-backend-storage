#!/usr/bin/env python3

"""
Module: my_module
Description: Example module for demonstration
"""

from pymongo import MongoClient

def top_students(mongo_collection):
    """
    Returns all students sorted by average score from a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo collection object.

    Returns:
        list: A list of dictionaries representing the top students sorted by average score.
              Each student dictionary includes the "averageScore" key with the calculated average score.
    """
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])

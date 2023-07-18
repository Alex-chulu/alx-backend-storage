#!/usr/bin/env python3

"""
Module: my_module
Description: Example module for demonstration
"""

from typing import List
from pymongo import MongoClient

def update_topics(mongo_collection, name: str, topics: List[str]):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo collection object.
        name (str): The name of the school to update.
        topics (List[str]): The list of topics to replace the existing topics.

    Returns:
        None
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

if __name__ == "__main__":
    school_collection = None
    school_name = "Holberton School"
    new_topics = ["Sys admin", "AI", "Algorithm"]
    update_topics(my_collection, school_name, new_topics)


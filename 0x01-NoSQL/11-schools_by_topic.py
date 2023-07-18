#!/usr/bin/env python3

"""
Module: my_module
Description: Example module for demonstration
"""


from typing import List
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic: str) -> List[dict]:
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo collection object.
        topic (str): The topic to search for.

    Returns:
        List[dict]: A list of dictionaries representing the schools having the specific topic.
    """
    schools = list(mongo_collection.find({"topics": topic}))
    return schools

if __name__ == "__main__":
    school_collection = None
    search_topic = "Python"
    result = schools_by_topic(school_collection, search_topic)
    print(result)


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
    students = list(mongo_collection.find())

    # Calculate the average score for each student
    for student in students:
        scores = student.get("scores", [])
        total_scores = len(scores)
        sum_scores = sum(score.get("score", 0) for score in scores)
        average_score = sum_scores / total_scores if total_scores > 0 else 0
        student["averageScore"] = average_score

    # Sort students by average score in descending order
    sorted_students = sorted(students, key=lambda x: x["averageScore"], reverse=True)
    return sorted_students

if __name__ == "__main__":
    client = MongoClient()
    db = client.my_db
    students_collection = db.students

    result = top_students(collection)
    for student in result:
        print(student)


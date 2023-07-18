#!/usr/bin/env python3

"""
Module: 12-log_stats
Description: Script to provide statistics about Nginx logs stored in MongoDB
"""


import pymongo
from pymongo import MongoClient


def get_nginx_logs_stats():
    """
    Retrieves and displays statistics about Nginx logs stored in MongoDB.

    Returns:
        None
    """
    # Connect to MongoDB
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    # Get the number of documents in the collection
    num_logs = collection.count_documents({})
    print(f"{num_logs} logs where {num_logs} is the number of documents in this collection")

    # Get the count of different HTTP methods
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    methods_stats = [collection.count_documents({"method": method}) for method in http_methods]
    print("Methods:")
    for method, count in zip(http_methods, methods_stats):
        print(f"\t{count} documents with method={method}")

    # Get the count of logs with specific method and path
    specific_logs_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"1 document with method=GET, path=/status")

    # Get the top 10 most frequent IPs
    top_ips = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    print("Top 10 IPs:")
    for i, ip_data in enumerate(top_ips, start=1):
        ip = ip_data["_id"]
        count = ip_data["count"]
        print(f"{i}. {ip}: {count} occurrences")

if __name__ == "__main__":
    get_nginx_logs_stats()


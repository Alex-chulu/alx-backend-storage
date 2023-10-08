#!/usr/bin/env python3
"""Script to provide stats about Nginx logs stored in MongoDB."""

from typing import List
from pymongo import MongoClient

def print_stats(collection):
    """Print statistics about Nginx logs."""
    total_logs = collection.count_documents({})

    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"    method {method}: {method_count}")

    status_check_count = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client.logs
    collection = db.nginx

    print_stats(collection)


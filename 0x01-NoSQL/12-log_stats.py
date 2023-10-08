#!/usr/bin/env python3
'''Analyzes Nginx request logs stored in MongoDB and prints statistics.
'''
from pymongo import MongoClient

def print_nginx_request_logs(nginx_collection):
    '''Prints statistics about Nginx request logs.
    '''
    # Count the total number of logs
    log_count = nginx_collection.count_documents({})
    print(f'Total logs: {log_count}')

    # Count logs for each HTTP method (GET, POST, PUT, PATCH, DELETE)
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print('HTTP Methods:')
    for method in methods:
        method_count = nginx_collection.count_documents({'method': method})
        print(f'{method}: {method_count}')

    # Count status check logs
    status_check_count = nginx_collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f'Status check logs: {status_check_count}')

def run():
    '''Connects to MongoDB, retrieves Nginx logs, and prints statistics.
    '''
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Retrieve Nginx logs collection
    nginx_collection = client.logs.nginx

    # Analyze and print statistics for Nginx logs
    print_nginx_request_logs(nginx_collection)

if __name__ == '__main__':
    run()


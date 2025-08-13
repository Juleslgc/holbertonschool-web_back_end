#!/usr/bin/env python3
""" Script that provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')  # Connecting to MongoDB

    # Select the db and the collection
    db = client.logs
    collection_nginx = db.nginx

    count_logs = collection_nginx.count_documents({})
    print("{} logs".format(count_logs))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for method in methods:
        count_method = collection_nginx.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count_method))

    count_doc = collection_nginx.count_documents(
        {"method": "GET", "path": "/status"})
    print("{} status check".format(count_doc))

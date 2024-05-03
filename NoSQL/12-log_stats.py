#!/usr/bin/env python3
"""Write a Python script that provides some stats
about Nginx logs stored in MongoDB
"""



from pymongo import MongoClient


if __name__ == "__main__":
    """provides stats about Nginx logs """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    count = collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{count} logs")
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    stats = collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{stats} status check")

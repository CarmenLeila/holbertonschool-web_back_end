#!/usr/bin/env python3
""" function returns the list of school having a specific topic """


def schools_by_topic(mongo_collection, topics):
    """return the list of school having a specific topic"""
    return mongo_collection.find({"topics": topics})

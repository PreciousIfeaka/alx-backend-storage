#!/usr/bin/env python3
"""
this module contains a function that returns the list of school having
 a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    '''this function finds schools by topic'''
    return mongo_collection.find({"topics": {"$in": [topic]}})

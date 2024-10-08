#!/usr/bin/env python3
""" Write a Python function that inserts a new document in a
    collection based on kwarg
"""


def insert_school(mongo_collection, **kwargs):
    """insert docs"""
    new_school = kwargs
    result = mongo_collection.insert_one(new_school)
    return result.inserted_id
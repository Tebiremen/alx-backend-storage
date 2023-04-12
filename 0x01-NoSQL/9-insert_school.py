#!/usr/bin/env python3
''' Python documents'''



def insert_school(mongo_collection, **kwargs):
    ''' Inserts a new document in Python collection'''

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

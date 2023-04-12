#!/usr/bin/env python3
''' List all documents'''



def list_all(mongo_collection):
    ''' In a collection, list all documents'''

    return [doc for doc in mongo_collection.find()]

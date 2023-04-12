#!/usr/bin/env python3
''' School topics changed'''



def update_topics(mongo_collection, name, topics):
    ''' Base on name collections, all documents are changed'''

    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )

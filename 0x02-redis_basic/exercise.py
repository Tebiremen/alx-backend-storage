#!/usr/bin/env python3
''' The method should generate a random key'''

import uuid import uuid4
import redis
from typing import union, callable, optional
from functools import wraps


UnionOfTypes = Union[str, bytes, int, float]


class Cache:
    ''' follow up the number of calls made to a method in a Cache class'''

     def __init__(self):
         ''' Gather the given method after incrementing the call counter'''
         self._redis = redis.Redis()
         self._redis.flushdb()

         def store(self, data: UnionOfTypes) -> str:
             '''After storing its inputs and output, return the method output.
             '''
             self._key = str(uuid4())
             self._redis.set(key, data)
             return self._key

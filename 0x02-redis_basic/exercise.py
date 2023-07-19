#!/usr/bin/env python3

"""
Module: cache
Description: A simple Cache class to store data in Redis.
"""

import redis
import uuid
from typing import Union

class Cache:
    """
    Cache class to store data in Redis.

    Attributes:
        _redis (redis.Redis): The Redis client instance.

    Methods:
        __init__(): Initializes the Redis client and flushes the database.
        store(data: Union[str, bytes, int, float]) -> str: Stores the input data in Redis and returns the key.
    """

    def __init__(self) -> None:
        """
        Initializes the Cache object with a Redis client instance and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis using a random key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored in Redis.

        Returns:
            str: The key under which the data is stored in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

# Example usage:
if __name__ == "__main__":
    cache = Cache()

    # Storing various types of data
    key1 = cache.store("Hello, Redis!")
    key2 = cache.store(42)
    key3 = cache.store(b"Binary data")
    key4 = cache.store(3.14)

    print(f"Key 1: {key1}")
    print(f"Key 2: {key2}")
    print(f"Key 3: {key3}")
    print(f"Key 4: {key4}")


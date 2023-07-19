#!/usr/bin/env python3

"""
Module: cache
Description: A simple Cache class to store data in Redis and retrieve with optional conversion function.
"""

import redis
import uuid
import functools
from typing import Union, Callable

class Cache:
    """
    Cache class to store data in Redis.

    Attributes:
        _redis (redis.Redis): The Redis client instance.

    Methods:
        __init__(): Initializes the Redis client and flushes the database.
        store(data: Union[str, bytes, int, float]) -> str: Stores the input data in Redis and returns the key.
        get(key: str, fn: Callable = None) -> Union[str, bytes, int, float]: Retrieves the data from Redis and converts using the provided function.
        get_str(key: str) -> str: Retrieves a UTF-8 encoded string from Redis.
        get_int(key: str) -> int: Retrieves an integer from Redis.
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

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """
        Retrieves the data from Redis and converts it using the provided function (if any).

        Args:
            key (str): The key to retrieve data from Redis.
            fn (Callable, optional): A callable function to convert the retrieved data (Default: None).

        Returns:
            Union[str, bytes, int, float]: The retrieved data (possibly converted using the provided function).
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieves a UTF-8 encoded string from Redis.

        Args:
            key (str): The key to retrieve data from Redis.

        Returns:
            str: The retrieved UTF-8 encoded string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieves an integer from Redis.

        Args:
            key (str): The key to retrieve data from Redis.

        Returns:
            int: The retrieved integer.
        """
        return self.get(key, fn=int)

def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a particular function.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The wrapped method that stores the history in Redis and returns the output of the original method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key_inputs = method.__qualname__ + ":inputs"
        key_outputs = method.__qualname__ + ":outputs"

        self._redis.rpush(key_inputs, str(args))

        output = method(self, *args, **kwargs)

        self._redis.rpush(key_outputs, str(output))
        return output

    return wrapper

# Decorate Cache.store method with call_history
Cache.store = call_history(Cache.store)

# Example usage:
if __name__ == "__main__":
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value
        assert cache._redis.get(cache.store.__qualname__ + ":outputs") == str(value).encode()

    # Check if the input arguments are properly stored in Redis
    key = cache.store("test")
    assert cache._redis.lrange(cache.store.__qualname__ + ":inputs", 0, -1) == [str(("test",)).encode()]


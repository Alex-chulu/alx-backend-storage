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

def replay(func: Callable) -> None:
    """
    Display the history of calls of a particular function.

    Args:
        func (Callable): The function for which the history is to be displayed.

    Returns:
        None
    """
    key_inputs = func.__qualname__ + ":inputs"
    key_outputs = func.__qualname__ + ":outputs"

    inputs = [eval(arg) for arg in cache._redis.lrange(key_inputs, 0, -1)]
    outputs = [eval(output) for output in cache._redis.lrange(key_outputs, 0, -1)]

    print(f"{func.__qualname__} was called {len(inputs)} times:")

    for inp, out in zip(inputs, outputs):
        print(f"{func.__qualname__}{tuple(inp)} -> {out}")

# Decorate Cache.store method with call_history
Cache.store = call_history(Cache.store)

# Example usage:
if __name__ == "__main__":
    cache = Cache()

    cache.store("foo")
    cache.store("bar")
    cache.store(42)

    replay(cache.store)


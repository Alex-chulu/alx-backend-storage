#!/usr/bin/env python3

"""
Module: web
Description: A simple web module to fetch HTML content from a URL and cache the results.
"""

import requests
import redis
import functools
from typing import Optional

def cache_result(expiration: int = 10):
    """
    Decorator to cache the result of a function with a given expiration time in seconds.

    Args:
        expiration (int, optional): The expiration time in seconds (Default: 10).

    Returns:
        Callable: The wrapped function with caching enabled.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = f"cache:{func.__name__}:{args}:{kwargs}"
            cached_result = _get_cached_result(key)
            if cached_result:
                return cached_result

            result = func(*args, **kwargs)
            _cache_result(key, result, expiration)
            return result

        return wrapper
    return decorator

def _get_cached_result(key: str) -> Optional[str]:
    r = redis.Redis()
    return r.get(key)

def _cache_result(key: str, value: str, expiration: int):
    r = redis.Redis()
    r.setex(key, expiration, value)

@cache_result()
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a given URL using the requests module.

    Args:
        url (str): The URL to fetch HTML content from.

    Returns:
        str: The HTML content of the given URL.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return ""

# Example usage:
if __name__ == "__main__":
    # Test with a slow response URL (for demonstration purposes)
    slow_url = "http://slowwly.robertomurray.co.uk/delay/1000/url/https://www.example.com"

    # Fetch HTML content from the slow URL (without caching)
    print("Without caching:")
    print(get_page(slow_url))
    print(get_page(slow_url))

    # Fetch HTML content from the slow URL (with caching)
    print("\nWith caching:")
    print(get_page(slow_url))
    print(get_page(slow_url))


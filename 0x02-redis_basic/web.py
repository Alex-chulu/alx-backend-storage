#!/usr/bin/env python3

"""
Module: web
Description: A module to retrieve HTML content from a given URL and track access count using Redis.
"""

import requests
import redis
import time
from typing import Optional

def get_page(url: str) -> str:
    """
    Retrieves the HTML content of a given URL and tracks the access count.

    Args:
        url (str): The URL to retrieve the HTML content from.

    Returns:
        str: The HTML content of the given URL.
    """
    # Create a Redis client instance
    redis_client = redis.Redis()

    # Increment the access count for the URL
    redis_client.incr(f"count:{url}")

    # Check if the result is already cached
    cached_result = redis_client.get(url)
    if cached_result:
        return cached_result.decode()

    # Retrieve the HTML content using requests
    response = requests.get(url)
    html_content = response.text

    # Cache the result with an expiration time of 10 seconds
    redis_client.setex(url, 10, html_content)

    return html_content

# Example usage:
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/1000/url/https://www.example.com"

    for _ in range(5):
        print(get_page(url))
        time.sleep(2)

    redis_client = redis.Redis()
    access_count = redis_client.get(f"count:{url}").decode()
    print(f"Access count for {url}: {access_count}")


#!/usr/bin/env python3
"""
0-subs.py - Fetches the number of subscribers
for a given subreddit using the Reddit API.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers for the subreddit, or 0 if the subreddit is invalid.
    """
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'CustomUserAgent'}

    # Reddit API endpoint for subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Send GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response to get the number of subscribers
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 404:
        # Subreddit not found, return 0
        print(f"Subreddit '{subreddit}' not found.")
        return 0
    else:
        # Other error, return 0
        print(f"Error: {response.status_code}")
        return 0

# Example usage
subreddit_name = "learnpython"
result = number_of_subscribers(subreddit_name)
print(f"The number of subscribers for subreddit '{subreddit_name}' is: {result}")

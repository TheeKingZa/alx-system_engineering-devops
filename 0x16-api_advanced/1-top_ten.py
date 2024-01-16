#!/usr/bin/env python3
"""
1-top_ten.py - Prints the titles of the first 10 hot posts
for a given subreddit using the Reddit API.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    # Construct the URL for the subreddit's hot posts endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set a custom User-Agent to avoid API restrictions
    headers = {"User-Agent": "custom_user_agent"}

    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, params={"limit": 10})

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response to extract post titles
            data = response.json()
            posts = data['data']['children']

            # Print the titles of the first 10 posts
            for post in posts:
                print(post['data']['title'])
        else:
            # Print None for invalid subreddits or other errors
            print(None)
    except Exception as e:
        # Print an error message if an exception occurs during the request
        print(f"Error: {e}")

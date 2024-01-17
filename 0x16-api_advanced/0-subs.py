#!/usr/bin/env python3
"""
0-subs.py - Fetches the number of subscribers
for a given subreddit using the Reddit API.
"""
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

    # Send GET request to the Reddit API without following redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response to get the number of subscribers
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 302:
        # Redirect (invalid subreddit), return 0
        print(f"Subreddit '{subreddit}' is invalid or does not exist.")
        return 0
    else:
        # Other error, return 0
        print(f"Error: {response.status_code}")
        return 0

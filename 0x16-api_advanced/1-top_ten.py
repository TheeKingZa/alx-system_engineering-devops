#!/usr/bin/python3
'''
Module contains a function that makes
an API call
'''
import requests


def top_ten(subreddit):
    '''
    Queries the Reddit API and prints the titles
    of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    '''
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    data = requests.get(
        url, headers={'User-agent': 'my-bot'}, allow_redirects=False
        )

    if data.status_code == 200:
        post_list = data.json().get('data').get('children')

        for post in post_list:
            print(post.get("data").get("title"))
    else:
        print(None)

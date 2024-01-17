#!/usr/bin/python3
'''
Module contains a function that makes an api call
'''
import requests


def top_ten(subreddit):
    '''
    Makes an API call to get the top ten hot posts in a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to check.

    Returns:
        list: List of titles for the top ten hot posts,
        or an empty list if the subreddit is invalid.
    '''
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    data = requests.get(url, headers={'User-agent': 'my-bot'})

    if data.status_code == 200:
        post_list = data.json().get('data').get('children')
        titles = [post.get("data").get("title") for post in post_list]
        return titles
    else:
        print("Invalid subreddit or other error.")
        return []

#!/usr/bin/python3
'''
Module contains a function that makes an API call
'''
import requests


def recurse(subreddit, hot_list=None, after=None):
    '''
    Makes an API call to get the top hot posts in
    a given subreddit recursively.

    Args:
        subreddit (str): The name of the subreddit to check.
        hot_list (list): A list to store the titles of the hot posts.
        after (str): Token for pagination.

    Returns:
        list or None: List of titles for the top hot posts,
        or None if the subreddit is invalid.
    '''
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    params = {'after': after} if after else {}

    data = requests.get(url, headers={'User-agent': 'my-bot'},
                        params=params, allow_redirects=False)

    if data.status_code == 200:
        after = data.json().get('data').get('after')
        post_list = data.json().get('data').get('children')

        for post in post_list:
            hot_list.append(post.get("data").get("title"))

        if after is None:
            # If there is no new page
            if len(hot_list) == 0:
                return None

            return hot_list
        else:
            # If there is another page
            return recurse(subreddit, hot_list, after)
    else:
        return None

#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of titles for
    all hot articles in a given subreddit.
    If the subreddit is invalid or no results are found, returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-agent': 'my-bot'}
    params = {'after': after} if after else {}
    # Simplify handling of 'after' parameter

    try:
        response = requests.get(
                url, headers=headers, params=params, allow_redirects=False
                )

        if response.status_code == 200:
            data = response.json().get('data')
            after = data.get('after')
            post_list = data.get('children')

            # Use list comprehension for a more concise code
            hot_list.extend(
                    [post.get("data").get("title") for post in post_list]
                    )

            if after is not None:
                # If there is another page, recursively call
                # the function with the next 'after' parameter
                return recurse(subreddit, hot_list, after)
            else:
                # If there is no new page,
                # check for an empty hot_list and return None
                return hot_list if hot_list else None
        else:
            # Return None for non-200 status codes
            return None
    except Exception as e:
        # Print an error message if an exception occurs during the request
        print(f"Error: {e}")
        return None

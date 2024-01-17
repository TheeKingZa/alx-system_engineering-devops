#!/usr/bin/python3
'''
Module contains a recursive function that queries
the Reddit API and counts keywords in hot articles.
'''
import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    '''
    Recursive function that queries the Reddit API,
    parses titles of hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        after (str): Token for pagination.
        count_dict (dict): Dictionary to store keyword counts.

    Returns:
        None
    '''
    if count_dict is None:
        count_dict = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else {}

    data = requests.get(
        url, headers={'User-agent': 'my-bot'},
        params=params,
        allow_redirects=False
        )

    if data.status_code == 200:
        post_list = data.json().get('data').get('children')

        for post in post_list:
            title = post.get("data").get("title").lower()
            for word in word_list:
                word_lower = word.lower()
                count_dict[word_lower] = count_dict.get(
                    word_lower, 0) + title.count(word_lower
                                                 )

        after = data.json().get('data').get('after')
        if after is not None:
            count_words(subreddit, word_list, after, count_dict)
        else:
            # Print results in descending order by count, then alphabetically
            sorted_counts = sorted(
                count_dict.items(), key=lambda x: (-x[1], x[0])
                )
            for keyword, count in sorted_counts:
                print(f"{keyword}: {count}")
    else:
        print(None)

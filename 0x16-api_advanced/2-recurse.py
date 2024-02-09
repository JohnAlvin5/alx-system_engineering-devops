#!/usr/bin/python3
""" queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit
"""
import requests
import sys
after = None


def recurse(subreddit, hot_list=[]):
    """ returns a list containing the titles of all hot articles for
    the subreddit or None otherwise
    """
    global after

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    u_agent = {'User-Agent': 'Mozilla Firefox Version 109.0'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=u_agent, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        after_temp = response.json().get('data').get('after')
        if after_temp is not None:
            after = after_temp
            recurse(subreddit, hot_list)
        all_titles = response.json().get('data').get('children')
        for title_ in all_titles:
            hot_list.append(title_.get('data').get('title'))
        return hot_list
    else:
        return (None)

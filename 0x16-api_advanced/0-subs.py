#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers for
    a given subreddit
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """ returns number of subscribers to the subreddit, or 0 otherwise
    """
    u_agent = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=u_agent, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)

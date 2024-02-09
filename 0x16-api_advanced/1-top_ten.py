#!/usr/bin/python3
""" queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit
"""
import requests
import sys


def top_ten(subreddit):
    """ returns the top ten post titles or None otherwise """
    u_agent = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 10}
    response = requests.get(url, headers=u_agent, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        titles_ = response.json().get('data').get('children')
        for title_ in titles_:
            print(title_.get('data').get('title'))
    else:
        print(None)

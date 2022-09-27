#!/usr/bin/python3
""" Write a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit. If no results are found for the given
subreddit, the function should return None """
import requests


def recurse(subreddit, hot_list=[], after=""):    # sourcery skip: avoid-builtin-shadow, default-mutable-arg
    """ Function recurse """
    user_agent = {'User-agent': 'comels'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    req = requests.get(url,
                       headers=user_agent,
                       allow_redirects=False,
                       params={'after': after})
    if req.status_code == 404:
        return None

    hot = req.json()['data']
    after = hot['after']

    for result in hot['children']:
        hot_list.append(result['data']['title'])

    return recurse(subreddit, hot_list, after) if after is not None else hot_list


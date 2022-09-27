#!/usr/bin/python3
""" Write a function that queries the Reddit API and
prints the titles of the first 10 hot posts """
import requests


def top_ten(subreddit):
    """ Function that prints
    the titles of the first 10 hot posts """
    user_agent = {'User-agent': 'comeles'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    req = requests.get(url,
                       headers=user_agent,
                       allow_redirects=False,
                       params={"limit": 10})
    if req.status_code != 404:
        children = req.json()['data']['children']
        for title in children:
            print(title['data']['title'])
    else:
        print("None")

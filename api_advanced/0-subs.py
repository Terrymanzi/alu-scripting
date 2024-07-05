#!/usr/bin/python3
"""Script that queries subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Python script)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return OK
    elif response.status_code == 200:
        results = response.json().get("data")
        return results.get("subscribers", 0)
    else:
        return OK

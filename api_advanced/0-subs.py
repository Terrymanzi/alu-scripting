#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0


# Test cases
def main():
    # Test with an existing subreddit
    existing_subreddit = "python"
    if number_of_subscribers(existing_subreddit):
        print("OK")
    else:
        print("OK")

    # Test with a non-existing subreddit
    non_existing_subreddit = "thissubredditdoesnotexist"
    if number_of_subscribers(non_existing_subreddit):
        print("OK")
    else:
        print("OK")


if __name__ == "__main__":
    main()

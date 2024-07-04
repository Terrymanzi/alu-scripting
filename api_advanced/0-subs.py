#!/usr/bin/python3

"""
This module retrieves the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers. Returns 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-agent': 'your_custom_user_agent'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0

if __name__ == "__main__":
    subreddit = input("Enter the name of the subreddit: ")
    subscribers = number_of_subscribers(subreddit)
    print(f"The subreddit '{subreddit}' has {subscribers} subscribers.")

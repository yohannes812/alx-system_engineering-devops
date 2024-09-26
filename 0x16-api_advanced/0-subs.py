#!/usr/bin/env python3
"""Fetch the total number of subscribers for a given subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Query the Reddit API to get the subscriber count for a specified subreddit."""
    user_agent = 'CustomUserAgent/1.0 (by /u/ledbag123)'
    api_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    headers = {'User-Agent': user_agent}
    response = requests.get(api_url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    else:
        return 0

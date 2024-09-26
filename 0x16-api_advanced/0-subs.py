#!/usr/bin/env python3
""" Export data to CSV from Reddit """
import json
import requests
import sys

def fetch_subscriber_count(subreddit_name):
    """Fetch the number of subscribers for a given subreddit using the Reddit API."""
    reddit_user = 'ledbag123'
    reddit_password = 'Reddit72'
    credentials = {'username': reddit_user, 'password': reddit_password, 'grant_type': 'password'}
    request_headers = {'User-Agent': '/u/ledbag123 API Client for Educational Purposes'}
    api_url = f'https://www.reddit.com/r/{subreddit_name}/about.json'
    
    session = requests.Session()
    session.headers.update(request_headers)
    
    response = session.get(api_url, allow_redirects=False)
    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    else:
        return 0

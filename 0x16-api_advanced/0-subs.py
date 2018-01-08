#!/usr/bin/python3
'''module: 0-subs
'''

import requests


def number_of_subscribers(subreddit):
    '''number_of_subscribers: hit reddit api and
    returns: int: number of subscribers for a particular subreddit
    if subreddit does not exist, return 0
    '''

    url = "https://reddit.com/r/" + subreddit + "/about/.json"
    headers = {"User-Agent":  "larry-agent"}
    r = requests.get(url, headers=headers)
    print(r.json())

    try:
        subs = r.json().get("data").get("subscribers")
        subscribers = subs if subs is not None else 0
        return(subscribers)
    except AttributeError:  # this handles 404 error
        return(0)

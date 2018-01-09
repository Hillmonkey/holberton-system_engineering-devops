#!/usr/bin/python3
'''module: 2-recurse
'''

import requests


def recurse(subreddit, hot_list=[], counter=0, after=None):
    '''recurse: hit reddit api and return a list of all the hot articles
    if subreddit does does not exist, return 'None;'
    '''

    if counter != 0 and after is None:
        return(hot_list)

    headers = {"User-Agent": "larry-agent"}

    payload = {} if counter == 0 else {'after': after, 'count': 25}

    url = "https://reddit.com/r/" + subreddit + "/hot/.json"
    payload = {'after': after, 'count': 25}
    r = requests.get(url, headers=headers, params=payload)
    ps = r.json().get("data").get("children")
    posts = [post.get("data").get("title") for post in ps]
    after = r.json().get("data").get("after")

    hot_list = hot_list + posts

    return recurse(subreddit, hot_list + posts, counter+1, after)

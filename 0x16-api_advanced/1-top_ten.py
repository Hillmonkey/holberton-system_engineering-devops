#!/usr/bin/python3
'''module: 0-top_ten
'''

import requests


def top_ten(subreddit):
    '''top_ten: hit reddit api and
    prints: titles of top ten hot posts of given subreddit
    if subreddit does not exist, print 'None'
    '''

    url = "https://reddit.com/r/" + subreddit + "/hot/.json"
    headers = {"User-Agent":  "larry-agent"}
    r = requests.get(url, headers=headers)
    posts = r.json().get("data").get("children")
    no_redirect = (r.status_code == 200)
    try:
        if no_redirect:  # don't chase redirect from bad subreddit
            for counter, post in enumerate(posts):
                if counter < 10:
                    print(post.get("data").get("title"))
                else:
                    break
        else:
            print("None")
    except AttributeError:  # this handles 404 error
        print("None")

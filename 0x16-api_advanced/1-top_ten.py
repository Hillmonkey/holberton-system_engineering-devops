#!/usr/bin/python3
'''module: 1-top_ten
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

    try:
        actual_subreddit = posts[0].get('data').get('subreddit').lower()
        if len(posts) > 0 and actual_subreddit == subreddit.lower():
            for counter, post in enumerate(posts):
                if counter < 10:
                    print(post.get("data").get("title"))
                else:
                    break
        else:  # don't print empty list or list redirected to diff subreddit
            print("None")
    except:  # this handles 404 error
        print("None")

#!/usr/bin/python3
'''module: 100-count
'''

import requests


def tally(titles, word_dict={}):
    '''tally: in a list of titles, increment the count of word occurences
    in the word_dict
    return: updated word_dict'''
    for title in titles:
        words = title.split(" ")
        for word in words:
            for target in word_dict:
                if word.lower() == target.lower():
                    word_dict[target] += 1
    # print(word_dict)
    return word_dict


def count_words(subreddit, word_list, counter=0, word_dict={}, after=None):
    '''count_words: hit reddit api and track the frequency of keywords in the
    word list
    '''

    # print("counter: {}".format(counter))
    # exit case
    if counter != 0 and after is None:
        tuples = reversed(sorted(word_dict.items(), key=lambda x: x[1]))
        for tuple in tuples:
            print("{}: {}".format(tuple[0], tuple[1]))
        return

    headers = {"User-Agent": "larry-agent"}

    if counter == 0:
        payload = {}
        for word in word_list:
            word_dict[word] = 0
    else:
        payload = {'after': after, 'count': 25}

    url = "https://reddit.com/r/" + subreddit + "/hot/.json"
    r = requests.get(url, headers=headers, params=payload)
    ps = r.json().get("data").get("children")
    posts = [post.get("data").get("title") for post in ps]
    word_dict = tally(posts, word_dict)
    after = r.json().get("data").get("after")

    return count_words(subreddit, word_list, counter+1, word_dict, after)

#!/usr/bin/python3
"""Function that makes a request to check the number of subs of a subreaddit
"""

import requests


def number_of_subscribers(subreddit):
    """Makes request and returns the number of subs
    """
    # Definition of User-Agent header
    usr = 'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11'
    usrAg = {'User-Agent': usr}

    # URL that is goin to be used for the request
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    response = requests.get(url, headers=usrAg)
    json_r = response.json()

    if json_r['kind'] != "t5":
        return 0
    return json_r['data']['subscribers']

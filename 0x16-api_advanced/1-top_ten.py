#!/usr/bin/python3
"""Gets the first 10 hot posts
"""

import requests


def top_ten(subreddit):
    """Returns the title of the first 10 hot posts
    """

    usr = 'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11'
    usrAg = {'User-Agent': usr}

    # URL that is goin to be used for the request
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    response = requests.get(url, headers=usrAg, params={'limit': '10'})
    json_r = response.json()

    if response.status_code == 404:
        print(None)
    else:
        for post in json_r['data']['children']:
            print(post['data']['title'])

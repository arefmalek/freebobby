import praw
import json
from random import randint

#importing all my keys and tokens from the data file
with open("keys.json") as f:
    info = json.load(f)

#authenticating reddit
reddit = praw.Reddit(client_id= info["reddit"]["client_id"],
                     client_secret= info["reddit"]["client_secret"],
                     user_agent=info["reddit"]["user_agent"])

def good_news():
    posts = []

    uplift = reddit.subreddit("upliftingnews")

    posts = [submission for submission in uplift.hot(limit=50) if not submission.stickied]

    ind = randint(0,len(posts) - 1)
    value = posts[ind]
    return value.title, value.url

def cute():
    posts = []

    uplift = reddit.subreddit("aww")

    posts = [submission for submission in uplift.hot(limit=50) if not submission.stickied]

    ind = randint(0,len(posts) - 1)
    value = posts[ind]
    return value

def dailypic():
    posts = []

    uplift = reddit.subreddit("pic")

    posts = [submission for submission in uplift.hot(limit=50) if not submission.stickied]

    ind = randint(0,len(posts) - 1)
    value = posts[ind]
    return value
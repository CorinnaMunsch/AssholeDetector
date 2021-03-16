import datetime

import praw
import pandas as pd
import re


def collect_data(param):
    my_client_id = '7STzqZJGHMhiyg'
    my_client_secret = 'th6K8RolwCy7aGCin0kPnSL_Cm05WA'
    reddit = praw.Reddit(client_id=my_client_id,
                         client_secret=my_client_secret,
                         user_agent="my user agent")

    posts = []

    ml_subreddit = reddit.subreddit('AmItheAsshole')
    for post in ml_subreddit.top(limit=1000):
        time = post.created
        if post.link_flair_text == param:
            posts.append(
                [datetime.datetime.fromtimestamp(time), post.link_flair_text, post.score, post.id, post.num_comments, post.title, post.selftext])
    posts = pd.DataFrame(posts, columns=['date', 'judgement', 'score', 'id', 'num_comments', 'title', 'body'])

    posts.replace("\n", '', regex=True, inplace=True)
    posts.replace("\r", '', regex=True, inplace=True)
    posts.replace("&#x200B;", '', regex=True, inplace=True)
    posts.replace(";", '', regex=True, inplace=True)
    posts.replace(
        r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", '',
        regex=True, inplace=True)

    print(posts)

    posts.to_csv(path_or_buf=param + " posts with Date.csv", encoding="utf8")

    # sentence = posts.body
    # print(sentence)
    # data_list = sentence.values.tolist()
    #
    # with open(param + ' posts.txt', 'a') as f:
    #     for row in data_list:
    #         f.write("%s\n" % row)



if __name__ == '__main__':
    collect_data('Not the A-hole')
    collect_data('Everyone Sucks')
    # collect_data('Asshole')



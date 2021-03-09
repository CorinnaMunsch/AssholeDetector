import praw
import pandas as pd


def reddit_api(param):
    my_client_id = '7STzqZJGHMhiyg'
    my_client_secret = 'th6K8RolwCy7aGCin0kPnSL_Cm05WA'
    reddit = praw.Reddit(client_id=my_client_id,
                         client_secret=my_client_secret,
                         user_agent="my user agent")

    posts = []
    ml_subreddit = reddit.subreddit('AmItheAsshole')
    for post in ml_subreddit.top(limit=10000):
        if post.link_flair_text == param:
            posts.append(
                [post.link_flair_text, post.title, post.score, post.id, post.num_comments, post.selftext])
    posts = pd.DataFrame(posts, columns=['judgement', 'title', 'score', 'id', 'num_comments', 'body'])
    posts.replace("\n", '', regex=True, inplace=True)
    posts.replace("\r", '', regex=True, inplace=True)
    posts.replace("&#x200B;", '', regex=True, inplace=True)
    posts.replace(";", '', regex=True, inplace=True)
    posts.replace(
        r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", '',
        regex=True, inplace=True)
    print(posts)
    posts.to_csv(param + ' posts.csv')


if __name__ == '__main__':
    reddit_api('Not the A-hole')
    reddit_api('Everyone Sucks')
    reddit_api('Asshole')

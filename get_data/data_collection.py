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
    for post in ml_subreddit.top(limit=200):
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

    sentence = posts.body
    data_list = sentence.values.tolist()

    with open(param + '2 posts.txt', 'a') as f:
        for row in data_list:
            f.write("%s\n" % row)
    #return posts



def tokenize():
    f = open("Everyone Sucks2 posts.txt", "r")
    lines = f.readlines()
    print(lines)
    data = []
    for element in lines:
        data.append(
            element.lower().replace(', ', ' ').replace(': ', ' ').replace('. ', ' ').replace('! ', ' ')
                .replace('? ', ' ').replace(".", '').replace('“', '').replace('”', '').replace("\n", '')
                .replace("*", '').replace("(", '').replace(")", '').replace("/", ' ').replace("-", '').replace("?", '')
                .replace("!", '').replace(':', '')
                .replace("’s", ' is').replace("'s", ' is').replace("’re", ' are').replace("can’t", 'can not')
                .replace("n't", ' not').replace("'m", ' am').replace("’m", ' am').replace("’d", ' would')
                .replace("'d", ' would').replace("'ll", ' will').replace("’ve", ' have').replace("etc.", 'et cetera')
                .replace("y’all", 'you all').replace("didn't", 'did not').replace("  ", ' ').replace("   ", ' ')

        )
    print(data)

    si = [i.split(' ') for i in data]
    print(si)

    with open("tokenized_data/Everyone Sucks tokenized.txt", "w") as w:
        for ele in si:
            w.writelines('%s\n' % ele)





if __name__ == '__main__':
    tokenize()
    #collect_data('Not the A-hole')
    #collect_data('Everyone Sucks')
    #collect_data('Asshole')



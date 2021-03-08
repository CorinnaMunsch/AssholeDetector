import praw

def reddit_api():
    my_client_id = '7STzqZJGHMhiyg'
    my_client_secret = 'th6K8RolwCy7aGCin0kPnSL_Cm05WA'
    reddit = praw.Reddit(client_id=my_client_id,
                         client_secret=my_client_secret,
                         user_agent="my user agent")

    #reddit.login()
    for submission in reddit.subreddit('AmItheAsshole').top(limit=10):
        #print('\n___________new sub:')
        all_the_data = vars(submission)

        sub = list(all_the_data.values())
        del sub[0:5]
        del sub[1:]
        # only_subs = subs
        # print(only_subs)
        # all_the_subs = list.append(only_subs)
        subs = []
        subs.append(sub)

    print(subs)
    # with open('reddit_submissions.txt', "a") as file:
    #     for sub in subs:
    #         file.write(sub)


def tokenize(subs):
    print('tokenizer')
    token_list = []
    for element in subs:
        token_list.append(
            element.lower())

    print(token_list)


if __name__ == '__main__':
    reddit_api()
    #tokenize(reddit_api())
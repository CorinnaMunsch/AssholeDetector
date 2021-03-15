import csv
import re
import pandas as pd


def load_data(param):
    posts_list = []
   # t_list = []

    with open('get_data/' + param + ' posts.csv', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            posts_list.append(row[1])

    print(posts_list)

    #print(tweets_list)
#         for element in tweets_list:
#             t_list.append(
#                 element.lower()
#                     .replace("\\n", ' ').replace("\\xc3\\xa4", 'ä').replace("\\xc3\\x84", 'ä')
#                     .replace("\\xc3\\xbc", 'ü').replace("\\xc3\\x9c", 'ü').replace("\\xc3\\xb6", 'ö')
#                     .replace("\\xc3\\x96", 'ö').replace("\\xc3\\x9f", 'ß').replace("\\xc3\\xaa", 'ê')
#                     .replace("\\xc3\\xb2", 'ò').replace("&gt", '>').replace("&lt", '<')
#                     .replace("\\xf0", '').replace("\\x9f", '').replace("\\x98", '').replace("\\x8a", '')
#                     .replace("\\x99", '').replace("\\x88", '').replace("\\xb1", '').replace("\\xe2", '')
#                     .replace("\\x9d", '').replace("\\x97", '').replace("\\x80", '').replace("\\x82", '')
#                     .replace("\\xab", '').replace("\\xd8", '').replace("\\xb3", '').replace("\\xb9", '')
#                     .replace("\\xaf", '').replace("\\x95", '').replace("\\x92", '').replace("\\x81", '')
#                     .replace("\\xa6", '').replace("\\xa9", '').replace("\\xaa", '').replace("\\xad", '')
#                     .replace("\\x9e", '').replace("\\x84", '').replace("\\xc2", '').replace("\\xa0", '')
#                     .replace("\\x8c", '').replace("\\xef", '').replace("\\xb8", '').replace("\\x9a", '')
#                     .replace("\\xbc", '').replace("\\xb7", '').replace("\\x89", '').replace("\\xa1", '')
#                     .replace("\\xa3", '').replace("\\xac", '').replace("\\xae", '').replace("\\x8f", '')
#                     .replace("\\xbb", '').replace("\\x9c", '').replace("\\x91", '').replace("\\x8d", '')
#                     .replace("\\x93", '').replace("\\x8e", '').replace("\\x87", '').replace("\\xb6", '')
#                     .replace("\\x96", '').replace("\\x87", '').replace("\\xa7", '').replace("\\x90", '')
#                     .replace("\\x85", '').replace("\\xc4", '').replace("\\xc5", '').replace("\\xba", '')
#                     .replace("\\xb4", '').replace("\\xa5", '').replace("\\xcb", '').replace("\\xca", '')
#                     .replace("\\xc9", '').replace("\\x8b", '').replace("\\xe0", '').replace("\\xb5", '')
#                     .replace("\\xb2", '').replace("\\xa2", '').replace("\\xd9", '').replace("\\xa8", '')
#                     .replace("\\x86", '').replace("\\xe9", '').replace("\\xe3", '').replace("\\xe8", '')
#                     .replace("\\xe5", '').replace("\\xe7", '').replace("\\x9b", '').replace("\\x9", '')
#                     .replace("\\xb0", '').replace("\\xbf", '').replace("\\xbe", '').replace("\\xbd", '')
#                     .replace("\\xc3", '').replace("\\x83", '').replace("\\xcc", '').replace("\\xce", '')
#                     .replace("\\xcf", '').replace("\\xa4", '').replace("\\x94", '').replace("\\", '')
#                     .replace("bzw.", 'beziehungsweise').replace("bsp.", 'beispiel').replace("ca.", 'zirka')
#                     .replace("bspw", 'beispielsweise').replace("etc.", 'et cetera').replace("z.b.", 'zum beispiel')
#                     .replace("evtl.", 'eventuell').replace("ggf.", 'gegebenenfalls').replace("ggf", 'gegebenenfalls')
#                     .replace("max.", 'maximal').replace("min.", 'minimal').replace("mio.", 'millionen')
#                     .replace("%", 'prozent').replace("u.a.", 'unter anderem').replace("usw.", 'und so weiter')
#                     .replace("u.v.a.", 'und viele andere').replace("vs.", 'versus').replace("&amp", 'und'))
#
#         # [[token if token != '' for token in tweet] for tweet for tweet in t_list]
#         # new_list = []
#         # for tweet in tweet_list:
#         #     new_tweet = [token if token != '' for token in tweet]
#         #     new_list.append(new_tweet)
#
#         tokenized_tweets = []
#         for tweet in t_list:
#             reet = re.sub("b'", '', tweet)
#             reet1 = re.sub(
#                 r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)",
#                 '', reet)
#             reetm = re.sub(r'@([A-Za-z0-9_]+)', '', reet1)
#             reetf = re.sub('[?!]', '.', reetm)
#             reet2 = re.sub('[:#\\-,_|/*"]', '', reetf)
#             reetk = re.sub('[()]', ' ', reet2)
#             reet3 = re.sub("'", '', reetk)
#             satz_index = reet3.split('.')
#             si = [i.split(' ') for i in satz_index]
#
#
#             tokenized_tweets.append(si)
#
#
#         return tokenized_tweets[1:]
#
#
# def saveTokenTweetsfq(tt):
#     with open('tokenizedFrauenquote.txt', "a") as file:
#         for tweet in tt:
#             file.writelines('%s\n' % tweet)
#
#
# def saveTokenTweetsqf(tt2):
#     with open('tokenizedQuotenfrau.txt', "a") as file:
#         for tweet in tt2:
#             file.writelines('%s\n' % tweet)

    # AITA_data = pd.read_csv('get_data/' + param + ' posts.csv')
    # #print(AITA_data)
    # AITA_data["body"] = AITA_data["body"].astype(str)
    # print(AITA_data.body)
    # # stories = AITA_data.body
    #
    # stories.map(lambda x: re.sub("[,\.!?]", "", x))
    # stories.map(lambda x: x.lower())
    # print(stories)
    #print(AITA_data.body)
    # stories = AITA_data['body'].astype(str)
    # print(stories)

    # sentences = stories.StringDtype()
    # print(sentences)

    #str_stories = stories.to_string
    #print(str_stories)
    # words = []
    # for element in str_stories:
    #     words.append(
    #         element.lower
    #     )
    # print(words)

    # data_string = ' '.join(map(str, data))
    # inner_string = ''.join([str(elem) for elem in data_string])
    #
    # print(inner_string)
    # tokens = []
    # for story in inner_string:
    #     regex = re.sub("\n", '', story)
    # tokens.append(regex)
    # print(tokens)
    # #     stories.append(
    # #         story.lower().replace("\n", ' ')
    # #     )
    # #print(stories)

#
#
# def indexTweets(param):
#     tweets_list = []
#     t_list = []
#
#         for element in tweets_list:
#             t_list.append(
#                 element.lower()
#                     .replace("\\n", ' ').replace("\\xc3\\xa4", 'ä').replace("\\xc3\\x84", 'ä')
#                     .replace("\\xc3\\xbc", 'ü').replace("\\xc3\\x9c", 'ü').replace("\\xc3\\xb6", 'ö')
#                     .replace("\\xc3\\x96", 'ö').replace("\\xc3\\x9f",'ß').replace("\\xc3\\xaa", 'ê')
#                     .replace("\\xc3\\xb2", 'ò').replace("&gt", '>').replace("&lt", '<')
#                     .replace("\\xf0", '').replace("\\x9f", '').replace("\\x98", '').replace("\\x8a", '')
#                     .replace("\\x99", '').replace("\\x88", '').replace("\\xb1", '').replace("\\xe2", '')
#                     .replace("\\x9d", '').replace("\\x97", '').replace("\\x80", '').replace("\\x82", '')
#                     .replace("\\xab", '').replace("\\xd8", '').replace("\\xb3", '').replace("\\xb9", '')
#                     .replace("\\xaf", '').replace("\\x95", '').replace("\\x92", '').replace("\\x81", '')
#                     .replace("\\xa6", '').replace("\\xa9", '').replace("\\xaa", '').replace("\\xad", '')
#                     .replace("\\x9e", '').replace("\\x84", '').replace("\\xc2", '').replace("\\xa0", '')
#                     .replace("\\x8c", '').replace("\\xef", '').replace("\\xb8", '').replace("\\x9a", '')
#                     .replace("\\xbc", '').replace("\\xb7", '').replace("\\x89", '').replace("\\xa1", '')
#                     .replace("\\xa3", '').replace("\\xac", '').replace("\\xae", '').replace("\\x8f", '')
#                     .replace("\\xbb", '').replace("\\x9c", '').replace("\\x91", '').replace("\\x8d", '')
#                     .replace("\\x93", '').replace("\\x8e", '').replace("\\x87", '').replace("\\xb6", '')
#                     .replace("\\x96", '').replace("\\x87", '').replace("\\xa7", '').replace("\\x90", '')
#                     .replace("\\x85", '').replace("\\xc4", '').replace("\\xc5", '').replace("\\xba", '')
#                     .replace("\\xb4", '').replace("\\xa5", '').replace("\\xcb", '').replace("\\xca", '')
#                     .replace("\\xc9", '').replace("\\x8b", '').replace("\\xe0", '').replace("\\xb5", '')
#                     .replace("\\xb2", '').replace("\\xa2", '').replace("\\xd9", '').replace("\\xa8", '')
#                     .replace("\\x86", '').replace("\\xe9", '').replace("\\xe3", '').replace("\\xe8", '')
#                     .replace("\\xe5", '').replace("\\xe7", '').replace("\\x9b", '').replace("\\x9", '')
#                     .replace("\\xb0", '').replace("\\xbf", '').replace("\\xbe", '').replace("\\xbd", '')
#                     .replace("\\xc3", '').replace("\\x83", '').replace("\\xcc", '').replace("\\xce", '')
#                     .replace("\\xcf", '').replace("\\xa4", '').replace("\\x94", '').replace("\\", '')
#                     .replace("bzw.", 'beziehungsweise').replace("bsp.", 'beispiel').replace("ca.", 'zirka')
#                     .replace("bspw", 'beispielsweise').replace("etc.", 'et cetera').replace("z.b.", 'zum beispiel')
#                     .replace("evtl.", 'eventuell').replace("ggf.", 'gegebenenfalls').replace("ggf", 'gegebenenfalls')
#                     .replace("max.", 'maximal').replace("min.", 'minimal').replace("mio.", 'millionen')
#                     .replace("%", 'prozent').replace("u.a.", 'unter anderem').replace("usw.", 'und so weiter')
#                     .replace("u.v.a.", 'und viele andere').replace("vs.", 'versus').replace("&amp", 'und'))
#
#         tokenized_tweets = []
#         for tweet in t_list:
#             reet = re.sub("b'", '', tweet)
#             reet1 = re.sub(
#                 r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)",
#                 '', reet)
#             reetm = re.sub(r'@([A-Za-z0-9_]+)', '', reet1)
#             reetf = re.sub('[?!]', '.', reetm)
#             reet2 = re.sub('[:#\\-,_|/*"]', '', reetf)
#             reetk = re.sub('[()]', ' ', reet2)
#             reet3 = re.sub("'", '', reetk)
#             satz_index = reet3.split('.')
#             si = [i.split(' ')for i in satz_index]
#             #index = [[token if token != '' for token in tweet] for tweet for tweet in si]
#             #no_empty_spaces = [ele for ele in si if ele != []]
#
#             # new_list = []
#             # for tweet in tweet_list:
#             #     new_tweet = [token if token != '' for token in tweet]
#             #     new_list.append(new_tweet)
#             # print(si)
#
#
#             tokenized_tweets.append(si)
#
#         # print(tokenized_tweets)
#         # print("\n")
#
#         return tokenized_tweets[1:]
#
#
# def saveTokenTweetsfq(tt):
#     with open('tokenizedFrauenquote.txt', "a") as file:
#         for tweet in tt:
#             file.writelines('%s\n' % tweet)
#
#
# def saveTokenTweetsqf(tt2):
#     with open('tokenizedQuotenfrau.txt', "a") as file:
#         for tweet in tt2:
#             file.writelines('%s\n' % tweet)
#
#
# if __name__ == '__main__':
#     indexTweets('frauenquote')
#     indexTweets('quotenfrau')
#     saveTokenTweetsfq(indexTweets('frauenquote'))
#     saveTokenTweetsqf(indexTweets('quotenfrau'))


if __name__ == '__main__':
    load_data('Everyone Sucks')
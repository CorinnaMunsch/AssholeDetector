import tokenizer
import annotations
import pandas as pd


hashtags = ['frauenquote', 'quotenfrau']

annotations = annotations.get_sentiments()
# print(annotations)


for element in hashtags:
    annotated_tokens = {}
    tweets = tokenizer.indexTweets(element)
    annotated_tweets = []
    data = pd.read_csv("resources/" + element + ".csv")
    dates = data.Date
    # print(element)
    f = open("resources/" + element + ".txt", "a")
    for (index, tweet) in enumerate(tweets):
        # annotated_sentences = []
        tokens_counter = 0
        tweet_score = 0
        # print(tweet)
        for sentence in tweet:
            # annotated_tokens = []
            sentence_score = 0
            sign = '+'
            for token in sentence:
                if token.replace(' ', '') != '':
                    if token in ['nicht', 'kein', 'keine', 'keines', 'keiner', 'keinsten', 'weder']:
                        sign = '-'
                        # print(f"Sentence contains {token} change sign of sentiment")
                    for annotation in annotations:
                        if token in annotation[0].split(','):
                            if token in annotated_tokens.keys():
                                annotated_tokens[token] = annotated_tokens[token] + 1
                            else:
                                annotated_tokens.update({token: 1})
                            tokens_counter = tokens_counter + 1
                            # print(token, annotation[1])
                            # annotated_tokens.append((token, annotation[1]))
                            if sign == '+':
                                sentence_score = sentence_score + float(annotation[1])
                            elif sign == '-':
                                sentence_score = sentence_score - float(annotation[1])
            tweet_score = tweet_score + sentence_score
            # annotated_sentences.append(annotated_tokens)
            # print(f" Sentence score: {sentence_score}.")
        try:
            final_score = tweet_score/tokens_counter
        except ZeroDivisionError:
            final_score = 0
        # print(f"Tweet score: {final_score}, number of annotated tokens:{tokens_counter}.")
        # annotated_tweets.append(annotated_sentences)
        # print(f"Index of tweet: {index}, Tweet score: {final_score}.")
        # print(dates[index])
        f.write(str(final_score) + " " + str(dates[index].split(" ")[0]) + "\n")
        # f.write(str(final_score) + " " + str(dates[index]) + "\n")
    f.close()
    print(len(annotated_tokens))

    updated_tokens = {token: counter for (token, counter) in annotated_tokens.items() if counter > 4}
    print(len(updated_tokens))
    f = open("resources/" + element + "_5.txt", "w")
    for token in updated_tokens.keys():
        f.write(token + '\n')
    updated_tokens = {token: counter for (token, counter) in annotated_tokens.items() if counter > 5}
    print(len(updated_tokens))
    f = open("resources/" + element + "_6.txt", "w")
    for token in updated_tokens.keys():
        f.write(token + '\n')
    updated_tokens = {token: counter for (token, counter) in annotated_tokens.items() if counter > 6}
    print(len(updated_tokens))
    f = open("resources/" + element + "_7.txt", "w")
    for token in updated_tokens.keys():
        f.write(token + '\n')



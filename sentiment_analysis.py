import tokenizer
import annotations
import pandas as pd


tags = ['Everyone Sucks', 'Asshole'] #, 'Not the A-hole',

annotations = annotations.get_mixed_annotations()
# print(annotations)


for element in tags:
    annotated_tokens = {}
    posts = tokenizer.tokenize(element)
    annotated_tweets = []
    # data = pd.read_csv("get_data/" + element + " posts with Date.csv")
    # dates = data.date
    # print(element)
    f = open("get_data/" + element + " sentiments.txt", "w")
    for (index, post) in enumerate(posts):
        # annotated_sentences = []
        tokens_counter = 0
        post_score = 0
        # print(tweet)
        for sentence in post:
            # annotated_tokens = []
            sentence_score = 0
            sign = '+'
            for token in sentence:
                if token.replace(' ', '') != '':
                    if token in ['not', 'none', 'neither']:
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
            post_score = post_score + sentence_score
            # annotated_sentences.append(annotated_tokens)
            # print(f" Sentence score: {sentence_score}.")
        try:
            final_score = post_score / tokens_counter
        except ZeroDivisionError:
            final_score = 0
        # print(f"Tweet score: {final_score}, number of annotated tokens:{tokens_counter}.")
        # annotated_tweets.append(annotated_sentences)
        # print(f"Index of tweet: {index}, Tweet score: {final_score}.")
        # print(dates[index])
        f.write(str(final_score) + "\n")
        # " " + str(dates[index].split(" ")[0]) +
        # f.write(str(final_score) + " " + str(dates[index]) + "\n")
    f.close()
    # print(len(annotated_tokens))
    #
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
    updated_tokens = {token: counter for (token, counter) in annotated_tokens.items() if counter > 9}
    print(len(updated_tokens))
    f = open("resources/" + element + "_10.txt", "w")
    for token in updated_tokens.keys():
        f.write(token + '\n')
    updated_tokens = {token: counter for (token, counter) in annotated_tokens.items() if counter > 14}
    print(len(updated_tokens))
    f = open("resources/" + element + "_15.txt", "w")
    for token in updated_tokens.keys():
        f.write(token + '\n')
    updated_tokens = {token: counter for (token, counter) in annotated_tokens.items() if counter > 19}
    print(len(updated_tokens))
    f = open("resources/" + element + "_20.txt", "w")
    for token in updated_tokens.keys():
        f.write(token + '\n')



import csv


def tokenize(param):
    post_list = []
    with open("get_data/" + param + ' posts with Date.csv', newline='', encoding="utf8") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            post_list.append(row[7])
    # print(post_list)

    data = []
    for element in post_list:
        data.append(
            element.lower().replace(', ', ' ').replace(': ', ' ').replace("[", '').replace("]", '')
                .replace('“', '').replace('”', '').replace("\n", '').replace("\\", '')
                .replace("*", '').replace("(", '').replace(")", '').replace("/", ' ').replace("-", '').replace("?", '.')
                .replace("!", '.').replace(':', '').replace("'", '')
                .replace("’s", ' is').replace("'s", ' is').replace("’re", ' are').replace("can’t", 'can not')
                .replace("n't", ' not').replace("'m", ' am').replace("’m", ' am').replace("’d", ' would')
                .replace("'d", ' would').replace("'ll", ' will').replace("’ve", ' have').replace("etc.", 'et cetera')
                .replace("y’all", 'you all').replace("didn't", 'did not').replace("  ", ' ').replace("   ", ' ')
                .__add__("*")


        )
    # print(data)
    tokenized_posts = []
    for entry in data:
        #data_string = ''.join(data)
        submission_list = entry.split("*")
        # print(submission_list)
        sentences = [i.split('.') for i in submission_list]
        # print(sentences)
        words = [t.split(' ') for j in sentences for t in j]
        #print(words[2:])
        tokenized_posts.append(words)
    # print(tokenized_posts)
    # with open("get_data/tokenized_data/" + param + " tokenized.txt", "w", encoding="utf8") as w:
    #     for ele in tokenized_posts:
    #         w.writelines('%s\n' % ele)
    # w.close()
    return tokenized_posts





if __name__ == '__main__':
    # tokenize('Not the A-hole')
    tokenize('Everyone Sucks')
    # tokenize('Asshole')

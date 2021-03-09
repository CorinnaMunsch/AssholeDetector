import csv
import re
import pandas as pd


def load_data(param):

    AITA_data = pd.read_csv(param + ' posts.csv')
    print(AITA_data.to_string())
    # data = []
    # # nm_comments = []
    # # stories = []
    #
    # with open(param + '.csv', newline='') as datafile:
    #     csv_reader = csv.reader(datafile, delimiter=',')
    #     for row in csv_reader:
    #         data.append(row)
    #
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


if __name__ == '__main__':
    load_data('Everyone Sucks')
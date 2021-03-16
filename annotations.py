import re

def get_mixed_annotations() -> list:
    with open("support/SentimentWordswithcomma.txt", encoding='utf-8') as f:
        content = [line.strip('\n') for line in f.readlines() if not line.startswith('%%')]

    parsed_list = []
    for element in content:
        parsed_element = element.split(',')
        lowercase = parsed_element[0].lower()
        annotation = parsed_element[1].split('=')
        parsed_list.append([lowercase, annotation])

    cleaned_list = [element for element in parsed_list if element[1][0] not in ["NEU", "INT", "SHI"]]
    sentiment = None
    sentiment_list = []
    for element in cleaned_list:
        if element[1][0] == "POS":
            sentiment = element[1][1]
        elif element[1][0] == "NEG":
            sentiment = '-' + element[1][1]
        sentiment_list.append([element[0], sentiment])
    #print(sentiment_list)
    # with open("sentilist.txt", "w") as w:
    #     for ele in sentiment_list:
    #         w.writelines('%s\n' % ele)
    return sentiment_list


if __name__ == "__main__":
    get_mixed_annotations()
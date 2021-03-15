import re


def get_annotations(param: str) -> list:

    with open("support/" + param + ".txt", encoding='utf-8') as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    # print()
    parsed_list = []
    for element in content:
        # remove elements after |
        element = re.sub(r'\|[A-Za-z]+', '', element)
        element = element.split()

        if len(element) == 3:
            element[0] = element[0] + ',' + element[2]
            element.pop(2)
        parsed_list.append(element)

    return parsed_list


def get_mixed_annotations() -> list:
    with open("support/SentimentWords.txt", encoding='utf-8') as f:
        content = [line.strip('\n') for line in f.readlines() if not line.startswith('%%')]

    parsed_list = []
    for element in content:
        parsed_element = element.split()
        lowercase = parsed_element[0].lower()
        annotation = parsed_element[1].split('=')
        parsed_list.append([lowercase, annotation])

    cleaned_list = [element for element in parsed_list if element[1][0] not in ["NEU", "INT", "SHI"]]

    sentiment_list = []
    for element in cleaned_list:
        if element[1][0] == "POS":
            sentiment = element[1][1]
        elif element[1][0] == "NEG":
            sentiment = '-' + element[1][1]
        sentiment_list.append([element[0], sentiment])
    return sentiment_list
    #print(sentiment_list)


def get_sentiments():
    mixed = get_mixed_annotations()
    old = get_annotations("positive") + get_annotations("negative")
    updated_list = []
    for new_element in mixed:
        for element in old:
            if new_element[0] in element[0].split(','):
                # print("*************")
                # print(new_element)
                # print(element)
                new_score = (float(new_element[1])+float(element[1]))/2
                # print(new_score)
                updated_list.append([element[0], str(new_score)])
        if not any(new_element[0] in element[0].split(',') for element in old):
            updated_list.append([new_element[0].replace('_', ' '), new_element[1]])
    return updated_list


if __name__ == "__main__":
    get_sentiments()

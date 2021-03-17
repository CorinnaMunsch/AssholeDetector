import matplotlib.pyplot as plt
from collections import Counter

def import_data(param):
    with open('resources/' + param + '.txt', newline='') as f:
        lines = f.readlines()
        values = [float(line.split()[0]) for line in lines]
        values.sort()
        return values


def count_instances(imported_data):
    all_the_entries = imported_data.__len__()
    print(imported_data)
    print('Entries in this list:')
    print(all_the_entries)
    # counted_instances_list = Counter(imported_data)

    count_very_positive = sum(i > 0.5 for i in imported_data)
    count_positive = sum((i < 0.5) and (i > 0) for i in imported_data)
    count_neutral = imported_data.count(0.0)
    count_very_negative = sum(i < -0.5 for i in imported_data)
    count_negative = sum((i > -0.5) and (i < 0) for i in imported_data)

    print('Very Positive Instances:')
    print(count_very_positive)
    print('Positive Instances:')
    print(count_positive)
    print('Neutral Instances:')
    print(count_neutral)
    print('Negative Instances:')
    print(count_negative)
    print('Very Negative Instances:')
    print(count_very_negative)

    print('\n')

    percentage_very_positive = count_very_positive/all_the_entries*100
    print('Percentage very positive:')
    print("%.2f" % percentage_very_positive)
    percentage_positive = count_positive/all_the_entries*100
    print('Percentage positive:')
    print("%.2f" % percentage_positive)
    percentage_neutral = count_neutral/all_the_entries * 100
    print('Percentage neutral:')
    print("%.2f" % percentage_neutral)
    percentage_negative = count_negative/all_the_entries*100
    print('Percentage negative:')
    print("%.2f" % percentage_negative)
    percentage_very_negative = count_very_negative/all_the_entries*100
    print('Percentage very negative:')
    print("%.2f" % percentage_very_negative)
    #print(counted_instances_list)

    percentage_list = ["%.2f" % percentage_very_positive, "%.2f" % percentage_positive, "%.2f" % percentage_neutral, "%.2f" % percentage_negative, "%.2f" % percentage_very_negative]
    #percentage_list.append(, )
    print(percentage_list)
    return percentage_list


def piechart(list):

        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = '0,5 bis 1 | sehr positiv', '0 bis 0,5 | positiv', '0 | neutral', '-0,5 bis 0 | negativ', '-1 bis -0,5 | sehr negativ'
    explode = (0, 0.1, 0, 0, 0)  # only "explode" the 2nd slice

    fig1, ax1 = plt.subplots()
    ax1.pie(list, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title('Prozent der Tweets')
    plt.show()


if __name__ == '__main__':
    import_data('frauenquote')
    count_instances(import_data('frauenquote'))
    piechart(count_instances(import_data('frauenquote')))


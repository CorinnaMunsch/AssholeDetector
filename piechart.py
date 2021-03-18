import matplotlib.pyplot as plt
from collections import Counter

def import_data(param):
    with open('resources/' + param + ' sentiments.txt', newline='') as f:
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

    count_very_positive = sum(i > 0.1 for i in imported_data)
    count_positive = sum((i < 0.1) and (i > 0) for i in imported_data)
    count_neutral = imported_data.count(0.0)
    count_negative = sum((i > -0.1) and (i < 0) for i in imported_data)
    count_very_negative = sum(i < -0.1 for i in imported_data)

    print('Score of 0.1 and higher:')
    print(count_very_positive)
    print('Score between 0.1 & 0:')
    print(count_positive)
    print('Score of 0:')
    print(count_neutral)
    print('Score between 0 & -0.1 :')
    print(count_negative)
    print('Score of -0.1 and lower:')
    print(count_very_negative)

    print('\n')

    percentage_very_positive = count_very_positive/all_the_entries*100
    print('Score of 0.1 and higher:')
    print("%.2f" % percentage_very_positive)
    percentage_positive = count_positive/all_the_entries*100
    print('Score between 0.1 & 0:')
    print("%.2f" % percentage_positive)
    percentage_neutral = count_neutral/all_the_entries * 100
    print('Score of 0:')
    print("%.2f" % percentage_neutral)
    percentage_negative = count_negative/all_the_entries*100
    print('Score between 0 & -0.1 :')
    print("%.2f" % percentage_negative)
    percentage_very_negative = count_very_negative/all_the_entries*100
    print('Score of -0.1 and lower:')
    print("%.2f" % percentage_very_negative)
    #print(counted_instances_list)

    percentage_list = ["%.2f" % percentage_very_positive, "%.2f" % percentage_positive, "%.2f" % percentage_neutral, "%.2f" % percentage_negative, "%.2f" % percentage_very_negative]
    #percentage_list.append(, )
    print(percentage_list)
    return percentage_list


def piechart(list):

        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Score of 0.1 and higher', 'Score between 0.1 & 0', 'Score of 0', 'Score between 0 & -0.1', 'Score of -0.1 and lower'
    explode = (0.2, 0, 0, 0, 0)  # only "explode" the 2nd slice

    fig1, ax1 = plt.subplots()
    ax1.pie(list, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title('Prozent der Posts')
    plt.show()


if __name__ == '__main__':
    # piechart(count_instances(import_data('Everyone Sucks')))
    # piechart(count_instances(import_data('Asshole')))
    piechart(count_instances(import_data('Not the A-hole')))


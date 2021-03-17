import numpy as np


def print_statistics(param):
    with open('resources/' + param + ' sentiments.txt', newline='') as f:
        lines = f.readlines()
    sentiments = np.array([float(line.split()[0]) for line in lines])
    print(f"Median (50-percentile): {np.median(sentiments)}")
    print(f"Average: {np.average(sentiments)}")
    print(f"Mean: {np.mean(sentiments)}")
    print(f"Variance: {np.var(sentiments)}")
    print(f"Standard Deviation: {np.std(sentiments)}")


if __name__ == '__main__':

    for elem in ['Everyone Sucks', 'Asshole', 'Not the A-hole']:
        print(f"--------------------- Statistiken {elem} -------------------")
        print_statistics(elem)
        print("-------------------------------------------------------------\n")

import matplotlib.pyplot as plt
import datetime as dt
# import matplotlib.colors
import numpy as np


def sp(param):
    with open('resources/' + param + ' sentiments.txt', newline='') as f:
        lines = f.readlines()
        parsed = [line.split() for line in lines]
        y = [float(elem[0]) for elem in parsed]

        # dates = [elem[1] + " " + elem[2] for elem in parsed]
        # # print(dates)
        # new = [dt.datetime.strptime(elem, '%Y-%m-%d %H:%M:%S') for elem in dates]
        # # print(new)
        x = np.random.rand(27)
        # [dt.datetime.strptime(elem, '%Y-%m-%d %H:%M:%S') for elem in dates]

    plt.scatter(y, x, marker='+', label='Posts')
    plt.title(param)
    plt.ylim(-1.0, 1.0)
    plt.xlim(0, 27)
    plt.xlabel('Post Number')
    plt.ylabel('Sentiment Score')

    plt.show()

    # axes = plt.gca()
    # axes.set_ylim([-1.0, 1.0])
    # plt.axis(None, None, -1, 1)
    # plt.plot(range(19))
    # plt.ylim(-1, 1)
    # bewertungs_scala = [-1.0, -0.9, -0.8]
    # fig, ax = plt.subplots(figsize=(10, 6))
    # ax.plot(x, bewertungs_scala)
    # marker = itertools.cycle((',', '+', '.', 'o', '*'))
    # fig = plt.figure()
    # plt.gca().set_prop_cycle(maker=[',', '+', '.', 'o', '*'])
    # for q,p in zip(x,y):
    #     plt.plot(q,p, linestyle = '')
    # values = [-1.0, -0.9, -0.8]
    # , '-0,7', '-0,6', '-0,5', '-0,4', '-0,3', '-0,2', '-0,1', '0', '0,1', '0,2', '0,3', '0,4', '0,5', '0,6', '0,7', '0,8', '0,9', '1,0']
    # plt.colorbar()


if __name__ == '__main__':
    sp('Everyone Sucks')
    # sp('Asshole')

# -*- coding: utf-8 -*

import matplotlib.pyplot as plt


def demo_pic():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    plt.axis([0, 6, 0, 20])
    plt.show()


demo_pic()
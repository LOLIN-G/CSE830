import numpy as np
import math, random
from time import time
from copy import deepcopy
from matplotlib import pyplot as plt
from utils import *

# Q2:
N = [10, 100, 200, ] # length of array
T = 200
K = 100 # repeat K times run for each array

times = []
try:
    for n in N:
        subtimes = []
        arr = list(np.random.randint(0, n, size=n))
        for t in range(T):
            time_ = time()
            for k in range(K):
                arr_ = deepcopy(arr)
                TimSort(arr_, t=t)
            time_ = time() - time_
            subtimes.append(time_)
            print('n:%d\tt:%d\ttime:%.4f' % (n, t, time_))
        times.append(subtimes)
except:
    for subtimes in times:
        x = list(range(len(subtimes)))
        plt.plot(x, subtimes)
    plt.xlabel('k')
    plt.ylabel('Time (100 runs)')
    plt.savefig('./Q2.pdf')
else:
    legends = []
    for i, subtimes in enumerate(times):
        legends.append('N= %d' % N[i])
        x = list(range(len(subtimes)))
        plt.plot(x, subtimes)
    plt.xlabel('k')
    plt.ylabel('Time (100 runs)')
    plt.legend(legends)
    plt.savefig('./Q2.pdf')

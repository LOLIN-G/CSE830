import numpy as np
import math, random
from time import time
from copy import deepcopy
from matplotlib import pyplot as plt
from utils import *

# Q2:
# N = [10, 100, 200, ] # length of array
N = 200
T = [2, 5, 10, 20, 50, 100, 120, 150, 200]
K = 100 # repeat K times run for each array

times = []
try:
    for t in T:
        subtimes = []
        for n in range(N):
            arr = list(np.random.randint(0, n, size=n))
            time_ = time()
            for k in range(K):
                arr_ = deepcopy(arr)
                TimSort(arr_, t=t)
            time_ = time() - time_
            subtimes.append(time_)
            print('n:%d\tt:%d\ttime:%.4f' % (n, t, time_))
        times.append(subtimes)
except:
    legends = []
    for i, subtimes in enumerate(times):
        x = list(range(len(subtimes)))
        legends.append('k= %d' % T[i])
        plt.plot(x, subtimes)
    plt.legend(legends)
    plt.xlabel('n')
    plt.ylabel('Time (100 runs)')
    plt.savefig('./Q2.pdf')
else:
    legends = []
    for i, subtimes in enumerate(times):
        legends.append('k= %d' % T[i])
        x = list(range(len(subtimes)))
        plt.plot(x, subtimes)
    plt.xlabel('n')
    plt.ylabel('Time (100 runs)')
    plt.legend(legends)
    plt.savefig('./Q2.pdf')

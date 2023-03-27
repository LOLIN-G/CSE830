import numpy as np
import math, random
from time import time
from copy import deepcopy
from matplotlib import pyplot as plt
from utils import *

# Q1:
N = [10, 100, 1000, 10000, 100000] # length of array
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
    plt.xlabel('t')
    plt.ylabel('Time (100 runs)')
    plt.savefig('./Q2.pdf')

    with open('./Q2.log', 'w+') as f:
        f.write('Len\ttime\n')
        for i in x:
            f.write('%d\t%f\t%f\n' % (i, time4merge[i], time4insert[i]))
    












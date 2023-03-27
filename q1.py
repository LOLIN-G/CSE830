import numpy as np
import math, random
from time import time
from copy import deepcopy
from matplotlib import pyplot as plt
from utils import *

# Q1:
N = 200 # length of array
K = 100 # repeat K times run for each array

time4merge, time4insert = [], []
try:
	for n in range(1, N+1):
		arr4merge = list(np.random.randint(0, n, size=n))
		arr4insert = deepcopy(arr4merge[:])

		time4merge_ = time()
		for k in range(K):
			arr4merge_ = deepcopy(arr4merge)
			mergeSort(arr4merge_, l=0, r=n-1)
		time4merge_ = time() - time4merge_
		time4merge.append(time4merge_)

		time4insert_ = time()
		for k in range(K):
			arr4insert_ = deepcopy(arr4insert)
			insertionSort(arr4insert_)
		time4insert_ = time() - time4insert_
		time4insert.append(time4insert_)
		
		print('%d\t%.4f\t%.4f' % (n, time4merge_, time4insert_))
except:
	L = min(len(time4insert), len(time4merge))
	x = list(range(L))
	plt.plot(x, time4merge[:L])
	plt.plot(x, time4insert[:L])
	plt.xlabel('Length of array')
	plt.ylabel('Time (100 runs)')
	plt.legend(['Time4MergeSort', 'Time4InsertSort'])
	plt.savefig('./Q1.pdf')

	with open('./Q1.log', 'w+') as f:
		f.write('Len\tt(merge)\tt(insert)\n')
		for i in x:
			f.write('%d\t%f\t%f\n' % (i, time4merge[i], time4insert[i]))
else:	
	L = min(len(time4insert), len(time4merge))
	x = list(range(L))
	plt.plot(x, time4merge[:L])
	plt.plot(x, time4insert[:L])
	plt.xlabel('Length of array')
	plt.ylabel('Time (100 runs)')
	plt.legend(['Time4MergeSort', 'Time4InsertSort'])
	plt.savefig('./Q1.pdf')

	with open('./Q1.log', 'w+') as f:
		f.write('Len\tt(merge)\tt(insert)\n')
		for i in x:
			f.write('%d\t%f\t%f\n' % (i, time4merge[i], time4insert[i]))












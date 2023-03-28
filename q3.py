import numpy as np
import math, random
from time import time
from copy import deepcopy
from matplotlib import pyplot as plt
from utils import *

# Q3:

# from chatgpt
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            current = self.root
            while True:
                if key == current.key:
                    current.value = value
                    return
                elif key < current.key:
                    if current.left is None:
                        current.left = Node(key, value)
                        return
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(key, value)
                        return
                    else:
                        current = current.right

tree_times, dict_times = [], []
try:
    for j in range(1000000000):
        tree = BinaryTree()
        dic = dict()

        N = list(range(j))
        random.shuffle(N)

        tree_time = time()
        for i in N:
            tree.insert(i, i)
        tree_time = time() - tree_time
        tree_times.append(tree_time)

        dict_time = time()
        for i in N:
            dic[i] = i
        dict_time = time() - dict_time
        dict_times.append(dict_time)

        print('Tree time:%f\nDict time:%f' % (tree_time, dict_time))
except:
    x_axis = list(range(min(len(dict_times), len(tree_times))))
    plt.plot(x_axis, dict_times[:len(x_axis)])
    plt.plot(x_axis, tree_times[:len(x_axis)])
    plt.legend(['Hash table', 'Binary tree'])
    plt.savefig('./Q3.pdf')
    plt.close()

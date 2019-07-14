import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import multiprocessing
from multiprocessing import Process
import os

def test(x,i):
    x[i] = os.getpid()
    return x

x = [0,0,0,0]
procs = []

for i in range(4):
    proc = Process(target=test, args=(x,i))
    procs.append(proc)
    proc.start()

for i in procs:
    proc.join()

print(x)
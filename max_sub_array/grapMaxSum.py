from maxSumSub import *
import random
from time import time
import matplotlib.pyplot as plt

n = []
naive = []
dc = []
kadane = []

for i in range(5,205,5):
    n.append(i)
    arr = [random.randint(-100,100) for j in range(i)]
    #Naive
    inicio = time()
    maxSubArraySumNaive(arr)
    final = time()
    naive.append(final-inicio)
    #dc
    inicio = time()
    maxSubArraySumDC(arr,0,len(arr)-1)
    final = time()
    dc.append(final-inicio)
    #kadane
    inicio = time()
    maxSubArraySumKadane(arr,len(arr))
    final = time()
    kadane.append(final-inicio)

plt.plot(n, naive, label='naive')
plt.plot(n, dc, label='divide')
plt.plot(n, kadane, label='kadane')
plt.legend()
plt.savefig('fig')
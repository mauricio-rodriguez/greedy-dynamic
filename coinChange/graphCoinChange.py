from coinChange import *
from random import randint, sample
from time import time
import matplotlib.pyplot as plt


rec = []
dp = []
l_i = []

for i in range(1,25):
    l_i.append(i)
    arr = sample([x for x in range(1,i+1)],i)
    arr.sort()
    n = max(arr)

    #Recursive
    inicio = time()
    coinChangeRecursive(arr,0,n)
    final = time()
    rec.append(final-inicio)

    #DP
    inicio = time()
    coinChangeWaysDP(arr,len(arr),n)
    final = time()
    dp.append(final-inicio)

plt.plot(l_i, rec, label="Recursive")
plt.plot(l_i, dp, label="Dynamic")
plt.legend()
plt.savefig("coin")




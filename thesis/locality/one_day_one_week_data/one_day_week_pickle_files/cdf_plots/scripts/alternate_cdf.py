from __future__ import division
import pickle
import numpy as np
import matplotlib.pyplot as plt
import sys

a = open(sys.argv[1],'rb') # A pickle file of the form {'keyword':score(integer), ...}

p = pickle.load(a)
y = []

temp = []

for word in p:
    temp.append(p[word])


x = set(temp)

for i in x:
    if len(y) == 0:
        y.append(temp.count(i)/len(temp))
    else:
        y.append(temp.count(i)/len(temp) + y[-1])

plt.plot(list(x),y,'x')
plt.show()

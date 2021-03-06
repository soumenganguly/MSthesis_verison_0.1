from __future__ import division
import pickle
import sys
import matplotlib.pyplot as plt
import numpy as np

a=open(sys.argv[1],'rb')

p=pickle.load(a)

x = []
y = []
for word in p:
    if p[word][2] <= 10 and p[word][3] <=10:
        continue
    else:
        x.append(p[word][2])
        y.append(p[word][3])

x_y = []

for score in range(len(x)):
    if x[score] == 0 and y[score] != 0:
        x[score] = 1
    elif y[score] == 0 and x[score]!= 0:
        y[score] = 1
    x_y.append(x[score]/y[score])

sorted_data = np.sort(x_y)

yvals=np.arange(len(sorted_data))/float(len(sorted_data)-1)

plt.plot(sorted_data,yvals, label='PUL vs. UMB')
plt.legend()
plt.xscale('log')
plt.xlabel('Popularity of keyword in PUL / Popularity of keyword in UMB')
plt.ylabel('CDF')
plt.grid()

plt.show()

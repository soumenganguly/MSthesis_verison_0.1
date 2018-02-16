from __future__ import division
import pickle
import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ks_2samp

a=open(sys.argv[1],'rb') # different populations
b = open(sys.argv[2],'rb')
c = open(sys.argv[3],'rb')
d = open(sys.argv[4],'rb')
e = open(sys.argv[5],'rb')
f = open(sys.argv[6],'rb')
g = open(sys.argv[7],'rb') # Same populations
h = open(sys.argv[8],'rb')
i = open(sys.argv[9],'rb')
j = open(sys.argv[10],'rb')

p1=pickle.load(a)
p2 = pickle.load(b)
p3 = pickle.load(c)
p4 = pickle.load(d)
p5 = pickle.load(e)
p6 = pickle.load(f)
p7 = pickle.load(g)
p8 = pickle.load(h)
p9 = pickle.load(i)
p10 = pickle.load(j)

x_i = []
y_i = []

x_j = []
y_j = []

x_k = []
y_k = []

x_l = []
y_l = []

x_m = []
y_m = []

x_n = []
y_n = []

x_o = []
y_o = []

x_p = []
y_p = []

x_q = []
y_q = []

x_r = []
y_r = []



for word in p1:
    if p1[word][0] <=10 and p1[word][1] <=10:
        continue
    else:
        x_i.append(p1[word][0])
        y_i.append(p1[word][1])

for word in p2:
    if p2[word][0] <=10 and p2[word][1] <=10:
        continue
    else:
        x_j.append(p2[word][0])
        y_j.append(p2[word][1])

for word in p3:
    if p3[word][0] <=10 and p3[word][1] <=10:
        continue
    else:
        x_k.append(p3[word][0])
        y_k.append(p3[word][1])

for word in p4:
    if p4[word][0] <=10 and p4[word][1] <=10:
        continue
    else:
        x_l.append(p4[word][0])
        y_l.append(p4[word][1])

for word in p5:
    if p5[word][0] <=10 and p5[word][1] <=10:
        continue
    else:
        x_m.append(p5[word][0])
        y_m.append(p5[word][1])

for word in p6:
    if p6[word][0] <=10 and p6[word][1] <=10:
        continue
    else:
        x_n.append(p6[word][0])
        y_n.append(p6[word][1])

for word in p7:
    if p7[word][0] <=10 and p7[word][1] <=10:
        continue
    else:
        x_o.append(p7[word][0])
        y_o.append(p7[word][1])

for word in p8:
    if p8[word][0] <=10 and p8[word][1] <=10:
        continue
    else:
        x_p.append(p8[word][0])
        y_p.append(p8[word][1])

for word in p9:
    if p9[word][0] <=10 and p9[word][1] <=10:
        continue
    else:
        x_q.append(p9[word][0])
        y_q.append(p9[word][1])

for word in p10:
    if p10[word][0] <=10 and p10[word][1] <=10:
        continue
    else:
        x_r.append(p10[word][0])
        y_r.append(p10[word][1])



x_y_i = [] # Different location
x_y_j = [] 
x_y_k = []
x_y_l = []
x_y_m = []
x_y_n = []
x_y_o = [] # Samples from same population
x_y_p = []
x_y_q = []
x_y_r = []

for score in range(len(x_j)):
    if x_j[score] == 0 and y_j[score] != 0:
        x_j[score] = 1
    elif y_j[score] == 0 and x_j[score]!= 0:
        y_j[score] = 1
    x_y_j.append(x_j[score]/y_j[score])

for score in range(len(x_k)):
    if x_k[score] == 0 and y_k[score] != 0:
        x_k[score] = 1
    elif y_k[score] == 0 and x_k[score] != 0:
        y_k[score] = 1
    x_y_k.append(x_k[score]/y_k[score])

for score in range(len(x_i)):
    if x_i[score] == 0 and y_i[score] != 0:
        x_i[score] = 1
    elif y_i[score] == 0 and x_i[score]!= 0:
        y_i[score] = 1
    x_y_i.append(x_i[score]/y_i[score])

for score in range(len(x_l)):
    if x_l[score] == 0 and y_l[score] != 0:
        x_l[score] = 1
    elif y_l[score] == 0 and x_l[score]!= 0:
        y_l[score] = 1
    x_y_l.append(x_l[score]/y_l[score])

for score in range(len(x_m)):
    if x_m[score] == 0 and y_m[score] != 0:
        x_m[score] = 1
    elif y_m[score] == 0 and x_m[score]!= 0:
        y_m[score] = 1
    x_y_m.append(x_m[score]/y_m[score])

for score in range(len(x_n)):
    if x_n[score] == 0 and y_n[score] != 0:
        x_n[score] = 1
    elif y_n[score] == 0 and x_n[score]!= 0:
        y_n[score] = 1
    x_y_n.append(x_n[score]/y_n[score])

for score in range(len(x_o)):
    if x_o[score] == 0 and y_o[score] != 0:
        x_o[score] = 1
    elif y_o[score] == 0 and x_o[score]!= 0:
        y_o[score] = 1
    x_y_o.append(x_o[score]/y_o[score])

for score in range(len(x_p)):
    if x_p[score] == 0 and y_p[score] != 0:
        x_p[score] = 1
    elif y_p[score] == 0 and x_p[score]!= 0:
        y_p[score] = 1
    x_y_p.append(x_p[score]/y_p[score])

for score in range(len(x_q)):
    if x_q[score] == 0 and y_q[score] != 0:
        x_q[score] = 1
    elif y_q[score] == 0 and x_q[score]!= 0:
        y_q[score] = 1
    x_y_q.append(x_q[score]/y_q[score])

for score in range(len(x_r)):
    if x_r[score] == 0 and y_r[score] != 0:
        x_r[score] = 1
    elif y_r[score] == 0 and x_r[score]!= 0:
        y_r[score] = 1
    x_y_r.append(x_r[score]/y_r[score])



sorted_data_i = np.sort(x_y_i)
sorted_data_j = np.sort(x_y_j)
sorted_data_k = np.sort(x_y_k)
sorted_data_l = np.sort(x_y_l)
sorted_data_m = np.sort(x_y_m)
sorted_data_n = np.sort(x_y_n)
sorted_data_o = np.sort(x_y_o)
sorted_data_p = np.sort(x_y_p)
sorted_data_q = np.sort(x_y_q)
sorted_data_r = np.sort(x_y_q)

yvals_i=np.arange(len(sorted_data_i))/float(len(sorted_data_i)-1)
yvals_j = np.arange(len(sorted_data_j))/float(len(sorted_data_j)-1)
yvals_k = np.arange(len(sorted_data_k))/float(len(sorted_data_k)-1)
yvals_l = np.arange(len(sorted_data_l))/float(len(sorted_data_l)-1)
yvals_m = np.arange(len(sorted_data_m))/float(len(sorted_data_m)-1)
yvals_n = np.arange(len(sorted_data_n))/float(len(sorted_data_n)-1)
yvals_o = np.arange(len(sorted_data_o))/float(len(sorted_data_o)-1)
yvals_p = np.arange(len(sorted_data_p))/float(len(sorted_data_p)-1)
yvals_q = np.arange(len(sorted_data_q))/float(len(sorted_data_q)-1)
yvals_r = np.arange(len(sorted_data_r))/float(len(sorted_data_r)-1)

'''
KS-test
diff_location_ks = ks_2samp(x_y_i, x_y_j)
same_location_ks = ks_2samp(x_y_j, x_y_k)

print diff_location_ks
print same_location_ks
'''

markers_on = [0.1]
plt.plot(sorted_data_i,yvals_i, 'b--*', markevery=0.1, label='ISP-City2-b vs. ISP-City1')
plt.plot(sorted_data_j,yvals_j, 'c--+', markevery=0.1, label='ISP-City2-b vs. Campus-City2')
plt.plot(sorted_data_k,yvals_k, 'm--o', markevery=0.1, label='ISP-City2-b vs. ISP-City2-a')
plt.plot(sorted_data_l,yvals_l, 'y--x', markevery=0.1, label='ISP-City1 vs. Campus-City2')
plt.plot(sorted_data_m,yvals_m, 'k--s', markevery=0.1, label='ISP-City1 vs. ISP-City2-a')
plt.plot(sorted_data_n,yvals_n, '-->', markevery=0.1, label='Campus-City2 vs. ISP-City2-a')
plt.plot(sorted_data_o,yvals_o, ':', markevery=0.1, label='ISP-City2-b vs. ISP-City2-b')
plt.plot(sorted_data_p,yvals_p, '--', markevery=0.1, label='ISP-City1 vs. ISP-City1')
plt.plot(sorted_data_q,yvals_q, 'g-.,', markevery=0.1,label='Campus-City2 vs. Campus-City2')
plt.plot(sorted_data_r,yvals_r, 'r-', markevery=0.1,label='ISP-City2-a vs. ISP-City2-a')
# plt.annotate('p-value = '+str(diff_location_ks[1]),xy=(0.005,0.6))
# plt.annotate('p-value = '+str(same_location_ks[1]),xy=(10,0.6))

plt.legend(loc=4)

plt.grid()

plt.xlabel('keyword popularity ratio', fontsize=18)
plt.ylabel('CDF', fontsize=22)
plt.xscale('log')

plt.show()

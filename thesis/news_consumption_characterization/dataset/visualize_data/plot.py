import pickle
import matplotlib.pyplot as plt
import sys

o = open("cord_dict.pkl","rb")
p = pickle.load(o)

title = sys.argv[1]

plt.plot(p['x'],p['y'],'ro')
plt.axis([0,4,1,12])
plt.xticks(range(1,3),('2015','2016'))
plt.yticks(range(1,13),('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
plt.title(title)
plt.show()

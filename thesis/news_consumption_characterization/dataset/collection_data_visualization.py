import pickle
import datetime
import matplotlib.pyplot as plt

file_open = open(,"rb")
pickle_file = pickle.load(file_open)

x = []
y = []

for values in pickle_file.values():
    for v in values:
        month = datetime.fromtimestamp(float(v[2]))
        x.append(1)
        y.append(month.month)

plt.plot(x,y)
plt.show()

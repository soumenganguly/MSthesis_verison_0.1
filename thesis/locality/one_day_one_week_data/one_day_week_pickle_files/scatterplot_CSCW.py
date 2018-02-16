import matplotlib.pyplot as plt
import numpy as np
import pylab as pylab
import pickle as pickle
from scipy.stats import pearsonr

plt.rc('font', size=18, family="serif")
plt.rc('text', usetex=True)

#change umb and poli as you whish 
#change oneday/oneweek
#don't forget to change the output in savefig
pic = pickle.load(open('UMB_POLI_oneday.pkl', 'rb'))
pos = {}
gn = np.array([pic[x][0] for x in pic.keys()])
po = np.array([pic[x][1] for x in pic.keys()])
gn95 = np.max(gn)
po95 = np.max(po)

normgn = []
normpo = []
for x in zip(gn, po):
	if x[0] <= gn95 and x[1] <= po95:
		normgn.append(x[0])
		normpo.append(x[1])
fig, ax = plt.subplots(figsize=(4,4))
ax.scatter(normgn, normpo, color='black', alpha=0.1, s=50, edgecolor=None)
ax.text(-0.0, 1.03, s='Pearson coeff. = %.4f' % float(pearsonr(normgn, normpo)[0]),  transform=ax.transAxes, fontsize=18)
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('axes', -0.05))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('axes', -0.03))
ax.set_ylabel(r'Popularity in ISP-Turin1')
ax.set_xlabel(r'Popularity in ISP-Campus')
ax.set_xlim([-0.05,100])
ax.set_ylim([-0.05,100])
plt.tight_layout()
fig.savefig("UMB_POLI_oneday_cscw.png")

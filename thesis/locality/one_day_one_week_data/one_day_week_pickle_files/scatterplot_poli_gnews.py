import matplotlib.pyplot as plt
import numpy as np
import pylab as pylab
import pickle as pickle
from scipy.stats import pearsonr

plt.rc('font', size=18, family="serif")
plt.rc('text', usetex=True)

#pic = pickle.load(open('PUL_keyword_pop_pop.pkl', 'rb') , encoding='ascii', errors='ignore')
pic2 = pickle.load(open('keywords_gnews_politonews_all.pkl', 'rb'))
pic ={}
for key in pic2:
	if pic2[key][0]==0 or pic2[key][1]==0:
		continue
	pic[key]=pic2[key]

#print(pic)
pos = {}
gn = np.array([pic[x][0] for x in pic.keys()])
po = np.array([pic[x][1] for x in pic.keys()])
# gn95 = np.percentile(gn, 99)
# po95 = np.percentile(po, 99)
gn95 = np.max(gn)
po95 = np.max(po)

normgn = []
normpo = []
for x in zip(gn, po):
	if x[0] <= gn95 and x[1] <= po95:
		normgn.append(x[0])
		normpo.append(x[1])

# normpo = np.array(normpo)/po95
# normgn = np.array(normgn)/gn95
# print([ xy for xy in zip(gn,po)])
fig, ax = plt.subplots(figsize=(4,4))
#print(pearsonr(normgn, normpo))
# intersecgn = []
# intersecpo = []
# for key in pic.keys():
# 	if pic[key][0] > 0 and pic[key][1] > 0:
# 		intersecgn.append(pic[key][0])
# 		intersecpo.append(pic[key][1]) 
# print(pearsonr(intersecgn, intersecpo))
ax.scatter(normgn, normpo, color='black', alpha=0.1, s=50, edgecolor=None)
ax.text(-0.0, 1.03, s='Pearson coeff. = %.4f' % float(pearsonr(normgn, normpo)[0]),  transform=ax.transAxes, fontsize=18)
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('axes', -0.05))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('axes', -0.03))
# ax.set_xscale("log")
# ax.set_yscale("log")
# ax.set_xscale("log")
# plt.yticks(x1, labels,  fontsize=20)
# ax.set_ylabel(r'Extensions')
ax.set_ylabel(r'Frequency in Google News')
ax.set_xlabel(r'Frequency in Campus')
ax.set_xlim([-0.05,100])
ax.set_ylim([-0.05,100])
# ax.set_xlim(xmin=0)
# ax.set_ylim(ymin=0)
# leg = ax.legend(loc='lower right', prop={'size': 24}, frameon=None)
# leg.draw_frame(False)

plt.tight_layout()
# plt.show()

fig.savefig("GNEWS_POLI_oneweek.png")
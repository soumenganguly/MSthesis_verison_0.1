import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

## the data
N = 15
pdf = [1.98450316383, 14.0906204446, 7.44559475817, 12.8576797561, 7.5482158191, 6.11444888218,1.42176728059, 6.01033986387, 4.33777976599, 3.6710788603, 1.50230897387, 3.68509445889,16.8957081069, 2.55194291235, 0]
poli = [1.57920267811,17.5940502928, 5.9940403423,12.1433800534, 6.09381219082, 9.05533917098, 1.12956302951, 2.38715030989, 3.58370173992, 3.01252345482, 0, 5.44080855177,20.0276660317, 2.92287982601,1.40026103618]
pul = [1.86773606317, 15.8181198917, 6.66954470841, 12.0117856361, 7.8360475555, 6.97657717859, 0, 4.85727435388, 4.03610894821, 3.47161028227, 2.63857708955,3.90466734841, 16.6474314787, 2.60677803641,1.48396187525]
umb = [1.88003515094, 17.4110057783, 7.84452583054, 11.9126577742, 7.68043084446, 9.03504293226, 1.14105541182,3.70643566544,3.23796104923, 3.55375491549, 0, 4.19565228064, 15.8857938172, 2.42399100607,1.27004855346]

## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.20                     # the width of the bars

## the bars
rects1 = ax.bar(ind, pdf, width,
                color='blue')

rects2 = ax.bar(ind+width, poli, width,
                    color='green')

rects3 = ax.bar(ind+2*width, pul, width,
                color='red')

rects4 = ax.bar(ind+3*width, umb, width,
                color='black')


# axes and labels
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(0,100)
ax.set_ylabel('% of visits')
ax.set_title('% of views of categories in 4 locations')
xTickMarks = ['Automobile','Crime','Economics',"Editor's column",'Entertainment','Foriegn','Health','People','Photo gallery','Politics','Regional','Science','Sport','Technology','Travel']
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=45, fontsize=10)

## add a legend
ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('PDF', 'POLI','PUL','UMB') )

plt.show()

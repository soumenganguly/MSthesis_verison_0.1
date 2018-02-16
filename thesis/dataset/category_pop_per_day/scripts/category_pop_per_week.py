import pickle
import sys

a = open(sys.argv[1],'rb') # Aggregated category popularities per day
output = open(sys.argv[2],'wb')

b = a.read()

c = b.split('\n')

c.pop(0)
c.pop(0)
c.pop(0)
c.pop(-1)

k=0
week_cat_pop = {}
for w in range(52):
    cat_pop = {}
    for j in c[k:k+7]:
        v = j.split(' ')
        v.pop(0)
        v.pop(0)
        v.pop(0)
        v.pop(-1)
        for i in range(len(v)):
            if i%2 == 0:
                if v[i] in cat_pop:
                    cat_pop[v[i]] = cat_pop[v[i]] + int(v[i+1])
                else:
                    cat_pop[v[i]] = int(v[i+1])
            else:
                continue
    week_cat_pop[w+1] = cat_pop
    k+=7

pickle.dump(week_cat_pop, output)
a.close()
output.close()

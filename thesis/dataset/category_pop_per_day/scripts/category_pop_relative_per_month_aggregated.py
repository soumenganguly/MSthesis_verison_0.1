from __future__ import division
import pickle
import sys

a = open(sys.argv[1],'rb')
output = open(sys.argv[2],'wb')


relative_category_pop_per_location = {}

p = pickle.load(a)

for i in p:
    cat = {}
    total_list = p[i].values()
    total = int(sum(total_list))
    for j in p[i]:
        cat[j] = (int(p[i][j])/total)*100
    relative_category_pop_per_location[i] = cat

pickle.dump(relative_category_pop_per_location, output)

a.close()
output.close()


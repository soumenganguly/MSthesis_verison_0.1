import pickle
import sys

a = open(sys.argv[1],'rb')
output = open(sys.argv[2],'wb')

p = pickle.load(a)

url_to_views = {}

for agent in p:
    for url in p[agent]:
        if url[0] in url_to_views:
            url_to_views[url[0]] = url_to_views[url[0]] + 1
        else:
            url_to_views[url[0]] = 1

pickle.dump(url_to_views, output)

a.close()
output.close()

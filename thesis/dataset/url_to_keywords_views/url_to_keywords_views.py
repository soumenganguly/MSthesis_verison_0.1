import pickle
import sys

keywords_file = open(sys.argv[1],'rb')
views_file = open(sys.argv[2],'rb')

output_file = open(sys.argv[3],'wb')

keywords = pickle.load(keywords_file)
views = pickle.load(views_file)

keywords_views = {}

for i in keywords:
    a = []
    if i in views:
        a.append(keywords[i][:10])
        a.append(views[i])
    else:
        a.append(keywords[i][:10])
        a.append(0)
    keywords_views[i] = a

pickle.dump(keywords_views, output_file)

keywords_file.close()
views_file.close()
output_file.close()

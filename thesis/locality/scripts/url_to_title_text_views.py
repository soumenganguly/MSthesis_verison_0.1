import pickle
import sys

file_1 = open(sys.argv[1],'rb')
file_2 = open(sys.argv[2],'rb')
output_file = open(sys.argv[3],'wb')

p1 = pickle.load(file_1)    # url to title text file
p2 = pickle.load(file_2)    # url to agent

for url in p1.keys():
    if url in p2.keys():
        views = len(p2[url])
        p1[url].append(views)
    else:
        pass

pickle.dump(p1, output_file)

file_1.close()
file_2.close()
output_file.close()

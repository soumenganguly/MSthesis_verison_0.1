import pickle
import sys


file_1 = open(sys.argv[1],'rb') # 1st pickle file for location 1
file_2 = open(sys.argv[2],'rb') # 2nd pickle file for location 2


output_file = open(sys.argv[3],'wb')

pickle_1 = pickle.load(file_1)
pickle_2 = pickle.load(file_2)

all_words = []

for words in pickle_1:
    all_words.append(words)
for words in pickle_2:
    all_words.append(words)
    
keywords = set(all_words)
no_of_words = len(keywords)

keyword_pop_loc = {}

count = 0

for word in keywords:
    score = []
    if word in pickle_1:
        score.append(pickle_1[word])
    else:
        score.append(0)
    if word in pickle_2:
        score.append(pickle_2[word])
    else:
        score.append(0)

    keyword_pop_loc[word] = score
    count+=1
    print '%d of %d'%(count,no_of_words)
    
pickle.dump(keyword_pop_loc, output_file)

file_1.close()
file_2.close()
output_file.close()

import pickle


pdf_file = open('pdf_2015_keyword_popularity.pkl','rb')
poli_file = open('poli_2015_keyword_popularity.pkl','rb')
pul_file = open('pul_2015_keyword_popularity.pkl','rb')
umb_file = open('umb_2015_keyword_popularity.pkl','rb')

output_file = open('keyword_pop_per_location.pkl','wb')

pdf_pickle = pickle.load(pdf_file)
poli_pickle = pickle.load(poli_file)
pul_pickle = pickle.load(pul_file)
umb_pickle = pickle.load(umb_file)

all_words = []

for words in pdf_pickle:
    all_words.append(words)
for words in poli_pickle:
    all_words.append(words)
for words in pul_pickle:
    all_words.append(words)
for words in umb_pickle:
    all_words.append(words)
    
keywords = set(all_words)
no_of_words = len(keywords)

keyword_pop_loc = {}

count = 0

for word in keywords:
    score = []
    if word in pdf_pickle:
        score.append(pdf_pickle[word])
    else:
        score.append(0)
    if word in poli_pickle:
        score.append(poli_pickle[word])
    else:
        score.append(0)
    if word in pul_pickle:
        score.append(pul_pickle[word])
    else:
        score.append(0)
    if word in umb_pickle:
        score.append(umb_pickle[word])
    else:
        score.append(0)
    keyword_pop_loc[word] = score
    count+=1
    print '%d of %d'%(count,no_of_words)
    
pickle.dump(keyword_pop_loc, output_file)

pdf_file.close()
poli_file.close()
pul_file.close()
umb_file.close()
output_file.close()

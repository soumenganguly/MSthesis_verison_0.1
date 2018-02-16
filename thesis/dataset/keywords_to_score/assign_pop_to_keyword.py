import pickle
import sys

input_file = open(sys.argv[1],'rb')
output_file = open(sys.argv[2],'wb')

url_list = pickle.load(input_file)

keyword_score = {}

for url in url_list:
    for keywords in url_list[url][0]:
        if keywords[0] in keyword_score:
            keyword_score[keywords[0]] = keyword_score[keywords[0]] + keywords[1]*url_list[url][1]
        else:
            keyword_score[keywords[0]] = keywords[1]*url_list[url][1]

pickle.dump(keyword_score, output_file)

input_file.close()
output_file.close()
        

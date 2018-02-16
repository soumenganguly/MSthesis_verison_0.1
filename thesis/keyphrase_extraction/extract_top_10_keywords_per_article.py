import pickle
from nltk.tokenize import word_tokenize, sent_tokenize
from string import punctuation
import sys
import newspaper
import signal
import operator


class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException
    
signal.signal(signal.SIGALRM, timeout_handler)

input_file = open(sys.argv[1], 'rb')

output_file = open(sys.argv[2], 'wb')

input_file_data = pickle.load(input_file)

error_url_files = open('error_url_files.txt','wb')

def tokenize(t):
    sentences = sent_tokenize(t)
    words = []
    refined_words = []
    for sentence in sentences:
        word = word_tokenize(sentence)
        for i in word:
            words.append(i.lower())
        
#Removal of stopwords and punctuations
    stopwords = open('../stop-words-it-en.txt','r').read().split('\r\n')
    for word in words:
        if word not in stopwords and word not in punctuation:
            refined_words.append(word)
    return refined_words
    
def extract_top_10_keywords_in_an_article(title,text,count):
	top_10_dict = {}
    	title_words = tokenize(title)
    	all_words = tokenize(title+' '+text)
    	for word in all_words:
        	if word in title_words:
            		score = 1
        	else:
            		score = 0.5
        	total_score = score*count
        	if word in top_10_dict:
            		top_10_dict[word] = top_10_dict[word] + total_score
        	else:
            		top_10_dict[word] = total_score
	temp = sorted(top_10_dict.items(), key=operator.itemgetter(1), reverse=True)
	return temp


if __name__ == "__main__":
    article_score = {}
    count = 0
    for url in input_file_data:
        list_of_top_10_words = []
	    signal.alarm(10)
	    try:
        	sorted_dict_of_top_10_terms = extract_top_10_keywords_in_an_article(input_file_data[url][0],input_file_data[url][1],input_file_data[url][2])
		    for item in sorted_dict_of_top_10_terms:
			    list_of_top_10_words.append(item)
	    except TimeoutException:
		    error_url_files.write(url+'\n')
	    else:
		    signal.alarm(0)
		article_score[url] = list_of_top_10_words
    	count+=1
   	    print count
    pickle.dump(keyword_score, output_file)
    input_file.close()
    output_file.close()
    error_url_files.close()


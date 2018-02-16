import pickle
from nltk.tokenize import word_tokenize, sent_tokenize
from string import punctuation
import sys
import newspaper

input_file = open(sys.argv[1],'rb')

output_file = open(sys.argv[2],'rb')

input_file_data = pickle.load(input_file)

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
    
def score_keywords_in_a_article(title,text,count):
    title_words = tokenize(title)
    all_words = tokenize(title+' '+text)
    for word in all_words:
        if word in title_words:
            score = 1
        else:
            score = 0.5
        total_score = score*count
        if word in keyword_score:
            keyword_score[word] = keyword_score[word] + total_score
        else:
            keyword_score[word] = total_score
    
if __name__ == '__main__:
    keyword_score = {}
    for url in input_file_data.keys():
        score_keywords_in_an_article(input_file_data[url][0],input_file_data[url][1],input_file_data[url][2])
    pickle.dump(keyword_score, output_file)
    input_file.close()
    output_file.close()
    
    
        

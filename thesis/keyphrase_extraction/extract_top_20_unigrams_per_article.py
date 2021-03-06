from __future__ import division

import re
import time
import hashlib

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder
#from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures
from nltk.corpus.reader import WordListCorpusReader

import sys
import string
import operator
from math import log
import pickle
import random

from newspaper import Article

from collections import Counter
import requests
from lxml import html
#import json
#import MySQLdb

#from sklearn.datasets import load_files
#from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
#from sklearn.naive_bayes import MultinomialNB


#dataset = load_files('/home/soumen/projects/scikit-learn/doc/tutorial/text_analytics/data/languages/paragraphs')  # Read an article

file_id_argv = open(sys.argv[1],'rb')
file_list = pickle.load(file_id_argv)
output_file = open(sys.argv[2],'wb')

italian_stopwords_list = WordListCorpusReader('.', ['stop-words-it-en.txt']).words()
italian_stopwords = set(italian_stopwords_list)

pattern = '^[0-9]+$'  # Remove numbers from keywords

def tokenize(text):
    """Description goes here"""
    tokens = []
    filtered = []
    lower = text.lower()
    #lower_str = lower.decode('utf-8')
    tokens = word_tokenize(lower)
    filtered = [w for w in tokens if w not in italian_stopwords and w not in string.punctuation and not re.match(pattern,w)]
    return filtered


def calculate_tf(word_list):
    """Description goes here"""
    tf_score = {}
    top_n_words = []
    count = Counter(word_list)
    for word in word_list:
        tf_score[word] = count[word]
    sorted_tf = sorted(tf_score.items(), key=operator.itemgetter(1))
    sorted_tf.reverse()
    for word in sorted_tf[0:20]:
        top_n_words.append(word)
        # print word[0], word[1]
    return top_n_words


if __name__ == "__main__":
    time_start = time.time()
    count = 0
    url_to_keywords = {}
    for url in file_list:
        count+=1
        title = file_list[url][0]
        text = file_list[url][1]
        link_text = title + text
        #lang = language_detection([link_text])
        tokens = tokenize(link_text)
        top_n = calculate_tf(tokens)  # Calculate the top unigrams.
        url_to_keywords[url] = top_n
        print "%d of %d"%(count, len(file_list))
    pickle.dump(url_to_keywords, output_file)
    output_file.close()
    file_id_argv.close()
    time_end = time.time() - time_start
    print time_end

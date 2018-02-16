#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""MIT licence add copyright """
import re
import math
import codecs
from collections import Counter
import sys

#with codecs.open("stop-words-it-en.txt", encoding='utf-8') as f:
#    stopwords = set([w.strip() for w in f.readlines()])

stopwords=set()
stopwords_file=open("stop-words-it-en.txt","r")
for line in stopwords_file:
    parola=line.strip("\r\n")
    stopwords.add(unicode(parola, 'utf-8'))

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def split_words(text):
    import nltk
    try:
        return [x.strip('.').lower() for x in nltk.tokenize.wordpunct_tokenize(text)]
    except TypeError:
        return None

def keywords(text):
    """top 10 keywords and their frequency
    """
    NUM_KEYWORDS = 10
    text=unicode(text, "utf-8")
    text = split_words(text)
    # of words before removing blacklist words
    if text:
        num_words = len(text)
        #G: the regex remove all the aphanumerich char plus underscores
        text = [ re.sub(r'[^\w]', '', x) for x in text if x not in stopwords]
        freq = {}
        for word in text:
            if word=='':
                continue
            if word.isdigit():
                continue
            if len(word)==1:
                continue
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

        min_size = min(NUM_KEYWORDS, len(freq))
        keywords = sorted(freq.items(),
                          key=lambda x: (x[1], x[0]),
                          reverse=True)
        keywords = keywords[:min_size]
        keywords = dict((x, y) for x, y in keywords)
        """
        for k in keywords:
            articleScore = keywords[k]*1.0 / max(num_words, 1)
            keywords[k] = articleScore * 1.5 + 1
        """
        return dict(keywords)
    else:
        return dict()


"""
list_text=open(sys.argv[1]+".txt","r").read().splitlines()
tot_keywords=[]
for text in list_text:
	tot_keywords+=list(keywords(text).keys())

print "end",len(tot_keywords)

text_cloud=' '.join(tot_keywords)

files=open(sys.argv[1]+'_keywords.txt','w')
files.write(text_cloud)
files.close()
"""

"""
from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts

tex_cloud='''I am trying to create a word cloud in python. With my current cloud, I can generate a cloud, but the words all are the same size. How can I alter the code so that my words' sizes appear in relation to their frequency?'''

counts = get_tag_counts(text_cloud)
tags = make_tags(counts, maxsize=120)
create_tag_image(tags, 'cloud_large.png', size=(900, 600), fontname='Lobster')
"""




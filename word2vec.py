# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 22:39:15 2018

@author: Dell
"""

import nltk
import urllib
import bs4 as bs
import re
from gensim.models import Word2Vec
from nltk.corpus import stopwords

source=urllib.request.urlopen('https://en.wikipedia.org/wiki/Elon_Musk')

soup=bs.BeautifulSoup(source,'lxml')

text=""
for para in soup.find_all('p'):
    text+=para.text

text=re.sub(r'\[[0-9]*\]',' ',text)
#text=re.sub(r'\s+',' ',text)
text=text.lower()
text=re.sub(r'\W',' ',text)
#text=re.sub(r'[@#\$%&\*\(\)\<\>\?\'\":[,;]]\[-]/',' ',text)
text=re.sub(r'\d',' ',text)
text=re.sub(r'\s+',' ',text)

sentences=nltk.sent_tokenize(text)

sentences=[nltk.word_tokenize(sentence) for sentence in sentences]

for i in range(len(sentences)):
    sentences[i]=[word for word in sentences[i] if word not in stopwords.words('english')]

model=Word2Vec(sentences,min_count=1)
words=model.wv.vocab

vector=model.wv['elon']
similar=model.wv.most_similar('tesla')
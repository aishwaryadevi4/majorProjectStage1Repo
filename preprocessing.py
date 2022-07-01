import json, re, nltk, csv, sys
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from collections import defaultdict
from nltk.stem.snowball import SnowballStemmer
def Preprocessing(words,s):
    words=re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?]))''',' ',words)
    words=re.sub('\n',' ',words)
    words=re.sub('_','-',words)
    words=words.replace('[',' ')
    words=words.replace(']',' ')
    words=words.replace('/',' ')
    words=words.replace('\\',' ')
    words = re.sub(r'(\s)\-+(\s)',r'\1', words)
    words = re.sub(r'\.+(\s)',r'\1', words)
    words = re.sub(r'\.+\.(\w)',r'\1', words)
    words = re.sub(r'(\s)\.+(\s)',r'\1', words)
    words = re.sub("'",'', words)
    words = re.sub(r'\s\d+[\.\-\+]+\d+|\s[\.\-\+]+\d+|\s+\d+\s+|\s\d+[\+\-]+',' ',words)
    words= re.sub("^\d+\s|\s\d+\s|\s\d+$"," ", words)
    words= re.sub(r'\s\#+\s|\s\++\s',' ',words)
    stemmer = SnowballStemmer("english", ignore_stopwords=True)
    stemmed_words = [stemmer.stem(word) for word in words.split()]
    clean_text=filter(lambda w: not w in s,stemmed_words)
    words=''
    for word in clean_text:
        words+=word+' '
    return words

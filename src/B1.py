"""
    B.Query expansion with expresions(bi-words)
"""
"""
    B1.We remove punctuation, make letters lowercase and stem the words so that the they all appear 
    as their roots. We used Porter Stemmer for stemming. We also removed stop words which are words commonly used in English that dont offer us
    information about our documents.

"""

import os
import re

import nltk
from nltk.corpus import stopwords
from nltk.stem import porter
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer

# nltk.download('stopwords')
myPorterStemmer = nltk.stem.porter.PorterStemmer()
stop_words = set(stopwords.words('english'))
train_folders = ['../input_files_and_queries/fbis', '../input_files_and_queries/latimes']
new_folders = '../outputs/final'
appendFile = open(new_folders, 'wt')
i = 0
j = 0
for folder in train_folders:
    files = os.listdir(folder)
    print(j)
    j = j + 1
    for file in files:
        path1 = os.path.join(folder, file)
        file1 = open(path1)
        line = file1.read()  # Use this to read file content as a stream:
        result = re.sub("\<[^<>]*\>", "", line, 0, re.IGNORECASE | re.MULTILINE)
        result2 = re.sub("[^\w\s]", "", result, 0, re.IGNORECASE | re.MULTILINE)
        result3 = result2.lower()
        words = result3.split()
        print(i)
        i = i + 1
        for r in words:
            if not r in stop_words:
                k = myPorterStemmer.stem(r)
                appendFile.write(" " + k)

# ---these have subfiles--
train_folders2 = ['../input_files_and_queries/fr94', '../input_files_and_queries/ft', ]

appendFile2 = open(new_folders, 'wt')

j = 0
for folder in train_folders2:
    subfolders = os.listdir(folder)
    print(j)
    j = j + 1
    for subfolder in subfolders:

        path = os.path.join(folder, subfolder)
        files = os.listdir(path)
        for file in files:
            path1 = os.path.join(folder, subfolder, file)
            print(i)
            i = i + 1
            file1 = open(path1, encoding="ISO-8859-1")
            line = file1.read()  # Use this to read file content as a stream:
            result = re.sub("\<[^<>]*\>", "", line, 0, re.IGNORECASE | re.MULTILINE)
            result2 = re.sub("[^\w\s]", "", result, 0, re.IGNORECASE | re.MULTILINE)
            result3 = result2.lower()
            words = result3.split()
            for r in words:
                if not r in stop_words:
                    k = myPorterStemmer.stem(r)
                    appendFile2.write(" " + r)

appendFile.close()
appendFile2.close()

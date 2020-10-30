"""
    B.Query expansion with expresions(bi-words)
"""

"""
B2.We tokenize the file and create the bigrams and count their frequency using the nltk library.
Note:We create 2 files one with all the bi-words and another one with the 2000 most frequent
"""
import nltk

# nltk.download('punkt')
i=0
print(i)
f = open('../outputs/final')
appendFile = open('../outputs/bi-words_20000',  "a")
raw = f.read()
i=i+1
print(i)
tokens = nltk.word_tokenize(raw)
i=i+1
print(i)
bgs = nltk.bigrams(tokens)
i=i+1
print(i)
#compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(bgs)
appendFile2 = open('../outputs/bi-words_all',  "a")
l = fdist.most_common()
print(l, file=appendFile2)
k = fdist.most_common(20000)
print(k, file=appendFile)
i=i+1
print(i)
appendFile.close()
f.close()
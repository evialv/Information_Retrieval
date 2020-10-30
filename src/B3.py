"""
    B.Query expansion with expresions(bi-words)
"""
"""
B3.We take the elements from the list created above in the bi-words_all file and with the appropriate checks
include in the new queries.
Note:We include words with frequency higher than 4000.
"""
import pickle
import re
f = open('../outputs/store.allbi-words', 'rb')
obj = pickle.load(f)
f.close()

j=0
m=0
filterlist=["<text>","</text>"]
fout=open('../outputs/Ifinal_output_higher_than_3000.EXAMPLE',"a")
with open('../outputs/IndriRunQuery.queries.file.301-450-titles-only.EXAMPLE', "r") as f:

    for line in f:
        m=m+1
        print(m,j)
        i = False

        result = re.sub('<text>', '<text> ', line)
        result2 = re.sub('</text>', ' </text>', result)
        wordlist1 = result2.split()
        word_number=0
        for word in wordlist1:
            words = []
            check_if_bi_word_already_replaced=False
            k=00000
            if i==True:
                while obj[k][1]>2:
                    if word.lower()==obj[k][0][0] or word.lower()==obj[k][0][1]:
                        j=j+1
                        print(j)
                        if wordlist1[word_number-1].lower()==obj[k][0][0] or wordlist1[word_number-1].lower()==obj[k][0][1]:
                            check_if_bi_word_already_replaced=True
                            j=j-1
                            print(j)
                            break
                        words.append(obj[k][0][0])
                        words.append(obj[k][0][1])
                        s = " "
                        s = s.join(words)
                        fout.write(s)
                        fout.write(" ")
                        break
                    k = k + 1
                if(words==[] and check_if_bi_word_already_replaced==False):
                    words.append(word)
                    s = " "
                    s = s.join(words)
                    fout.write(s)
                    fout.write(" ")
                k=k+1
            else:
                words.append(word)
                s = " "
                s = s.join(words)
                fout.write(s)
            if word.lower() in filterlist:
                i=not i
            word_number = word_number + 1

        fout.write("\n")

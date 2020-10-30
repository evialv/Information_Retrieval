"""
Create and run 150 queries with 3 different ways (title,title+desc,title+desc+narr)
and evaluate the retrieval results based on trec eval metrices.
"""
"""
        A.1.2.1 create scripts that isolate titles for all queries

        1)If there there is a <title>  in the begining, start copying the lines until you reach <desc> then stop. We keep the <title> to indicate the different queries
        2)If there is content in the line strip the line and make it lower case
        3)Remove any punctuation except <> (we need them for the title tag) and replace it with space
        4)Append the above sentences in the titles.trec file
        5)Create the appropriate trec formation and remove the <title> tag
        5)You have your title queries ready for trec eval!! :)
        Note 1:step 5 and 6 could be done in the same loop as the previous once but we decided to keep them in 2 different ones.
        Note 2: The procedures on A.1 could be done easily by using ntlk or other libraries however we decided to do them ourselves for our better understanding
"""
import re

filename = '../outputs/topics.301-450.trec'
filterlist = ["<title>"]

with open(filename) as infile, open('../outputs/titles.trec', 'w') as outfile:
    copy = False
    for line in infile:

        if bool(re.search("<title>", line)):
            copy = True
        if bool(re.search("<desc>", line)):
            copy = False
        if copy:
            cleanedLine = line.strip().lower() # remove new lines

            if cleanedLine:  # line is not empty
                cleanedLine = re.sub('[^\w\s<>]', ' ', cleanedLine)
                outfile.write(cleanedLine)
                outfile.write(" ")

fin = "../outputs/titles.trec"
fout = open("../outputs/IndriRunQuery.queries.file.301-450-titles-only.EXAMPLE", "wt")
filterlist=["<title>"]
#------printing the 1rst line which is default for the trec file we want to create----------------#
fout.write('<parameters> \n')
fout.write('<index>../Lemur_indices/trec7-8</index>\n') #  where ../Lemur_indices/trec7-8 the trec location in our computer
fout.write('<rule>method:dirichlet,mu:1000</rule> \n')
fout.write('<count>1000</count> \n')
fout.write('<trecFormat>true</trecFormat> \n')
fout.write('<query> <type>indri</type> <number>301</number> <text>')
i=300
with open(fin, "r") as f:
    for line in f:
        wordlist1 = line.split()
        for word in wordlist1:
            words = []
            if word.lower() not in filterlist:
                words.append(word.lower())
                s = " "
                s = s.join(words)
                fout.write(s)
                fout.write(" ")
            else:
                fout.write('</text> </query> \n')
                i += 1
                fout.write('<query> <type>indri</type> <number>{}</number> <text>'.format(i))
    fout.write('</text> </query> \n')
    fout.write('</parameters> \n')
    print(type(fout))

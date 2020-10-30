"""
Create and run 150 queries with 3 different ways (title,title+desc,title+desc+narr)
and evaluate the retrieval results based on trec eval metrices.
"""
"""
        A.1.2.2 create scripts that isolate title+desc for all queries
        Process the same as the above with a change in key words
"""

filename = '../outputs/topics.301-450.trec'
import re
with open(filename) as infile, open('../outputs/titles_desc.trec', 'w') as outfile:
    copy = False
    for line in infile:

        if bool(re.search("<narr>", line)):
            copy = False
        if bool(re.search("<title>", line)):
            copy = True
        if copy:
            cleanedLine = line.strip().lower()  # remove new lines

            if cleanedLine:  # line is not empty
                cleanedLine = re.sub('[^\w\s<>]', ' ', cleanedLine)
                outfile.write(cleanedLine)
                outfile.write(" ")

fin = "../outputs/titles_desc.trec"
fout = open("../outputs/IndriRunQuery.queries.file.301-450-titles-desc-only.EXAMPLE", "wt")
filterlist = ["<title>", "<desc>"]

# ------printing the 1rst line which is default for the trec file we want to create----------------#
fout.write('<parameters> \n')
fout.write(
    '<index>../Lemur_indices/trec7-8</index>\n')  # where ../Lemur_indices/trec7-8 the trec location in our computer
fout.write('<rule>method:dirichlet,mu:1000</rule> \n')
fout.write('<count>1000</count> \n')
fout.write('<trecFormat>true</trecFormat> \n')

i = 300
with open(fin, "r") as f:
    for line in f:
        wordlist1 = line.split()
        for word in wordlist1:
            words = []
            if word not in filterlist:
                words.append(word)
                s = " "
                s = s.join(words)
                fout.write(s)
                fout.write(" ")
            elif word == "<desc>":
                continue
            else:
                fout.write('<query> <type>indri</type> <number>301</number> <text>')
                fout.write('</text> </query> \n')
                i += 1
                fout.write('<query> <type>indri</type> <number>{}</number> <text>'.format(i))
    fout.write('</text> </query> \n')
    fout.write('</parameters> \n')
    print(type(fout))

"""
NOTE: the code below was used for creating the queries for efficient search amongst the documents given to us by our instructors.
The goal of the project was to create queries that produce good metrices in trec eval as explained in the report.
This is just the basic code to create these queries
For more information about how the queries we created retrive the documents that we want please check the report

"""


"""

A1.1 we need to create one file from all the initial queries (in text form)
filenames ->all the initial queries in seperate files

"""
filenames = ['../input_files_and_queries/topics.301-350.trec6','../input_files_and_queries/topics.351-400.trec7','../input_files_and_queries/topics.401-450.trec8']

# Open topics.301-450.trec in write mode
# topics.301-450.trec->our file with all the queries
with open('topics.301-450.trec', 'w') as outfile:
    # Iterate through list
    for names in filenames:
        # Open each file in read mode
        with open(names) as infile:
            # read the data from files 1,2,3 and write the data in topics.301-450.trec
            outfile.write(infile.read())
        # Add '\n' to enter data from different files from to seperate them
        outfile.write("\n")

"""

A.1.2 create scripts that isolate title, title+desc & title+desc+narr

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

filename = 'topics.301-450.trec'
filterlist = ["<title>"]

with open(filename) as infile, open('titles.trec', 'w') as outfile:
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

fin = "titles.trec"
fout = open("IndriRunQuery.queries.file.301-450-titles-only.EXAMPLE", "wt")
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

"""
        A.1.2.2 create scripts that isolate title+desc for all queries
        Process the same as the above with a change in key words
"""

filename = 'topics.301-450.trec'

with open(filename) as infile, open('titles_desc.trec', 'w') as outfile:
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

fin = "titles_desc.trec"
fout = open("IndriRunQuery.queries.file.301-450-titles-desc-only.EXAMPLE", "wt")
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
"""
        A.1.2.3 create scripts that isolate title+desc+narr for all queries
        Process the same as the above with a change in key words
"""


filename = 'topics.301-450.trec'

with open(filename) as infile, open('titles_desc_narr.trec', 'w') as outfile:
    copy = False
    for line in infile:

        if bool(re.search("</top>", line)):
            copy = False
        if bool(re.search("<title>", line)):
            copy = True
        if copy:
            cleanedLine = line.strip().lower()  # remove new lines

            if cleanedLine:  # line is not empty
                cleanedLine = re.sub('[^\w\s<>]', ' ', cleanedLine)
                outfile.write(cleanedLine)
                outfile.write(" ")

fin = "titles_desc_narr.trec"
fout = open("IndriRunQuery.queries.file.301-450-titles-desc-narr-only.EXAMPLE", "wt")
filterlist = ["<title>", "<desc>","<narr>"]

# ------printing the 1rst line which is default for the trec file we want to create----------------#
fout.write('<parameters> \n')
fout.write(
    '<index>../Lemur_indices/trec7-8</index>\n')  # where ../Lemur_indices/trec7-8 the trec location in our computer
fout.write('<rule>method:dirichlet,mu:1000</rule> \n')
fout.write('<count>1000</count> \n')
fout.write('<trecFormat>true</trecFormat> \n')
fout.write('<query> <type>indri</type> <number>301</number> <text>')
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
            elif word != "<title>":
                continue
            else:

                fout.write('</text> </query> \n')
                i += 1
                fout.write('<query> <type>indri</type> <number>{}</number> <text>'.format(i))
    fout.write('</text> </query> \n')
    fout.write('</parameters> \n')
    print(type(fout))
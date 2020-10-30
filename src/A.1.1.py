"""
Create and run 150 queries with 3 different ways (title,title+desc,title+desc+narr)
and evaluate the retrieval results based on trec eval metrices.
"""
"""
A1.1 we need to create one file from all the initial queries (in text form)
filenames ->all the initial queries in seperate files

"""
filenames = ['../input_files_and_queries/topics.301-350.trec6','../input_files_and_queries/topics.351-400.trec7','../input_files_and_queries/topics.401-450.trec8']

# Open topics.301-450.trec in write mode
# topics.301-450.trec->our file with all the queries
with open('../outputs/topics.301-450.trec', 'w') as outfile:
    # Iterate through list
    for names in filenames:
        # Open each file in read mode
        with open(names) as infile:
            # read the data from files 1,2,3 and write the data in topics.301-450.trec
            outfile.write(infile.read())
        # Add '\n' to enter data from different files from to seperate them
        outfile.write("\n")


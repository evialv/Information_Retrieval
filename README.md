# Information_Retrival
The goal of the project was to create queries that produce good metrices in Trec Eval, a performance evaluation tool for Information Retrival. <br/>
For more information about how the queries we created retrive the documents that we want, please check the report included in the project. <br/>
#### Report included in the repository :) ####

### Part A: ###
* Create and run 150 queries with 3 different ways (title,title+desc,title+desc+narr) and evaluate the retrieval results based on trec eval metrices.</br>
  Process:
    * A1.1 We need to create one file from all the initial queries (in text form) 
    * A.1.2 Create scripts that isolate title, title+desc & title+desc+narr
      * A.1.2.1 Create scripts that isolate titles for all queries 
        <details>
          <summary> Steps Followed: </summary>
          <summary> 1. If there there is a <title>  in the begining, start copying the lines until you reach <desc> then stop. We keep the <title> to indicate the different queries. </summary>
          <summary> 2. If there is content in the line strip the line and make it lower case. </summary>
          <summary> 3. Remove any punctuation except <> (we need them for the title tag) and replace it with space. </summary>
          <summary> 4. Append the above sentences in the titles.trec file. </summary>
          <summary> 5. Create the appropriate trec formation and remove the <title> tag.</summary>
          <summary> 6. You have your title queries ready for trec eval!! </summary>
       * A.1.2.1 Create scripts that isolate titles for all queries.</br>
       Process the same as above with small changes in the "key words". </br>
       * A.1.2.3 Create scripts for the title+desc+narr.</br>
        Process the same as above with small changes in the "key words"</br>
### Part B: ###
* Expand the queries with expressions, find a number of "statistically good" expressions (ex.bi-words) while processing the collection of documents and 
run the new queries and evaluate them with the trec eval metrices.</br>
  Process:
    * B1. We process the collection so that we retrieve only words that have add value to the query search.
        <details>
        <summary> Steps Followed: </summary>
        <summary> 1.Remove punctuation. </summary>
        <summary> 2.Make letters lowercase. </summary>
        <summary> 3.Stem the words so that the they all appear as their roots. We used Porter Stemmer for stemming. </summary>
        <summary> 4.We also removed stop words which are words commonly used in English that don't offer us useful information about our documents.</summary>
    * B2. We tokenize the file and create the bigrams and count their frequency using the nltk library </br>
    * B3. We take the elements from the list created above in the bi-words_all file and with the appropriate checks
include in the new queries (We take into consideration bi-words with frequency larger than 4000).

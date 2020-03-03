# Assignment 1 - Python for Text Processing

*Submission deadline: Friday 13 March 2020, 11:55pm.*

*Assessment weight: 5% of the total unit assessment.*

## Objectives of this assignment

In this assignment you will practice with the use of Python for text processing. In particular, you will implement a text summarisation system that uses PageRank to select the most important sentences in a document. The assignment will be split into 5 tasks that will allow you to gradually implement the summarisation system.

**The deadline of this assignment is before census date, so that it can serve as a diagnostic test and you can determine whether you want to remain in the unit or to withdaw without academic penalty.**

You are provided with a template that contains the definitions of the functions that you need to implement in each of the tasks below. The template includes simple [Python doctests](https://docs.python.org/3/library/doctest.html) that you can use to check the correctness of the code. These tests are there to help you, but note that we will use the [unittest framework](https://docs.python.org/3/library/unittest.html) with a separate set of tests when we assess your submission. It is your responsibility to run your own tests, in addition to the doctests provided.

## The Tasks (1 mark each)

### 1. Find the Top Stems

Implement a function `get_top_stems` that returns a list with the *n* most frequent stems, sorted by frequency in descending order. The input arguments of the function are:

* *document*: A string that represents the document.
* *n*: The number of stems to return.
* *stopwords*: A list of stop words.

You must use NLTK to find the tokens and the stems. If you use different libraries your solution probably won't pass the tests. Your function must find the tokens *(remember to use NLTK's sentence tokeniser before NLTK's word tokeniser!)*, then ignore those tokens that are in the list of stop words (do the comparison with the list ignoring differences between uppercase and lowercase), stem them, and then return the *n* most frequent stems.

*Remember to use the list of stop words provided in the function argument. Do not make your own list of stopwords. No not use NLTK's list of stopwords or any list other than the one provided in the function argument.*

### 2. Convert a sentence into a set of stems

Implement a function `sentence_to_set` that returns the set of all stems of a sentence. The input arguments of the function are:

* *sentence*: A string that contains the sentence.
* *list_of_stems*: A list of stems that will be used by your function.

You must use NLTK to find the tokens and the stems of the sentence. Once you have found the stems, keep only those that occur in *list_of_stems* and return them as a Python set.

For example, if the sentence is `"This is sentence 1"` and the list of stems provided is `['thi', 'sentenc', 'one']`, then the result must be the set `{'thi', 'sentenc'}`. Note that the comparison with the list of stems is not case sensitive.

### Jaccard Similarity

The template includes an implementation of the Jaccard similarity `compute_jaccard`. **Do not modify this function or your solution may not pass the tests.** The implementation uses your solution to task 2, and you can use it to complete the remaining tasks. You can find out more about the Jaccard similarity in this Wikipedia page:

* https://en.wikipedia.org/wiki/Jaccard_index

### 3. Compute the transition matrix

Implement a function `get_transition_matrix` that computes the transition matrix of a list of sentences. The transition matrix is the same as described in the unit lectures. The difference in the lectures is that the transition matrix represents a graph of webpages that are connected through their web links. But your implementation will represent a graph of sentences that are connected when their Jaccard similarity is equal or greater than a threshold. The input arguments of the function are:

* "list_sentences": A Python list of strings where each string represents one sentence.
* "list_of_stems": A list of stems that is used to define what stems will be used by the Jaccard similarity.
* "threshold": A threshold that will determine whether two sentences are related. If the Jaccard similarity between two sentences is equal or larger than the threshold, then the transition matrix will show a link between them.

When you compute the transition matrix it may happen that a sentence is not similar with any other sentence. It could even happen that the sentence shows a Jaccard similarity of zero with itself! This may happen if none of the stems of the sentence appears in the list of stems. This is a case of a "dangling" page in the original PageRank algorithm. When that happens, all of the elements in the column of the transition matrix that represents the sentence must the same value: 1/number_of_sentences. This means that a random surfer that visits a dangling page will randomly visit any page in the next step.

### 4. Compute PageRank

Implement the PageRank algorithm `compute_pagerank`. This task should be very easy to complete since we are covering the algorithm and a Python implementation in the lectures and workshops. The input arguments are:

* *list_sentences*: The list of sentences.
* *list_of_stems*: The list of important stems that is used to compute the Jaccard similarity.
* *threshold*: The threshold that is used to compute the transition matrix.
* *damping_factor*: The damping factor.
* *epsylon*: The value of epsylon used to determine when to stop the PageRank algorithm. See the lecture notes and related workshop for details.

### 5. Compute the summarisation system

Finally, you can now implement the summariser! Implement a function `summarise` that returns the *n* sentences with highest PageRank value. Make sure that the list of sentences is returned in the same order as they appear in the original list. The input arguments are:

* *text*: The text of the document. This is a string that has multiple sentences. You need to split the text into sentences using NLTK, and pass the list to the other functions that you have implemented in the previous tasks in order to determine the PageRank.
* *list_of_stems*: The list of important stems used for the Jaccard similarity.
* *N*: The number of sentences to return in the summary. If *N* is larger than the total number of sentences, then the system returns the original list (and it would be a useless summary).
* *threshold*: The threshold used to determine the transition matrix.
* *damping_factor*: The damping factor used to compute the PageRank.
* *epsylon*: The value of epsylon to determine when to stop the PageRank algorithm.

## Submission

The submission must be a single Python file. Do not submit several files or a zip file since the automarker would not know what to do with your submission.

Note that the deadline is a hard deadline and there will be a penalty for late submission as specified in the unit guide (0.5 marks per day late or part thereof). In addition, since the submission date is less than a week before the census date of 19 of March 2020, late submissions might not be assessed before census date.

Finally, note that **the work submitted should be your own work**. You may be tempted to search the Web for Python implementations of the questions asked in this tutorial. Be aware that:

1. If we find out that your work is copied from the Web or from other submissions, you may face disciplinary action.
2. Often, trying to adapt work from the web may be more difficult than when you try from scratch.
3. The work you find on the web may be wrong or not do exactly what is asked in this assignment anyway.

## Credits

The idea of using PageRank to extract a text summary is not new, and it has a name: **TextRank**. We are using the Jaccard similarity index in this assignment because it is easy to implement. But there are better similarity metrics for this task, and some of these better metrics are used in the links listed below. Some of the links below include Python code but you will probably find it too hard to adapt it to the assignment. You are advised to implement your solution from scratch.

* The original paper that introduces TextRank by  
Rada Mihalcea and Paul Tarau (2004). *"TextRank: Bringing Order into Texts"*. Proceedings of EMNLP. https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf
* A tutorial with Python code: https://www.analyticsvidhya.com/blog/2018/11/introduction-text-summarization-textrank-python/
* Another tutorial with Python code: https://nlpforhackers.io/textrank-text-summarization/
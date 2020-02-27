"""Python interface to the OHSUMED data
Author: Diego Molla
Date: 20 March 2014"""

corpusfile = 'ohsumed.87'
questionsfile = 'query.ohsu.1-63'
answersfile = 'qrels.ohsu.batch.87'

def yieldrecords(f):
    "Yield the key and text of the documents"
    key = ''
    text = ''
    inKey = False
    inText = False
    for l in f.readlines():
        if inKey:
            inKey = False
            key = l.strip()
            continue
        if inText:
            inText = False
            text = l.strip()
            continue
        if l[:2] == '.U':
            inKey = True
            continue
        if l[:2] == '.W':
            inText = True
            continue
        if key != '' and l[:2] == '.I':
            yield (key,text)
            key = ''
            text = ''
            continue
    yield (key,text)

def yieldquestions(f):
    "Yield the key and text of the questions"
    key = ''
    text = ''
    inDesc = False
    for l in f.readlines():
        l = l.strip()
        if l[:5] == "<num>":
            key = l[14:]
            text = ''
            continue
        if l[:7] == "<title>":
            text = l[8:]
            continue
        if l[:6] == "<desc>":
            inDesc = True
            continue
        if l[:6] == "</top>":
            inDesc = False
            yield (key,text)
            continue
        if inDesc:
            text += " "+l
            continue

def yieldanswers(f):
    "Yield the key of the question and the ID of the relevant documents"
    key = ''
    IDs = set()
    for l in f.readlines():
        l = l.strip()
        (newkey,ID,relevance) = l.split()
        if key == '':
            key = newkey
        if key != newkey:
            yield (key,IDs)
            key = newkey
            IDs = set()
            continue
        IDs.add(ID)
    yield (key,IDs)

print("Reading OHSUMED data")
with open(corpusfile) as f:
    index = dict()
    for (key,text) in yieldrecords(f):
        # print(l.strip().split())
        index[key] = text

with open(questionsfile) as f:
    questions = dict()
    for (key,text) in yieldquestions(f):
        questions[key] = text

with open(answersfile) as f:
    answers = dict()
    for (key,text) in yieldanswers(f):
        answers[key] = text

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 22:59:25 2023

@author: user
"""
import spacy

text = """There are broadly two types of extractive summarization tasks depending on what the summarization program focuses on. The first is generic summarization, which focuses on obtaining a generic summary or abstract of the collection (whether documents, or sets of images, or videos, news stories etc.). The second is query relevant summarization, sometimes called query-based summarization, which summarizes objects specific to a query. Summarization systems are able to create both query relevant text summaries and generic machine-generated summaries depending on what the user needs.
An example of a summarization problem is document summarization, which attempts to automatically produce an abstract from a given document. Sometimes one might be interested in generating a summary from a single source document, while others can use multiple source documents (for example, a cluster of articles on the same topic). This problem is called multi-document summarization. A related application is summarizing news articles. Imagine a system, which automatically pulls together news articles on a given topic (from the web), and concisely represents the latest news as a summary.
Image collection summarization is another application example of automatic summarization. It consists in selecting a representative set of images from a larger set of images.[4] A summary in this context is useful to show the most representative images of results in an image collection exploration system. Video summarization is a related domain, where the system automatically creates a trailer of a long video. This also has applications in consumer or personal videos, where one might want to skip the boring or repetitive actions. Similarly, in surveillance videos, one would want to extract important and suspicious activity, while ignoring all the boring and redundant frames captured """

text

from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

stopwords = list(STOP_WORDS)
stopwords

len(stopwords)

nlp = spacy.load('en_core_web_sm')

text

doc = nlp(text)
doc

tokens = [token.text for token in doc]
print(tokens)

tokens

len(tokens)

punctuation

doc

word_frequencies = {}
for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1
                
word_frequencies                

len(word_frequencies)                

max_frequency = max(word_frequencies.values())
max_frequency

for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency

word_frequencies

sentence_tokens = [sent for sent in doc.sents]
sentence_tokens

len(sentence_tokens)

sentence_scores = {}
for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.text.lower()]
       
sentence_scores        

from heapq import nlargest

select_length = int(len(sentence_tokens)*0.3)
select_length

summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
summary

sentence_scores

final_summary = [word.text for word in summary]
final_summary

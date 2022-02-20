# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 21:57:48 2022

Jeison Robles Arias

This code is writen with educational purposes and for this case I'll use
Natural Language Processing Library NLTK

"""




from nltk.tokenize import sent_tokenize, word_tokenize
from pathlib import Path
import nltk
from nltk.corpus import PlaintextCorpusReader

corpus_root = r"C:\Users\tan\Documents\GitHub\Machine-Learning\NLTK FOR NATURAL LANGUAGE PROCESSING"

f = open(r"C:\Users\tan\Documents\GitHub\Machine-Learning\NLTK FOR NATURAL LANGUAGE PROCESSING\CostaRica.txt")

filelists = PlaintextCorpusReader(corpus_root, '.*')

print(filelists.fileids())

wordslist = filelists.words("CostaRica.txt")

# Content = Path(r"C:\Users\tan\Documents\GitHub\Machine-Learning\NLTK FOR NATURAL LANGUAGE PROCESSING\CostaRica.txt").read_text().replace('\n', ' ')



# import nltk
# nltk.download('stopwords')

# import nltk
# nltk.download('punkt')

from nltk.corpus import stopwords


example_string = """
Muad'Dib learned rapidly because his first training was in how to learn.
And the first lesson of all was the basic trust that he could learn.
It's shocking to find how many people do not believe they can learn,
and how many more believe learning to be difficult."""

# st = sent_tokenize(example_string)
# wt = word_tokenize(example_string)
# wt = word_tokenize(wordslist)

from nltk import FreqDist

# path = nltk.data.find(r"C:\Users\tan\Documents\GitHub\Machine-Learning\NLTK FOR NATURAL LANGUAGE PROCESSING\CostaRica.txt")



# FD = FreqDist(example_string)
FD = FreqDist(wordslist)
FD.plot(30,cumulative=False)
# FD.plot(10,cumulative=True)


# print(wt)

import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import gutenberg

corpus = PlaintextCorpusReader('../../data/english', '.*')
fd1 = nltk.FreqDist(corpus.words())
fd2 = nltk.FreqDist(gutenberg.words())
tf_idf = []
weight = 1
word_dict = [word[:-1] for word in open('../../data/dict.txt').readlines()]
word_dict = dict(zip(word_dict, word_dict))

for word, times in fd1.most_common():
    if word not in word_dict: continue
    if word in fd2:
        times *= 1.0 / fd2[word]
    else:
        times *= weight
    tf_idf.append((times, word))

tf_idf.sort(reverse=True)
threshold = 1
outf = open('../../data/sort1_dict.txt', 'w')
for relate_freq, word in tf_idf:
    if relate_freq >= threshold:
        print relate_freq, word
        outf.write('%s\n' % word)

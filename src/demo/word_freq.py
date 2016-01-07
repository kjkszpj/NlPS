import nltk
from nltk.corpus import PlaintextCorpusReader

corpus = PlaintextCorpusReader('../../data/english', '.*')
print "begin1"
total_word = corpus.words()
word_dict = [line[:-1] for line in open('../../data/stem_dict.txt').readlines()]
word_dict1 = word_dict[:100]
word_dict3 = word_dict[:300]
word_dict10 = word_dict[:1000]
word_dict1 = dict(zip(word_dict1, word_dict1))
word_dict3 = dict(zip(word_dict3, word_dict3))
word_dict10 = dict(zip(word_dict10, word_dict10))

print 'begin2'
total_word1 = [word for word in total_word if word in word_dict1]
total_word3 = [word for word in total_word if word in word_dict3]
total_word10 = [word for word in total_word if word in word_dict10]
print 'begin3'
nltk.FreqDist(total_word1).plot()
nltk.FreqDist(total_word3).plot()
nltk.FreqDist(total_word10).plot()
# nltk.FreqDist(total_word).plot()
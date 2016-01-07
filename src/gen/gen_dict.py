import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords

input_dir = '../../data/english'
corpus = PlaintextCorpusReader(input_dir, '.*')

porter = nltk.PorterStemmer()
std_stop = stopwords.words('english')
my_stop = open('../../data/stop.txt', 'r').readlines()
my_stop = [line[:-1] for line in my_stop]
total_words = []
for word in corpus.words():
    if word not in std_stop and word not in my_stop:
        total_words.append(porter.stem(word))

outf = open('../../data/dict.txt', 'w')
fd = nltk.FreqDist(total_words)
for a in fd.most_common():
    if a[1] > 2:
        outf.write('%s\n' % a[0])
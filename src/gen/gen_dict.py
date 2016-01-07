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
temp = corpus.words()
for word in temp:
    if (word not in std_stop) and (word not in my_stop):
        total_words.append(word)

outf = open('../../data/dict.txt', 'w')
fd = nltk.FreqDist(total_words)
print fd
for a in fd.most_common():
    if a[1] > 2:
        outf.write('%s\n' % a[0])

stemf = open('../../data/stem_dict.txt', 'w')
fd = nltk.FreqDist([porter.stem(word) for word in total_words])
print fd
for a in fd.most_common():
    stemf.write('%s\n' % a[0])
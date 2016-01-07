import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords

input_dir = '../../data/english'
corpus = PlaintextCorpusReader(input_dir, '.*')

porter = nltk.PorterStemmer()
std_stop = stopwords.words('english')
my_stop = [word[:-1] for word in open('../../data/stop.txt', 'r').readlines()]
yes_word = [word[:-1] for word in open('../../data/yes_word.txt', 'r').readlines()]
total_words = []
temp = corpus.words()
for word in temp:
    if ((word not in std_stop) and (word not in my_stop) and (len(word) > 2)) or (word in yes_word):
        total_words.append(word)

threshold = range(8, 4000)
fd = nltk.FreqDist(total_words)
for a in fd.most_common():
    if a[1] in threshold:
        print a

outf = open('../../data/dict.txt', 'w')
fd = nltk.FreqDist(total_words)
print fd
for a in fd.most_common():
    if a[1] in threshold:
        outf.write('%s\n' % a[0])

stemf = open('../../data/stem_dict.txt', 'w')
fd = nltk.FreqDist([porter.stem(word) for word in total_words])
print fd
for a in fd.most_common():
    stemf.write('%s\n' % a[0])
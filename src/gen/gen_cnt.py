# todo, better stem dict
import nltk
from nltk.corpus import PlaintextCorpusReader

input_dir = '../../data/english'
corpus = PlaintextCorpusReader(input_dir, '.*')
list = corpus.fileids()

porter = nltk.PorterStemmer()

dict = [line[:-1] for line in open('../../data/dict.txt').readlines()]
m = len(dict)

outf = open('../../data/first.ldac', 'w')
stem_dict = [line[:-1] for line in open('../../data/stem_dict.txt').readlines()]

for paper in list:
    word = [porter.stem(s) for s in corpus.words(paper) if s in dict]
    word = [s for s in word if s in stem_dict]
    # print len(corpus.words(paper)), len(word)
    mfd = {}
    for s in word: mfd[s] = mfd.get(s, 0) + 1

    outf.write('%d' % len(mfd))
    for i in range(len(stem_dict)):
        if mfd.has_key(stem_dict[i]):
            outf.write(' %d:%d' %(i, mfd[stem_dict[i]]))
    outf.write('\n')
    print paper, len(mfd)
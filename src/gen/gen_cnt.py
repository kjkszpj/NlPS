import nltk
from nltk.corpus import PlaintextCorpusReader

input_dir = '../../data/english'
corpus = PlaintextCorpusReader(input_dir, '.*')
list = corpus.fileids()

porter = nltk.PorterStemmer()

dict = [line[:-1] for line in open('../../data/dict.txt').readlines()]
m = len(dict)

outf = open('../../data/first.ldac', 'w')

for paper in list[:20]:
    word = [porter.stem(s) for s in corpus.words(paper)]
    word = [s for s in word if s in dict]
    # print len(corpus.words(paper)), len(word)
    mfd = {}
    for s in word: mfd[s] = mfd.get(s, 0) + 1

    outf.write('%d' % len(mfd))
    for i in range(len(dict)):
        if mfd.has_key(dict[i]):
            outf.write(' %d:%d' %(i, mfd[dict[i]]))
    outf.write('\n')
    print paper
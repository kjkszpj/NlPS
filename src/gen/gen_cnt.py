# todo, better stem dict
import nltk
from nltk.corpus import PlaintextCorpusReader

input_dir = '../../data/english'
corpus = PlaintextCorpusReader(input_dir, '.*')
text_list = corpus.fileids()

porter = nltk.PorterStemmer()

word_dict = [line[:-1] for line in open('../../data/dict.txt').readlines()]
word_dict = dict(zip(word_dict, range(0, len(word_dict))))
m = len(word_dict)

stem_dict = [line[:-1] for line in open('../../data/stem_dict.txt').readlines()]
stem_dict = dict(zip(stem_dict, range(0, len(stem_dict))))

outf = open('../../data/first.ldac', 'w')

for paper in text_list[:-10]:
    word = [porter.stem(s) for s in corpus.words(paper) if s in word_dict]
    word = [s for s in word if s in stem_dict]
    # print len(corpus.words(paper)), len(word)
    mfd = {}
    for s in word: mfd[s] = mfd.get(s, 0) + 1

    outf.write('%d' % len(mfd))
    for stem in stem_dict.keys():
        if stem in mfd:
            outf.write(' %d:%d' % (stem_dict[stem], mfd[stem]))
    outf.write('\n')
    print paper, len(mfd)

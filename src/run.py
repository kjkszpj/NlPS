import numpy
import lda

X = lda.utils.ldac2dtm(open('../data/first.ldac'), offset=0)
vocab = [line[:-1] for line in open('../data/dict.txt').readlines()]
# titles = lda.datasets.load_reuters_titles()

model = lda.LDA(n_topics=7, n_iter=2000, random_state=1)
model.fit(X)
topic_word = model.topic_word_
n_top_words = 20
for i, topic_dist in enumerate(topic_word):
    topic_words = numpy.array(vocab)[numpy.argsort(topic_dist)][:-(n_top_words+1):-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))
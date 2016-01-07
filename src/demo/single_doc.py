import lda
import pickle
import numpy
import matplotlib.pyplot as plt

print 'load'
model = pickle.load(open('../../data/model_lda.pk'))
train = lda.utils.ldac2dtm(open('../../data/first.ldac'), offset=0)
test = lda.utils.ldac2dtm(open('../../data/test.ldac'), offset=0)
print 'transform'

print 'train'
temp = model.transform(train)
cnt = [0] * 7
for i in range(len(temp)):
    max_result = 0
    max_id = 0
    for j in range(len(temp[i])):
        if max_result < temp[i][j]:
            max_result = temp[i][j]
            max_id = j
    cnt[max_id] += 1
print cnt
index = numpy.arange(len(cnt))
bar_width = 0.83
plt.bar(index, cnt, bar_width)
plt.title('Topic Distribution over NIPS2015')
plt.xticks(index + bar_width / 2, ['optimization', 'graph', 'bandit', 'probability', 'deep learning', 'matrix', 'ml'])
plt.show()

print 'test'
temp = model.transform(test)
for i in range(len(temp)):
    output = ''
    for j in range(len(temp[i])):
        if temp[i][j] < 0.2: temp[i][j] = 0
        output += '%.2f\t' %(temp[i][j])
    print(output)
















# Topic 0: optim
# Topic 1: graph
# Topic 2: bandit
# Topic 3: distribut
# Topic 4: (d)nn
# Topic 5: matrix
# Topic 6: ml

import os
import pickle

input_dir = '../../data/english'
dict_dir = '../../data/dict.pk'
all_file = os.popen('find %s -name "*.txt"' % input_dir)
total = []
for file_name in all_file.readlines():
    content = open(file_name[:-1], 'r').readline()
    content = content.split(' ')
    total = total + content
pickle.dump(set(total), open(dict_dir, 'wb'))
print set(total)
print len(set(total))

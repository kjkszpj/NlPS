import os
import re

text_dir = '../../data/text'
english_dir = '../../data/english'

#   todo, lowercase

all_text_file = os.popen('find %s -name "*.txt"'  % text_dir)
cnt = 1
for text_file in all_text_file.readlines():
    text_f = open(text_file[:-1], 'r')
    english = ''
    for line in text_f.readlines():
        line = line.lower()
        line = re.sub('[^a-z]+', ' ', line)
        english = english + ' ' + line
    english = re.sub('\s+', ' ', english)
    outf = open('%s/%d.txt' % (english_dir, cnt), 'w')
    cnt += 1
    outf.write(english)
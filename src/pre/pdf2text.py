import os

raw_data_dir = '../../data/raw'
output_dir = '../../data/text'
all_pdf_name = os.popen('find %s -name "*.pdf"' % raw_data_dir)
dir_content = all_pdf_name.readlines()
cnt = 1
for pdf_name in dir_content:
    if pdf_name[-1] == '\n': pdf_name = pdf_name[:-1]
    file_content = os.popen('./tools/pdf2txt.py %s' % pdf_name).readlines()
    text = ''
    for s in file_content:
        while s[0] == '<':
            s = s[s.find('>'):]
        if s != '\n' and s != '':
            text = text + ' ' + s
    text = text.replace('\t', ' ')
    while text.find('  ') != -1:
        text = text.replace('  ', ' ')
    # if (cnt % 10 < 2):
    #     print(file_content)
    #     print('----------')
    #     print(text)
    outf = open(output_dir + '/%d.txt' % cnt, 'w')
    outf.write(text)
    print cnt
    cnt += 1
    # input('______')
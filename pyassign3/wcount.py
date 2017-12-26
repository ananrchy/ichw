#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Yu Yuanhe"
__pkuid__  = "1700012623"
__email__  = "yuyuanhe@pku.edu.cn"
"""

import sys,string
from urllib.request import urlopen

def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    for i in string.punctuation:
        lines = lines.replace(i,'') 
    dic = {}
    for i in lines.lower().split():
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    sequence = sorted(dic.items(),key = lambda x: x[1],reverse = True)
    for i in range(topn):
        print(sequence[i][0],' '*(10-len(sequence[i][0])),sequence[i][1])
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)

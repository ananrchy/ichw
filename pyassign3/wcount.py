# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 15:42:10 2017

@author: anarchy
"""

#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Yu Yuanhe"
__pkuid__  = "1700012623"
__email__  = yuyuanhe@pku.edu.cn"
"""

import sys
from urllib.request import urlopen
import collections
import re

def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    a = lines.lower()
    a = re.sub("\"|,|\.", " ", a)
    a = a.split()
    out=collections.Counter(a).most_common(10)
    for i in range(len(out)):
        print(out[i][0],' '*(10-len(out[i][0])),out[i][1]) 
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
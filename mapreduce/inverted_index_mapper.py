#!/usr/bin/env python
import sys, os, re
from collections import defaultdict

# try:
#     file = os.environ['mapreduce_map_input_file']
# except KeyError:
#     file = os.environ['map_input_file']

file = 'data/test.txt'
freq_dict = defaultdict(lambda: 0)

for line in sys.stdin:
    line = line.strip()
    words = line.split()

    for word in words:
        w = re.sub(r'\W+', '', word)
        freq_dict[w] += 1
    
for w in freq_dict.keys():
    # print(type(key))
    key = w + '|' + file
    print ('%s\t%s' % (key, freq_dict[w]))
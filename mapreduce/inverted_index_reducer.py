#!/usr/bin/env python
  
from operator import itemgetter, pos
import sys
  
curr_count = 0
current_word = None

# read the entire line from STDIN
for line in sys.stdin:
    output = []
    # remove leading and trailing whitespace
    line = line.strip()
    
    try:
        # slpiting the data on the basis of tab we have provided in mapper.py
        word, value = line.split('\t')
        value = int(value)
    except ValueError:
        continue

    if current_word == word:
        curr_count += value
    else:
        if current_word:
            if curr_count ==0:
                print ('%s\t%s' % (current_word, value))
            else:
                print ('%s\t%s' % (current_word, curr_count))

        current_count = value
        current_word = word

if current_word == word:
    if curr_count ==0:
        print ('%s\t%s' % (current_word, value))
    else:
        print ('%s\t%s' % (current_word, curr_count))

    # postings = value.split(',')
    # # print(value)
    # # print(term, postings)
    # for posting in postings:
    #     try: 
    #         file, freq = posting.split('|')
    #     except ValueError:
    #         output.append((value, 0))
    #         continue

    #     output.append((file, freq))
    
    # output.sort(key=lambda x: x[1], reverse=False)

    # for pair in output:
    #     value = pair[0] + '|' + str(pair[1])
    #     print ('%s\t%s' % (term, value))
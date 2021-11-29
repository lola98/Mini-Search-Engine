# import sys because we need to read and write data to STDIN and STDOUT
import sys, re
  
# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
      
    # we are looping over the words array and printing the word
    # with the count of 1 to the STDOUT
    for word in words:
        w = re.sub(r'\W+', '', word).lower()
        if len(w) >0:
            print('%s\t%s' % (w, 1))
        
        

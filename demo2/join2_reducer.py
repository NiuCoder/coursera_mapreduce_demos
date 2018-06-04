#!/usr/bin/env python
import sys
prev_word = None
line_cnt = 0
running_total = 0
abc_found = False
for line in sys.stdin:
    line = line.strip()
    key_value = line.split("\t")
    line_cnt = line_cnt+1
    key_in = key_value[0]
    value_in = key_value[1]
    curr_word = key_value[0]    

    if curr_word != prev_word:
        if line_cnt>1:
            if abc_found:
                print('{0}\t{1}'.format(prev_word,running_total))
                abc_found = False
        prev_word = curr_word
        if value_in.isdigit():
            running_total = int(value_in)
    elif value_in.isdigit():
        running_total += int(value_in)
    elif value_in == 'ABC':
        abc_found = True
if prev_word == curr_word:
    print('{0}\t{1}'.format(prev_word,running_total))

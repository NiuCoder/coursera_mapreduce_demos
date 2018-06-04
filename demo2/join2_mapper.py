#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    key_value = line.split(",")
    key_in = key_value[0]
    value_in = key_value[1]
    if value_in=='ABC' or value_in.isdigit():
        print('%s\t%s' % (key_in,value_in))
    else:
        continue

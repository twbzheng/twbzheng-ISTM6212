#!/usr/bin/env python

"""
A filter that _split words in each line_.
"""

import fileinput


def process(line):
    """For each line of input,split the words by blanks."""
    l = line.split()
    for i in l:
        print (i.strip().lstrip('"').rstrip(',').rstrip(',"').rstrip(';').rstrip('!').rstrip('?').rstrip('-').rstrip('.').rstrip(')').rstrip('--'))


for line in fileinput.input():
    process(line[:-1])

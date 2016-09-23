#!/usr/bin/env python

"""
A filter that _________.
"""

import fileinput


def process(line):
    """For each line of input, _____."""   
    stopwords = ["a","an","and","are","as","at", "be", "that", "it","the","for","is","of","to"]    
    if line not in stopwords:
        print(line.strip())




for line in fileinput.input():
    process(line)
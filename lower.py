#!/usr/bin/env python

"""
A filter that _transform text into lower case._.
"""

import fileinput


def process(line):
    """For each line of input, transform all characters into lower case."""
    print(line.lower())


for line in fileinput.input():
    process(line)

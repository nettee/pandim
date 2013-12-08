#!/usr/bin/env python3

""" yate: html generator
"""

def para(p):
    return '<p>{}</p>'.format(p)

def header(s, level=3):
    return '<h{0}>{1}</h{0}>'.format(level, s)

def comment(s):
    return '<!-- {} -->'.format(s)



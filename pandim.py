#!/usr/bin/env python3

""" pandim: html file generator
use yate as support
"""

import sys
import re
import argparse

import yate
    
def pandim(line, args):
    line = line.rstrip('\n')
    if line.startswith('#'):
        npounds = re.match(r'#+', line).group(0)
        line = line.lstrip('#').lstrip(' ')
        line = yate.header(line, len(npounds))
    else:
        line = yate.para(line)

    return line

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--title')
    
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    templ_1 = """<!DOCTYPE html>
    <html lang='zh' xmlns="http://www.w3.org/1999/xhtml">
      <head>
        <meta charset='utf-8' />
        <title>{title}</title>
      </head>
      <body> """
    templ_2 = """</body> </html> """

    if args.title:
        print(templ_1.format(title=args.title))
    else:
        print(templ_1.format(title='a.html'))

    for line in sys.stdin:
        line = pandim(line, args)
        print(line)
    print(templ_2)

#!/usr/bin/env python3

""" pandim: html file generator
use yate as support
"""

import sys
import argparse

import yate
    
def pandim(args):
    for line in sys.stdin:
        line = line.rstrip('\n')
        if line.startswith('#'):
            line = yate.header(line.lstrip('#'))
        print(line)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--title')
    
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    templ_1 = """<!DOCTYPE html>
    <html lang='zh' xmlns="http://www.w3.org/1999/xhtml">
      <head><title>{title}</title></head>
      <body> """
    templ_2 = """</body> </html> """
    print(templ_1.format(title=args.title))
    pandim(args)
    print(templ_2)

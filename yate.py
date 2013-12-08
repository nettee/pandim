#!/usr/bin/env python3

# version: 0.2.1
# 2013-12-8

""" yate: html generator
"""

import re

def escape(line):
    esc_map = {'&' : '&amp;',
            '<' : '&lt;',
            '>' : '&gt;',
        }
    return ''.join(esc_map[c] if c in esc_map else c for c in line)

def para(p):
    p = escape(p)
    def _code_inline(mobj):
        return code_inline(mobj.group(1))
    p = re.sub(r'``(.*)``', _code_inline, p)
    return '<p>{}</p>'.format(p)

def header(s, level=3):
    return '<h{0}>{1}</h{0}>'.format(level, escape(s))

def comment(s):
    return '<!-- {} -->'.format(escape(s))

def blockquote(lines):
    return ("<blockquote>" + '\n'.join(lines) + "</blockquote>")

def code(lines):
    return "<pre><code>" + '\n'.join(lines) + "</code></pre>"

def code_inline(s):
    return "<code>{}</code>".format(s)




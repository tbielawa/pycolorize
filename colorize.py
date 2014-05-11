#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The MIT License (MIT)
#
# Copyright © 2014 Tim Bielawa <timbielawa@gmail.com>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

BG = {}
BG['BLACK'] = '\033[40m'
BG['RED'] = '\033[41m'
BG['GREEN'] = '\033[42m'
BG['YELLOW'] = '\033[43m'
BG['BLUE'] = '\033[44m'
BG['PURPLE'] = '\033[45m'
BG['CYAN'] = '\033[46m'
BG['LIGHTGRAY'] = '\033[47m'
COLORS = {}
COLORS['RESTORE'] = '\033[0m'
COLORS['RED'] = '\033[00;31m'
COLORS['GREEN'] = '\033[00;32m'
COLORS['YELLOW'] = '\033[00;33m'
COLORS['BLUE'] = '\033[00;34m'
COLORS['PURPLE'] = '\033[00;35m'
COLORS['CYAN'] = '\033[00;36m'
COLORS['TEAL'] = '\033[00;36m'
COLORS['LIGHTGRAY'] = '\033[00;37m'
COLORS['LRED'] = '\033[01;31m'
COLORS['LGREEN'] = '\033[01;32m'
COLORS['LYELLOW'] = '\033[01;33m'
COLORS['LBLUE'] = '\033[01;34m'
COLORS['LPURPLE'] = '\033[01;35m'
COLORS['LCYAN'] = '\033[01;36m'
COLORS['WHITE'] = '\033[01;37m'


def colorize(item, color=None, underline=False, background=None):
    if underline:
        ul = "\033[4m"
    else:
        ul = ''

    if background:
        bg = BG[background.upper()]
    else:
        bg = ""

    if color:
        c = COLORS[color.upper()]
    else:
        c = COLORS["WHITE"]

    return "%s%s%s%s%s%s" % (COLORS['RESTORE'],
                             c,
                             bg, ul, item,
                             COLORS['RESTORE'])


def hr(msg=None, color=None):
    print colorize("---------------------------------------------", color=color)
    if msg:
        print colorize("| %s" % msg, color=color)
        print colorize("---------------------------------------------", color=color)


def main():
    hr(msg="Just different Text colors", color="cyan")

    print "Red text, black background:"
    print colorize("Red text, black background:", "red")
    print "Green text, black background:"
    print colorize("Green text, black background:", "green")
    print "Yellow text, black background:"
    print colorize("Yellow text, black background:", "yellow")

    hr(msg="Text with backgrounds", color="cyan")

    print "White text, red background:"
    print colorize("White text, red background:", color="white", background="red")
    print "White text, green background:"
    print colorize("White text, green background:", color="white", background="green")
    print "Yellow text, lightgray background:"
    print colorize("Yellow text, lightgray background:", color="yellow", background="lightgray")

    hr(msg="Different text colors, with underlines", color="cyan")

    print "Red underlined text, black background:"
    print colorize("Red underlined text, black background:", "red", underline=True)
    print "Green underlined text, black background:"
    print colorize("Green underlined text, black background:", "green", underline=True)
    print "Yellow underlined text, black background:"
    print colorize("Yellow underlined text, black background:", "yellow", underline=True)

    hr("Underlined texts with backgrounds", color="cyan")

    print "White underlined text, red background:"
    print colorize("White underlined text, red background:", color="white", background="red", underline=True)
    print "White underlined text, green background:"
    print colorize("White underlined text, green background:", color="white", background="green", underline=True)
    print "Yellow underlined text, lightgray background:"
    print colorize("Yellow underlined text, lightgray background:", color="yellow", background="lightgray", underline=True)


if __name__ == '__main__':
    main()

#!/usr/bin/python -tt
import argparse
from collections import Counter
import re


def purge(word):
    if not word.isalpha():
        word = ''.join(ch for ch in word if ch.isalpha())
    return word

def count(textfile):
    content = textfile.read().lower().split()
    words = [purge(w) for w in content]
    #words = re.split(r"[^a-z']", content)
    return Counter(words)

def asc(words):
    return sorted(words.items())

def top(words, qty):
    return sorted(words.items(), key=lambda t: t[1], reverse=True)[:qty]

def count_words(textfile):
    return asc(count(textfile))

def top_words(textfile, qty=20):
    return top(count(textfile), qty)

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():

    parser = argparse.ArgumentParser(description='Conta palavras.')
    parser.add_argument('-c', '--count', action='store_true', help='Conta ocorrências.')
    parser.add_argument('-t', '--topcount', type=int, help='Mais frequentes.')
    parser.add_argument('textfile', type=argparse.FileType(), help='Arquivo texto.')

    options = parser.parse_args()

    if options.count:
        words = count_words(options.textfile)

        for w, c in words:
            print('%s: %d' % (w, c))

    elif options.topcount:
        words = top_words(options.textfile, options.topcount)

        for i, (w, c) in enumerate(words, start=1):
            print('{:0=2d} {}: {}'.format(i, w, c))


def main():
    pass
    # tkinter

if __name__ == '__main__':
    main()

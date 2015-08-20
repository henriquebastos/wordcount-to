from collections import Counter
import re


def count(textfile):
    content = textfile.read().lower()
    words = re.split(r"[^a-z']", content)
    return Counter(words)

def asc(words):
    return sorted(words.items())

def top(words, qty):
    return sorted(words.items(), key=lambda t: t[1], reverse=True)[:qty]

def lines(words):
    return '\n'.join('%s: %d' % t for t in words)

def count_words(textfile):
    return asc(count(textfile))

def top_words(textfile, qty=20):
    return top(count(textfile), qty)


__all__ = ['count_words', 'top_count', 'lines']

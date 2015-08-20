import argparse
from core import count_words, top_words


def cli():
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

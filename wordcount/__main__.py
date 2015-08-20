import sys

from wordcount.gui import gui
from wordcount.cli import cli


if len(sys.argv) < 2:
    gui()
else:
    cli()

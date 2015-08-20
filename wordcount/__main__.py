import sys

from gui import gui
from cli import cli


if len(sys.argv) < 2:
    gui()
else:
    cli()

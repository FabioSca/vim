

from Npp import *
import re

first = True
def found(line, m):
    global first
    pos = editor.positionFromLine(line)
    if first:
        editor.setSelection(pos + m.end(), pos + m.start())
        first = False
    else:
        editor.addSelection(pos + m.end(), pos + m.start())

regex = notepad.prompt('Search for:', 'Select all results')
if regex:
    editor.setMultipleSelection(True)
    lines = editor.getUserLineSelection()
    editor.pysearch(regex, found, 0, lines[0], lines[1])
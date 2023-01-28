from Npp import *


notepad.menuCommand(MENUCOMMAND.SEARCH_CLEAR_BOOKMARKS)
linesBookmarked = []

def onMatch(lineNumber, match):
  if lineNumber not in linesBookmarked:
    lineStartPos = editor.positionFromLine(lineNumber)
    editor.gotoPos(lineStartPos)
    #notepad.menuCommand(MENUCOMMAND.SEARCH_TOGGLE_BOOKMARK)
    notepad.menuCommand(MENUCOMMAND.HIDELINES)
    linesBookmarked.append(lineNumber)

editor.pysearch("Pos", onMatch)

from Npp import *
import re


fileName = notepad.getCurrentFilename()
maxFuncs = 30
defaultFoldLevel = 1024
def resetFoldLevel(contents, lineNumber, totalLines):
        editor.setFoldLevel(lineNumber, defaultFoldLevel)

# only run this on .gm files
if not (fileName.endswith(".gm")):
        editor.forEachLine(resetFoldLevel)
        editor.documentStart()
        editor.searchAnchor()
        counter = 0

        while 1:
                # make the line containing "= function" the folding header
                found = editor.searchNext(0, "= function")
                if (found < 0 | counter >= maxFuncs):
                        break
                editor.searchAnchor()
                editor.setFoldLevel(editor.getUserLineSelection()[0], defaultFoldLevel | FOLDLEVEL.HEADERFLAG )

                # increase fold level for everything inside the curly brackets
                editor.searchAnchor()
                editor.searchNext(0, "{")
                cursorpos = editor.getUserCharSelection()
                editor.setSelection( cursorpos[0], editor.braceMatch(cursorpos[0])+1 )
                bracepos = editor.getUserLineSelection()
                i = bracepos[0]
                while i <= bracepos[1]:
                        editor.setFoldLevel(i, defaultFoldLevel+1)
                        i+=1
                counter += 1
                editor.searchAnchor()
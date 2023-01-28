

from Npp import *
import re


defaultFoldLevel = 1024

defaultFoldLevel2 = 9216
defaultFoldLevel3 = 1026

editorContent = editor.getText()

prima = defaultFoldLevel

numLines = -1

inizio = 0
fine = 0

conta = 0

listalinee = editorContent.splitlines()


for nline in range(len(listalinee)):
  numLines += 1
  line = listalinee[nline]
  line = line.lstrip()
  
  console.write(str(editor.getFoldLevel(numLines)) + " " + str(line) + "\n" )
  
  if nline>40:
   break
  

notepad.messageBox( str(conta) + " hided lines!!" )





from Npp import *
import re


defaultFoldLevel = 1024

editorContent = editor.getText()

prima = ""

numLines = 0

inizio = 0
fine = 0

conta = 0

listalinee = editorContent.splitlines()

skippaline = ["CHEXA","CIFHEX"]

for nline in range(len(listalinee)):
  numLines += 1
  line = listalinee[nline]
  #console.write( line + str(line != prima) + "\n" )
  
  #console.write( str((prima.strip() in skippaline)) + str( (line[0:8].replace("+","").replace(" ","") == "") ) + "\n" )
  
  if (prima.strip() in skippaline) and (line[0:8].replace("+","").replace(" ","") == "") :
    
    fine = numLines
    continue
  
  if (line[0:8] != prima):
    fine = fine-1
    if (fine > inizio):
        #console.write( "hide *** " + str(inizio) + "," + str(fine) + "\n" )
        editor.hideLines(inizio,fine)
        conta = conta + (fine-inizio)
        fine = inizio
        
    inizio = numLines
    
  else:
    #console.write( "===" )
    fine = numLines
    #editor.setFoldLevel(editor.getUserLineSelection()[0], 1)
    
  
  prima = line[0:8]
  
  """
  if numLines>2000:
    break
  else:
    console.write( "******** " + str(inizio) + "," + str(fine) + "\n" )
  """



notepad.messageBox("Collassate " + str(conta) + " linee!!" )


#editor.hideLines(1,10)



from Npp import *
#import re


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
  
  if (line[0:1] == "$") or (line[0:1] == " "):
    # se si tratta di un commento riga normale
    #editor.setFoldLevel(numLines , defaultFoldLevel)
    
    continue
  
  
  
  if ( line[0:1].isdigit() ) or (line[0:1].replace(" ","")  == "") \
   or (line[0:1] == "-") or (line[0:1] == "+") :
          
        fine = numLines
        
        
  else:
        if (fine > inizio+1):
                
            editor.setFoldLevel(inizio , defaultFoldLevel2)
            for ii in range(inizio+1,fine+1):
                editor.setFoldLevel(ii , defaultFoldLevel3)
            conta = conta + (fine-inizio)
            
          
        inizio = numLines 
        
        
        
        #conta = conta + 1
        
  

notepad.messageBox( str(conta) + " hided lines!!" )



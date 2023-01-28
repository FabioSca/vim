

from Npp import *

console.write( "Start NASTRAN_HIDE4 \n" )

defaultFoldLevel = 1024

defaultFoldLevel2 = 9216
defaultFoldLevel3 = 1026

editorContent = editor.getText()

prima = ""

numLines = 0

inizio = 0
fine = 0

conta = 0

listalinee = editorContent.splitlines()

skippaline = ["CHEXA","CIFHEX","NLSTEP"]



doppio = False

for nline in range(len(listalinee)):
  numLines += 1
  line = listalinee[nline]
  
  
  
  # ci sono delle righe che finiscono su due righe
  if (doppio) and (line[0:8].replace("+","").replace("*","").replace(" ","").replace(","," ") == "") :
    
    fine = numLines
    doppio = False
    continue
  
  if (line[0:8].replace("*","").strip() != prima.replace("*","").strip() ):
    
    fine = fine-1
    if (fine > inizio+1):
    
        editor.gotoLine(inizio)
        start = editor.getCurrentPos()
        
        editor.gotoLine(fine)
        end = editor.getCurrentPos()
        
        editor.setSelectionStart(start)
        editor.setSelectionEnd(end)
        
        editor.copy()
        
        notepad.runMenuCommand("View","Hide Lines")
        
        console.write( str(start) + " " + str(end) + "\n")
        conta = conta + (fine-inizio)
        fine = inizio
        
    inizio = numLines
    if len(listalinee) > inizio :
        if listalinee[inizio][0:1] == "+":
            inizio = inizio-1
    
  else:
    fine = numLines
    
  
  prima = line[0:8]
  
  if (prima.strip() in skippaline)  or ("*" in prima.strip() ):
    doppio = True
  else:
    doppio = False
  

console.write( "Done ... !!! \n" )



#notepad.runMenuCommand("View","Hide Lines")

#notepad.messageBox( str(conta) + " hided lines!!" )





from Npp import *
import os
import subprocess

# CQUAD4

line = editor.getSelText()

stringa = '"C:\Program Files (x86)\Internet Explorer\iexplore.exe" file:///C:/MSC.Software/exo6_v1_9m/Doc/pdf_nastran/reference/qrg/qrg.pdf#' + str(line)

#stringa = '"C:\Program Files (x86)\Internet Explorer\iexplore.exe" file:///C:/MSC.Software/MSC_Nastran/20122/msc20122/Doc/pdf_nastran/reference/qrg/qrg.pdf#' + str(line)
#os.system(stringa)

#pid = subprocess.Popen([sys.executable, stringa], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)


pid = subprocess.Popen(stringa)

console.write( "******** " + str(stringa) + "\n" )


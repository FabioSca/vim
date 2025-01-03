#!/usr/bin/python


"""
=================================================================================================
@revision: 8
@date    : 3 Gennato 2018   ( 13:50:09 )
@author  : fabio
=================================================================================================
"""


'''
START MY IMPORT
START MY INIT
START MY CODE

11-09-2012
- Testata in ambiente linux puo essere lanciata direttamente non ha bisogno del .bat
- Adesso anche le prime righe con import vengono caricate
- Le righe my code vengono lette e poi riportate prima del main

Created on 25/ago/2012


'''


import os

import sys

import Leonardo


def main(filename2):



    if ".ui" not in filename2:
        print(("Error not a file *.ui  " , filename2))
        sys.exit(1)

    dirqui = os.path.dirname(os.path.abspath(filename2))
    os.chdir(dirqui)
    print("in folder ", os.getcwd() )

    filename2 = os.path.basename(filename2)
    filename2py = filename2.replace(".ui",".py")
    filename2bak = "." + filename2.replace(".ui",".py.bak")


    # il file batch provvede a copiare
    # il file py se esiste in un file di bak

    if "linux" in sys.platform :
        stringa = "cp %s %s " % (filename2py,filename2bak)
        print(stringa)
        os.system(stringa)
    else:
        stringa = "copy %s %s " % (filename2py,filename2bak)
        print(("copio il python backup",stringa))
        os.system(stringa)
    
    # produco python da ui
    # e provvede a generare dal file ui il codice python che salvo temporaneamente in un txt
    
    filename2txt = "." + filename2.replace(".ui",".txt")

    if "linux" in sys.platform:
        software_py = Leonardo.LeoPaths.ottieni_path("Python_linux")
    else:
        software_py = Leonardo.LeoPaths.ottieni_path("Python_win")
            
    #software_py = r"C:\DE-Python\envs\LEO4\Scripts\python"
    software_dir = os.path.dirname(software_py)
    
    percorso_uic5 = os.path.join( software_dir, "pyuic5.exe" )
    #print("--- ", percorso_uic5)
    if not os.path.exists(percorso_uic5):
        percorso_uic5 = "%s\\Library\\bin\\pyuic5" % software_dir
    if not os.path.exists(percorso_uic5):
        percorso_uic5 =  "%s\\Scripts\\pyuic5" % software_dir
    if not os.path.exists(percorso_uic5):
        percorso_uic5 =  "%s\\Library\\bin\\pyuic5" % software_dir
    if not os.path.exists(percorso_uic5):
        percorso_uic5 =  "%s\\envs\\LEO4\\Scripts\\pyuic5" % software_dir
    stringa = "%s -o %s -x %s " % (percorso_uic5, filename2txt, filename2)
    print(stringa)
    
    os.system(stringa)

    print("------------")
    



    filename = "." + filename2py.replace(".py",".txt")

    # esiste il file di backup
    # se si potrebbe contenere user code che voglio ricopiare

    filebak = filename.replace(".txt",".py.bak")
    esistebak = 0
    importstring = []
    mainstring = []
    mycodestring = []
    mycodestringinit = []
    importstring2 = []

    #OPERAZIONI DAL FILE DI BACKUP
    if os.path.exists(filebak):
        print(("esiste file bak", filebak))
        esistebak = 1

        filei2 = open(filebak,"r")
        while 1:
            linea2 = filei2.readline()  # file di backip di prima da cui leggo old impostazioni

            if not linea2:
                break

            if "START MY IMPORT" in linea2:
                while 1:
                    importstring.append(linea2)
                    linea2 = filei2.readline()
                    if not linea2:
                        break

                    if "END MY IMPORT" in linea2:
                        importstring.append(linea2)
                        break



            if "import" in linea2.lstrip()[0:6]:
                importstring.append(linea2)

            if ".hide" in linea2:
                mainstring.append(linea2)

            if "START MY CODE" in linea2:
                while 1:
                    linea3 = filei2.readline()
                    if not linea3:
                        break

                    if "END MY CODE" in linea3:
                        break

                    mycodestring.append(linea3)
                break

            if "START MY INIT" in linea2:
                while 1:
                    linea3 = filei2.readline()
                    if not linea3:
                        break

                    if "END MY INIT" in linea3:
                        break

                    mycodestringinit.append(linea3)


        filei2.close()

    print("Working dir ",os.getcwd())

    print(filename2py)

    # adesso prendo il file txt e inietto il mio user code

    filenameout = filename2py

    if os.path.exists(filename2):
        filei = open(filename2,"r")
        fileo = open(filenameout,"w")

        retranslatedone = 0
        scrittomycode = 0

        ignore_list = ["from mplwidget import MplWidget", "import resource_rc", "from PyQt5 import QtWebKit",
                       "from QVTKWidget import QVTKWidget"]

        while 1:
            linea = filei.readline()    # leggo dal .filename.txt creato da traslatore standard

            if not linea:
                break

            if linea.strip().replace("\n","") in ignore_list:
                continue

            if "self.retranslateUi" in linea:

                for linea2 in mainstring:
                    print(linea2)
                    fileo.write(linea2)

                fileo.write("\n")

            if ":./images/images" in linea:
                linea = linea.replace(":./images/images","./images")
            elif ":/images/images" in linea:
                linea = linea.replace(":/images/images","./images")


            if "QtCore.QObject.connect" in linea:


                if "Dialog.accept" in linea:
                    print("..")
                elif "Dialog.reject" in linea:
                    print("..")
                elif ("MainWindow.close" in linea) or ("Dialog.close" in linea):
                    print("..")
                else:
                    linea = linea.replace("Dialog.","self.")
                    linea = linea.replace("MainWindow.","self.")

            if "import" in linea:
                importstring2.append(linea)

            if ("MainWindow" in linea) and ("self." in linea):
                if ".connect(" in linea:
                    if ".close" not in linea:
                        linea = linea.replace("(MainWindow.","(self.")

            if ("Dialog" in linea) and ("self." in linea):
                if ".connect(" in linea:
                    if ".accept" in linea:
                        pass
                    elif ".reject" in linea:
                        pass
                    else:
                        linea = linea.replace("(Dialog.","(self.")

            if "def retranslateUi" in linea:

                fileo.write("    \n")
                fileo.write("        # START MY INIT\n")

                #fileo.write("    \n")
                if esistebak == 1:
                    for linea2 in mycodestringinit:
                        fileo.write(linea2)

                #fileo.write("    \n")
                fileo.write("        # END MY INIT    \n")
                fileo.write("    \n")

                fileo.write(linea)

                retranslatedone = 1

                continue

            if (("if __name__ == \"__main__\":" in linea) or (("import" in linea.lstrip()[0:7]) and (retranslatedone == 1))) and (scrittomycode == 0) :

                print(("Debug-----", (("if __name__ == \"__main__\":" in linea) or (("import" in linea) and (retranslatedone == 1)) and (scrittomycode == 0)), scrittomycode))
                fileo.write("    \n")
                fileo.write("    # START MY CODE    \n")

                #fileo.write("    \n")
                if esistebak == 1:
                    for linea2 in mycodestring:
                        fileo.write(linea2)

                #fileo.write("    \n")
                fileo.write("    # END MY CODE    \n")
                fileo.write("    \n")


                scrittomycode = 1

                fileo.write(linea)
                #linea = filei.readline()
                #fileo.write(linea)

            elif "class" in linea:
                for newlin in importstring:
                    if newlin in importstring2:
                        continue
                    else:
                        #if (newlin[0:1] == " "):
                        #    continue
                        #else:
                        fileo.write(newlin)

                fileo.write("\n")
                fileo.write(linea)


            else:

                #print linea
                if "    import sys" == linea.replace("\n",""):
                    print(("ecco", linea))
                    linea = "    import sys  # @Reimport\n"

                fileo.write(linea)




        filei.close()
        fileo.close()
    
    else:
        print("File does not exist ", filename2 )


    print("Done script fromuitopy ! ")






if __name__ == '__main__':

    #

    print(("Argomenti", sys.argv))

    print((" start from ui " + os.getcwd ()))

    #
    test=False

    if test:
        print("test??")
        os.chdir (r"C:\Projects\ALA5\AllowablesParameters")
        main("AllowablesParameters.ui")
    else:
        filename2 = sys.argv[1]  # con estensione .ui

        main(filename2)


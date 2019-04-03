#-*- coding: utf-8 -*-
from time import sleep
import svg_parser as PARSER
import scaler as SCALER
import plotterio as IO
import os.path

#var------
lastfilepath = "" #do not edit
#-------

if __name__ == "__main__":
    SCALER.initScale()
    drucken()


def drucken():
    print("auf Antwort warten...")
    print("-V---P-l-o-t-t-e-r-----------------------------------------------")
    sleep(1)
    print("Bitte den Anweisungen hier folgen!")
    print("-> mit [Strg] + [C] beenden")
    sleep(2)
    print("-Viel Spass...")
    PARSER.initParser()
    lastfilepath = selectFile()
    PARSER.parse(lastfilepath)
    print("Druck fertig###########################################")
    print("Noch mal selbe Datei drucken ?")
    answer = raw_input("j/n:")
    if(answer.startswith("j") or answer.startswith("y")):
        nochmalDrucken()
    drucken()
    return


def nochmalDrucken():
    print("auf Antwort warten...")
    sleep(1)
    print("Bitte den Anweisungen hier folgen!")
    print("-> mit [Strg] + [C] beenden")
    PARSER.initParser()
    sleep(2)
    PARSER.parse(lastfilepath)
    print("Druck fertig :) :) :) :) :) :)")
    print("Noch mal selbe Datei drucken ?")
    answer = raw_input("j/n:")
    if(answer.startswith("j") or answer.startswith("y")):
        nochmalDrucken()
    return

def selectFile():
    print("welche Datei soll gedruckt werden?")
    filepath = raw_input("Dateiname:")
    if(os.path.isfile(filepath) and filepath.endswith(".svg")):
        return filepath
    else:
        filepath += ".svg"
        if(os.path.isfile(filepath)):
            return filepath
        else:
            print("Die Datei kann nicht gefunden werden!")
            return selectFile()

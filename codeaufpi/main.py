#-*- coding: utf-8 -*-
from time import sleep
import svg_parser as PARSER
import scaler as SCALER
import plotterio as IO
import os.path

#var------
lastfilepath = "" #do not edit
#-------

# Frage nach der Druckdatei im Ordner Dateien
# Überprüfung, ob sie vorhanden ist und ggf Anhängen der Endung ".svg"
def selectFile():
    print("welche Datei im Ordner Dateien/ soll gedruckt werden?")
    filepath = "dateien/" + raw_input("Dateiname:")
    if(os.path.isfile(filepath) and filepath.endswith(".svg")):
        return filepath
    else:
        # Anhaengen der Dateiendung, Ueberpruefen und Rueckgabe
        filepath += ".svg"
        if(os.path.isfile(filepath)):
            return filepath
        else:
            print("Die Datei kann nicht gefunden werden!")
            return selectFile()

# innere Loop dieser Methode, um Datei wiederholt zu drucken
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

# main Loop für den Druckvorgang
def drucken():
    global lastfilepath
    print("auf Antwort warten...")
    print("-V---P-l-o-t-t-e-r-----------------------------------------------")
    sleep(1)
    print("Bitte den Anweisungen hier folgen!")
    print("-> mit [Strg] + [C] beenden")
    sleep(2)
    print("-Viel Spass...")
    #Einrichten des Parsers
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


if __name__ == "__main__":
    SCALER.initScale()
    drucken()
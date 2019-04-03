#-*- coding: utf-8 -*-
from time import sleep
import svg_parser
import scaler as SCALER
import plotterio as IO

if __name__ == "__main__":
    SCALER.initScale()
    while(True):
        print("auf Antwort warten...")
        print("-V---P-l-o-t-t-e-r-----------------------------------------------")
        sleep(1)
        print("Bitte den Anweisungen hier folgen!")
        print("-> mit [Strg] + [C] beenden")
        sleep(2)
        print("-Viel Spass...")
        svg_parser.initParser()
        print("welche Datei soll gedruckt werden?")
        filepath = raw_input("Dateiname:")
        if(!filepath.endswith(".svg")):
            filepath += ".svg"
        svg_parser.parse(filepath)
        print("Druck fertig###########################################")
        print("Noch mal selbe Datei drucken ?")
        IO.aufOKWarten()
        sleep(3)

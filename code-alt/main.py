#-*- coding: utf-8 -*-
from time import sleep
import svg_parser
import scaler as SCALER

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
        svg_parser.parse_standart()
        print("Druck fertig")
        sleep(3)
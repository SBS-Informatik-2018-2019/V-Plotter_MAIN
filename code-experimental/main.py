#-*- coding: utf-8 -*-
from time import sleep
import filereader as FILER
import scaler as SCLR
import plotterioPRE as IO

if __name__ == "__main__":
    print("[SYS]: Warten...")
    print("[INFO]: Bitte den Anweisungen folgen!")
    print("[INFO]: mit [Strg] + [C] beenden")
    print("[INFO]: Schlitten auf (800/800) einstellen")
    IO.aufOKWarten()
    print("[SYS]: SVG-Datei lesen und in Token umwandeln...")
    FILER.svgLesen()
    sleep(2)
    print("[SYS]: fertig")
    print("[SYS]: Tokens lesen und in Koordinaten umwandeln...")
    FILER.tokensLesen()
    sleep(2)
    print("[SYS]: fertig")
    print("[SYS]: Scalieren...")
    sleep(1)
    print("[SYS]: fertig")
    print("[SYS]: Koordinaten lesen und Motorbewegungen vorbereiten...")
    SCLR.init()
    sleep(2)
    print("[SYS]: fertig")
    print("[SYS]: Motorbewegungen lesen und Drucken...")
    FILER.linesLesen()
    sleep(2)
    print("[SYS]: fertig")
    sleep(3)
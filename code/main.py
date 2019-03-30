#-*- coding: utf-8 -*-
from time import sleep
import filereader as FILER

if __name__ == "__main__":
    print("[SYS]: Warten...")
    print("[INFO]: Bitte den Anweisungen folgen!")
    print("[INFO]: mit [Strg] + [C] beenden")
    sleep(2)
    print("[SYS]: SVG-Datei lesen und in Token umwandeln...")
    FILER.svgLesen()
    sleep(2)
    print("[SYS]: fertig")
    print("[SYS]: Tokens lesen und in Koordinaten umwandeln...")
    FILER.tokensLesen()
    sleep(2)
    print("[SYS]: fertig")

    print("[SYS]: Koordinaten lesen und Motorbewegungen vorbereiten...")
    #TODO
    sleep(2)
    print("[SYS]: fertig")
    print("[SYS]: Motorbewegungen lesen und Drucken...")
    #TODO
    print("[SYS]: fertig")
    sleep(3)
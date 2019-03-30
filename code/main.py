#-*- coding: utf-8 -*-
from time import sleep
import filereader as FILER

if __name__ == "__main__":
    print("[SYS]: Warten...")
    print("[INFO]: Bitte den Anweisungen folgen!")
    print("[INFO]: mit [Strg] + [C] beenden")
    sleep(2)
    print("[SYS]: File lesen...")
    FILER.svgLesen()
    sleep(2)
    print("[SYS]: fertig")
    print("[SYS]: Motorbewegungen vorbereiten...")
    #TODO
    sleep(2)
    print("[SYS]: fertig")
    print("[SYS]: Drucken...")
    #TODO
    print("[SYS]: fertig")
    sleep(3)
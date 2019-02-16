#-*- coding: utf-8 -*-
from time import sleep
import parser as PARSER

if __name__ == "__main__":
    print("-V---P-l-o-t-t-e-r-----------------------------------------------")
    sleep(1)
    print("Bitte den Anweisungen hier folgen!")
    print("-> mit [Strg] + [C] beenden")
    sleep(2)
    print("-Viel Spass...")
    PARSER.parse("file.svg")
    
    

#-*- coding: utf-8 -*-
from time import sleep
import svg_parser
import PyV8

if __name__ == "__main__":
    print("auf Antwort warten...")
    print("-V---P-l-o-t-t-e-r-----------------------------------------------")
    sleep(1)
    print("Bitte den Anweisungen hier folgen!")
    print("-> mit [Strg] + [C] beenden")
    sleep(2)
    print("-Viel Spass...")
    
    ctx = PyV8.JSContext()
    ctx.enter()

    js = """
    function escramble_758(){
    var a,b,c
    a='+1 '
    b='84-'
    a+='425-'
    b+='7450'
    c='9'
    document.write(a+c+b)
    }
    escramble_758()
    """

    print ctx.eval(js.replace("document.write", "return "))
    
    svg_parser.parse("file.svg")
    
    

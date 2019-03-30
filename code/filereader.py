#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os.path as OSPATH
import sys as SYS
import tokenizer as TOKER
import pathparser as PP
import polylineparser as PLP
import scaler as SCL

#VARIABLES#######################################
SVG_FILE = "file.svg"
TOKEN_FILE = "tokens.vplotter"
LINES_FILE = "lines.vplotter"
nameSpace={'svgNs':'http://www.w3.org/2000/svg'}
#END VARIABLES####################################

# Start des Einlesens einer svg-Datei
def svgLesen():
    if(OSPATH.exists(SVG_FILE)):
        svgRootElement = ET.parse(SVG_FILE).getroot()
        # Einlesen eines Path
        if (svgRootElement.find("svgNs:path", nameSpace) != None):
            pathElement = svgRootElement.find("svgNs:path", nameSpace)
            path = pathElement.get('d')
            TOKER.tokenize_path(path)
        # Anders wird eine Polyline eingelesen
        elif (svgRootElement.find("svgNs:polyline", nameSpace) != None):
            polylineElement = svgRootElement.find("svgNs:polyline", nameSpace)
            points = polylineElement.get('points')
            TOKER.tokenize_polyline(points)
        else:
            SYS.exit("[WARN]: in File:" + SVG_FILE + " wurde kein Path oder Polyline gefunden!")
    else:
        SYS.exit("[WARN]: File: " + SVG_FILE + " konnte nicht gefunden werden!")
    return

def tokensLesen():
    if(OSPATH.exists(TOKEN_FILE)):
        file = open(TOKEN_FILE, "rt")
        typ = file.readline()
        if(typ.startswith("is_polyline")):
            PLP.parse(file)
        elif(typ.startswith("is_path")):
            PP.parse(file)
        else:
            SYS.exit("[WARN]: File: " + TOKEN_FILE + " ist korrupt!")
        file.close()
    else:
        SYS.exit("[WARN]: File: " + TOKEN_FILE + " konnte nicht gefunden werden!")
    return

def linesLesen():
    if(OSPATH.exists(LINES_FILE)):
        file = open(LINES_FILE, "rt")
        SCL.scale(file)
        file.close()
    else:
        SYS.exit("[WARN]: File: " + LINES_FILE + " konnte nicht gefunden werden!")
    return
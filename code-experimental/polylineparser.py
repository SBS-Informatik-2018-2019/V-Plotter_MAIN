# -*- coding: utf-8 -*-

#VARIABLES#######################################
LINEPOINTS_FILE = "lines.vplotter"
#END VARIABLES####################################


def parse(openfile):
    line_file = open(LINEPOINTS_FILE, "wt")
    token1 = openfile.readline().strip("\n").strip()
    token2 = openfile.readline().strip("\n").strip()
    float1 = float(token1)
    float2 = float(token2)
    line_file.write("M"+ " " + str(float1) +" " + str(float2) + "\n")
    while(token1 and token2):
        float1 = float(token1)
        float2 = float(token2)
        line_file.write("L"+ " " + str(float1) +" " + str(float2) + "\n")
        token1 = openfile.readline().strip("\n").strip()
        token2 = openfile.readline().strip("\n").strip()
    return

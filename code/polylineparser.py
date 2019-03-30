# -*- coding: utf-8 -*-

#VARIABLES#######################################
LINEPOINTS_FILE = "lines.vplotter"
#END VARIABLES####################################


def parse(openfile):
    line_file = open(LINEPOINTS_FILE, "wt")
    token1 = openfile.readline().strip("\n")
    token2 = openfile.readline().strip("\n")
    line_file.write("M"+ " " + token1 +" " + token2 + "\n")
    while(token1 and token2):
        line_file.write("L"+ " " + token1 +" " + token2 + "\n")
        token1 = openfile.readline().strip("\n")
        token2 = openfile.readline().strip("\n")
    return

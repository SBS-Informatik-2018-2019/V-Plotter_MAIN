#-*- coding: utf-8 -*-

#VARIABLES#######################################

LINEPOINTS_FILE = "lines.vplotter"
#END VARIABLES####################################

def parse(tokenfile):
    token = getNextToken(tokenfile)
    #verarbeiten(token)
    return








def getNextToken(tokenfile):
    token = tokenfile.readline().strip("\n")
    if(token):
        return token
    else:
        return ""
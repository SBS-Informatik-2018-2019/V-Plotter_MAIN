#-*- coding: utf-8 -*-

#VARIABLES#######################################
LINEPOINTS_FILE = "lines.vplotter"
#END VARIABLES####################################

def parse(tokenfile):
    token = getNextToken(tokenfile)
    #verarbeiten(token)
    return






def getNextFloat(tokenfile):
    token = getNextToken(tokenfile)
    if(token.isnumeric()):
        return float(token)
    else:
        return "NULL"

def getNextToken(tokenfile):
    token = tokenfile.readline().strip("\n").strip()
    if(token):
        return token
    else:
        return "NULL"
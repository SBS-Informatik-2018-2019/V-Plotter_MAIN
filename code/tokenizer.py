#-*- coding: utf-8 -*-

#VARIABLES#######################################
COMMANDS_PATH = set('MmZzLlHhVvCcSsQqTtAa')
TOKEN_FILE = "tokens.vplotter"
#END VARIABLES####################################

def tokenize_path(pathdef):
    tokens = tokenize_path_replace(pathdef)
    file = open(TOKEN_FILE, "wt")
    file.write("is_path!\n")
    file.close()
    file = open(TOKEN_FILE, "at")
    for token in tokens:
        token = str(token)
        token = token.upper()
        file.write(token + "\n")
    file.close()
    return

def tokenize_path_replace(pathdef):
    pathdef = pathdef.replace('e-', 'NEGEXP').replace('E-', 'NEGEXP')
    pathdef = pathdef.replace(',', ' ').replace('-', ' -')
    pathdef = pathdef.replace('NEGEXP', 'e-')
    for c in COMMANDS_PATH:
        pathdef = pathdef.replace(c, ' %s ' % c)
    return pathdef.split()



def tokenize_polyline(points):
    tokens = tokenize_polyline_replace(points)
    file = open(TOKEN_FILE, "wt")
    file.write("is_polyline!\n")
    file.close()
    file = open(TOKEN_FILE, "at")
    for token in tokens:
        token = str(token)
        token = token.upper()
        file.write(token + "\n")
    file.close()
    return

def tokenize_polyline_replace(points):
    points = points + " "
    tokens = list()
    while len(points) != 0:
        # separate xpolynext and ypolynext coord from points
        points = points.lstrip()
        index = points.index(',')
        polyNextX = float(points[0:index])
        tokens.append(polyNextX)
        points = points[index+1:len(points)]
        points = points.lstrip()
        index = points.index(' ')
        polyNextY = float(points[0:index])
        tokens.append(polyNextY)
        points = points[index+1:len(points)]
        points = points.lstrip()
        continue
    return tokens



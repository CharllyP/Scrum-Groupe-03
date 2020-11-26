import os
import glob
import re
from os.path import basename, splitext


def parser():
    # Creation du repertoire pour les fichiers .txt
    os.system("rm -r ParsedPapers")
    os.system("mkdir ParsedPapers")
    listePDF=getName()
    for i in listePDF:
        i = i[1:]
        toConvert = i
        converted = "ParsedPapers/" + i + ".txt"
        converted = converted.replace(' ', '\ ')
        command = "pdftotext " + toConvert + " " + converted
        os.system(command)
        fr = open(converted, "r+")
        
        # Name
        parsed = "ParsedPapers/" + i + "Parsed.txt"
        fw = open(parsed, 'w+')
        fw.write(i)
        
        # Title
        titre = fr.readline()
        fw.write(titre)

        # Abstract
        content = fr.read()
        debutAbstract = (content.find("Abstract"))
        finAbstract = (content.find("\n\n", debutAbstract))
        substring = content[debutAbstract:finAbstract]
        fw.write(substring)
        fw.close()

def getName():
    listePDF=[]
    liste = glob.glob("Papers/*.pdf")
    for i in liste:
        l = i.strip("Papers/")
        listePDF.append(l)
    return(listePDF)

def main():
    parser()

main()

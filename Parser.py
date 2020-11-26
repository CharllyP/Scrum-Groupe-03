import os
import glob
import sys


def parser():
    # Creation du repertoire pour les fichiers .txt
    os.system("rm -r ParsedPapers")
    os.system("mkdir ParsedPapers")

    dossierSource = sys.argv[1]
    listePDF = glob.glob(dossierSource+"*.pdf")

    for i in listePDF:
        toConvert = i
        converted = i + ".txt"
        os.system("touch "+ converted)
        command = "pdftotext " + toConvert + " " + converted
        os.system(command)
        fr = open(converted, "r+")
        
        # Nom
        iStripped = i.strip(dossierSource)
        parsed = "ParsedPapers/" + iStripped + "Parsed.txt"
        fw = open(parsed, 'w+')
        fw.write(iStripped+ "\n")
        
        # Titre
        titre = fr.readline()
        fw.write(titre)

        # Abstract
        abstract = fr.read()
        debut = (abstract.find("Abstract"))
        fin = (abstract.find("\n\n", debut))
        substring = abstract[debut:fin]
        fw.write(substring)
        fw.close()

def main():
    parser()

main()

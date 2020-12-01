import os
import glob
import sys


def parser():
    # Creation du repertoire pour les fichiers .txt
    os.system("rm -r ParsedPapers")
    os.system("mkdir ParsedPapers")


    dossierSource = sys.argv[2]
    listePDF = glob.glob(dossierSource+"*.pdf")
    option = sys.argv[1]

    if(option == "-t"):
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

            read = fr.read()

            # Authors
            substring = read.lstrip(titre)
            substring = substring.strip()
            fin = (read.find("Abstract"))
            substring = read[:fin]
            fw.write(substring)


            # Abstract
            debut = (read.find("Abstract"))
            fin = (read.find("\n\n", debut))
            substring = read[debut:fin]
            fw.write(substring)

            # References
            debut = (read.find("References"))
            substring = read[debut:]
            fw.write("\n"+substring)

            fw.close()

    elif(option == "-x"):
        print("xml")
    else:
        print("Option inconnue !")

def main():
    if(len(sys.argv) != 3):
        print("Veuillez suivre cette syntaxe: 'python3 Parser.py -(t ou x) RepertoireSource/")
    else:
        parser()

main()

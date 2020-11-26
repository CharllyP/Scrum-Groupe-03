import os
import glob


def parser():
    # Creation du repertoire pour les fichiers .txt
    os.system("rm -r ParsedPapers")
    os.system("mkdir ParsedPapers")
    listePDF = []
    liste = glob.glob("Papers/*.pdf")

    for j in liste:
        l = j.strip("Papers/")
        listePDF.append(l)

    for i in listePDF:
        i = i[1:]
        toConvert = i
        converted = "ParsedPapers/" + i + ".txt"
        converted = converted.replace(' ', '\ ')
        command = "pdftotext " + toConvert + " " + converted
        os.system(command)
        fr = open(converted, "r+")
        
        # Nom
        parsed = "ParsedPapers/" + i + "Parsed.txt"
        fw = open(parsed, 'w+')
        fw.write(i)
        
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

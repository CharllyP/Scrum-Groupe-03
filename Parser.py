import os
import glob


def parser():
    # Creation du repertoire pour les fichiers .txt
    os.system("rm -r ParsedPapers")
    os.system("mkdir ParsedPapers")

    listePDF = glob.glob("Papers/*.pdf")
    print(listePDF)

    for i in listePDF:
        toConvert = i
        print(i)
        converted = i + ".txt"
        os.system("touch "+ converted)
        command = "pdftotext " + toConvert + " " + converted
        print(command)
        os.system(command)
        fr = open(converted, "r+")
        
        # Nom
        iStripped = i.strip("Papers/")
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

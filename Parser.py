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

    j = 1
    for i in listePDF:
        print(j, end="")
        print(" - "+i)
        j += 1

    print("Entrez le numero du fichier que vous ne voulez pas parser (pour finir les suppressions entrez '0'):")
    k = int(input())
    k -= 1
    while k != -1 :
        listePDF.pop(k)
        j = 0
        for i in listePDF:
            print(j, end="")
            print(" - " + i)
            j += 1
        print("Entrez le numero du fichier que vous ne voulez pas parser (pour finir les suppressions entrez '0'):")
        k = int(input())
        k -= 1

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
            fw.write(iStripped + "\n\n")

            # Titre
            titre = fr.readline()
            fw.write(titre + "\n\n")
            read = fr.read()

            # Authors
            substring = read.lstrip(titre)
            fin = (read.find("Abstract"))
            substring = read[:fin]
            fw.write(substring + "\n\n")

            # Abstract
            debut = (read.find("Abstract"))
            fin = (read.find("\n\n", debut))
            substring = read[debut:fin]
            fw.write(substring + "\n\n")

            # References
            debut = (read.find("References"))
            substring = read[debut:]
            fw.write(substring + "\n\n")

            fw.close()

    elif (option == "-x"):
        for i in listePDF:
            toConvert = i
            converted = i + ".txt"
            os.system("touch " + converted)
            command = "pdftotext " + toConvert + " " + converted
            os.system(command)
            fr = open(converted, "r+")

            # Nom
            iStripped = i.strip(dossierSource)
            parsed = "ParsedPapers/" + iStripped + "Parsed.xml"
            fw = open(parsed, 'w+')
            fw.write("<article>\n<preamble>" + iStripped + "</preamble>\n")

            # Titre
            titre = fr.readline()
            fw.write("<titre>" + titre + "</titre>\n")
            read = fr.read()

            # Authors
            substring = read.lstrip(titre)
            fin = (read.find("Abstract"))
            substring = read[:fin]
            fw.write("<auteur>" + substring + "</auteur>\n")

            # Abstract
            debut = (read.find("Abstract"))
            fin = (read.find("\n\n", debut))
            substring = read[debut:fin]
            fw.write("<abstract>" + substring + "</abstract>\n")

            # References
            debut = (read.find("References"))
            substring = read[debut:]
            fw.write("<biblio>" + substring + "</biblio>\n</article>\n")

            fw.close()

    elif(option == "-xml"):
        for i in listePDF:
            toConvert = i
            converted = i + ".txt"
            os.system("touch "+ converted)
            command = "pdftotext " + toConvert + " " + converted
            os.system(command)
            fr = open(converted, "r+")

            # Nom
            iStripped = i.strip(dossierSource)
            parsed = "ParsedPapers/" + iStripped + "Parsed.xml"
            fw = open(parsed, 'w+')
            fw.write("<article>\n<preamble>"+iStripped+ "</preamble>\n")

            # Titre
            titre = fr.readline()
            fw.write("<titre>"+titre+"</titre>\n")
            read = fr.read()

            # Authors
            substring = read.lstrip(titre)
            fin = (read.find("Abstract"))
            substring = read[:fin]
            fw.write("<auteur>"+substring+"</auteur>\n")

            # Abstract
            debut = (read.find("Abstract"))
            fin = (read.find("\n\n", debut))
            substring = read[debut:fin]
            fw.write("<abstract>"+substring+"</abstract>\n")

            # Introduction
            debut = (read.find("Introduction\n"))
            substring = read[debut:]
            substring = substring.strip("Introduction\n")
            fin = (substring.find("\n\n"))
            substring = substring[:fin]
            substringIntro = "Introduction\n" + substring
            fw.write("<introduction>"+ substringIntro + "</introduction>\n")

            # Corps
            debut = (read.find("Introduction"))
            fin = (read.find("Conclusion"))
            substring = read[debut:fin]
            substring = substring.strip(substringIntro)
            substring = "Corps\n" + substring
            substring = substring.replace("<", "(")
            fw.write("<corps>" + substring + "</corps>\n")

            # Conclusion
            debut = (read.find("Conclusion\n"))
            substring = read[debut:]
            substring = substring.strip("Conclusion\n")
            fin = (substring.find("\n\n"))
            substring = substring[:fin]
            substringCon = "Conclusion\n" + substring
            fw.write("<conclusion>" + substringCon + "</conclusion>\n")

            # Discussion
            debut = (read.find("Conclusion"))
            fin = (read.find("References"))
            substring = read[debut:fin]
            substring = substring.strip(substringCon)
            substring = "Discussion\n" + substring
            fw.write("<discussion>" + substring + "</discussion>\n")

            # References
            debut = (read.find("References"))
            substring = read[debut:]
            fw.write("<biblio>"+substring+"</biblio>\n</article>\n")

            fw.close()
    else:
        print("Option inconnue !")

def main():
    if(len(sys.argv) != 3):
        print("Veuillez suivre cette syntaxe: 'python3 Parser.py -(t, x ou xml) RepertoireSource/")
    else:
        parser()

main()

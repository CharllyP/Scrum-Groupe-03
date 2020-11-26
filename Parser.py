import os
import glob
import re
from os.path import basename, splitext


def parser():
    #Creation du repertoire pour les fichiers .txt
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
        fw.write(listePDF[i])
        
        # Title
        first_lines = f.readline()

        fw.write(first_lines)
        # Abstract
        content = f.read()
        debutAbstract = (content.find("Abstract"))
        finAbstract = (content.find("\n\n", debutAbstract))
        substring = content[debutAbstract:finAbstract]
        fw.write(substring)
        fw.close()


def getTitle(file_to_parse):
    title = ""

    # Creating directory to put .txt files
    os.system('rm -r ParsedPapers')
    os.system('mkdir ParsedPapers')

    # Calculate the .pdf file to convert
    file_to_open = 'Papers/' + file_to_parse + '.pdf'
    file_to_open = file_to_open.replace(' ', '\ ')

    # Calculate the .txt file to read
    file_to_read = 'ParsedPapers/' + file_to_parse + '.txt'
    temp = file_to_read
    file_to_read = file_to_read.replace(' ', '\ ')

    # Converting file
    command = 'pdftotext ' + file_to_open + ' > ' + file_to_read
    os.system(command)

    # Reading .txt file
    f = open(temp, 'r')
    first_lines = f.readline()

    return (first_lines)


def getAbstract():
    f = open('Papers/Papers/Alexandrov.txt', "r+")
    content = f.read()
    debutAbstract = (content.find("Abstract"))
    print(debutAbstract)
    finAbstract = (content.find("\n\n", debutAbstract))
    print(finAbstract)
    substring = content[debutAbstract:finAbstract]
    print(substring)


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

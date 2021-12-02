import sys # pt a citi fisierul si parola

#Date de intrare->le vom citi din terminal, invatam dupa
key=sys.argv[2]
inputFile=open(sys.argv[1],"rb")
outputFile=open(sys.argv[3],"w",encoding="utf-8")

def ParsingFile(file):
    codedText=file.read()

    return codedText
def DecryptText(codedText):
    rez = []
    index = 0
    lenKey= len(key)
    for byte in codedText:
        try:
            rez.append(chr(byte ^ ord(key[index % lenKey])))
            index += 1
        except:
            print(index)

    decodedText = "".join(rez)
    return decodedText
def DisplayText(text,file):
    file.write(text)

#citire cod criptat
codedText=ParsingFile(inputFile)

#decriptare cod
decodedText=DecryptText(codedText)

#afisare mesaj original
DisplayText(decodedText,outputFile)

#inchidere fisier
inputFile.close()
outputFile.close()



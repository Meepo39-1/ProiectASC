import sys # pt a citi fisierul si parola

#Date de intrare->le vom citi din terminal, invatam dupa
key=sys.argv[2]
inputFile=open(sys.argv[1],"rb")
outputFile=open(sys.argv[3],"w")

def ParsingFile(file):
    codedText=file.read()

    return codedText
def DecryptText(codedText):
    rez = []
    index = 0
    lenKey= len(key)
    for byte in codedText:
        rez.append(chr(byte ^ ord(key[index % lenKey])))
        index += 1

    decodedText = "".join(rez)
    return decodedText


def DisplayText(text,file):
    file.write(text)
codedText=ParsingFile(inputFile)
decodedText=DecryptText(codedText)
DisplayText(decodedText,outputFile)

'''


def CryptingText(text,parola):
    lenText = len(text)
    lenParola = len(parola)
    outputText=[]
    for index in range(lenText):
        chrText=text[index]
        chrParola=parola[index % lenParola-1]
        outputText.append(chr(ord(chrText) ^ ord(chrParola)))

    outputText=" ".join(outputText)
    return outputText

def DisplayText(text,file):
    file.write(text.encode())

#citire fisier
inputText=ParsingFile(inputFile)

#criptare text
outputText=CryptingText(inputText,password)

#afisare text criptat
DisplayText(outputText,outputFile)

#inchidere fisiere
inputFile.close()
outputFile.close()
print(password)

'''
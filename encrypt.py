import sys # pt a citi fisierul si parola

#Date de intrare
key=sys.argv[1]
inputFile=open(sys.argv[2],"r")
outputFile=open(sys.argv[3],"wb")

def ParsingFile(file):
    text=file.read()

    return text

def CryptingText(text,parola):
  #  print(text)
    lenText = len(text)
    lenKey = len(key)
    outputText=[]
    for index in range(lenText):
        chrText=text[index]
        chrKey=parola[index % lenKey]

        outputText.append(chr(ord(chrText) ^ ord(chrKey)))
        # print(f'{chrText} XOR {chrParola} ={chr(ord(chrText) ^ ord(chrParola))}, original={chr(ord(chrParola)^ ord(chrText) ^ ord(chrParola))}')

    outputText="".join(outputText)
    return outputText

def DisplayText(text,file):
    file.write(text.encode("utf-8"))

#citire fisier
inputText=ParsingFile(inputFile)

#criptare text
outputText=CryptingText(inputText,key)

#afisare text criptat
DisplayText(outputText,outputFile)

#inchidere fisiere
inputFile.close()
outputFile.close()



import sys # pt a citi fisierul si parola

#Date de intrare->le vom citi din terminal, invatam dupa
password=sys.argv[1]
inputFile=open(sys.argv[2],"r")
outputFile=open(sys.argv[3],"wb")

def ParsingFile(file):
    text=file.read()

    return text

def CryptingText(text,parola):
  #  print(text)
    lenText = len(text)
    lenParola = len(parola)
    outputText=[]
    for index in range(lenText):
        chrText=text[index]
        chrParola=parola[index % lenParola]

        outputText.append(chr(ord(chrText) ^ ord(chrParola)))
        # print(f'{chrText} XOR {chrParola} ={chr(ord(chrText) ^ ord(chrParola))}, original={chr(ord(chrParola)^ ord(chrText) ^ ord(chrParola))}')

    outputText="".join(outputText)
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
# print(password)


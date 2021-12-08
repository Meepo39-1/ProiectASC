import sys

#key=sys.argv[1]
f=open("input.txt",'r')
f2=open("output",'rb')
g=open("output2", 'w')

text=f.read()
biti=f2.read()

key = []
for i in range(19):
    index=32
    while index<=127:
        rez = ord(text[i]) ^ index
        if rez == biti[i]:
            print(chr(index))
            key.append(chr(index))
            printed = True
        index +=1
    print(printed,i)
key="".join(key)
print(key)

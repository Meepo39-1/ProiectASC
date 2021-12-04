# ProiectASC
Membrii:  
Nadu Toma    
Marin Florin Eduard Marian  
Furdui Vlad Rares  

Parola echipei adverse: 2PisicipeOita  
Metoda: brute-forcing 
Stim ca lungimea parolei este intre 10 si 15, iar caracterele pot fi litere sau cifre. De asemenea, stim ca fiecare caracter are o reprezentare unica in baza 2. Astfel,aplicam urmatorul algoritm:
Pentru fiecare caracter din primele 30 caractere din fisierul input.txt:
    incearca operatia xor cu fiecare litera/cifra din tabelul ascii
    retine rezultatul si compara-l cu byte-ul de pe pozitia corespunzatoare din fisierul output
    daca cei 2 bytes sunt egali, retine rezultatul

Dupa efectuarea algoritmului, verificam de la al catelea caracter parola se repeta si testam scriptul decrypt.py cu datele din fisierele echipei adverse

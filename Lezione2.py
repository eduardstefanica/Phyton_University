#Si scriva un programma che conti e stampi quante volte compare il carattere   (spazio) all'interno di una stringa legata alla variabile a. Il programma deve far uso soltanto dei costrutti Python fin qua studiati. Suggerimento: potrebbe essere utile un ciclo while che conta il numero di spazi consecutivi a partire da una posizione e che sia 'annidato' nel ciclo principale che scorre i caratteri della stringa.

#in phyton le funzioni si scrivono con la lettera minuscola altrimenti
#non funziona
'''
a='programmazione dei calcolatori' #variabile iniziale
spaces = 0
i=34

#calcolare il nr di spazi in 'a' a partire dalla posizione 'i'
#serve contatore

 while i < len(a) :
    spaces_from_i=0
    #j=1
    
    while i+spaces_from_i <len(a) and a[i+spaces_from_i] == ' ':
        spaces_from_i +=1
        #j+=1 risparmio di una variabile
        
    spaces+= spaces_from_i
    i+= spaces_from_i+1 #+= significa attribuire/sommare 

print(spaces) '''

'----------------------------------------------------------------'
#Modificare il codice precedente facendo in modo che il programma conti il numero di vocali minuscole all'interno della stringa. Risolvere il problema usando l'operatore in di seguito descritto
'''
a='programmazione dei calcolatori' #variabile iniziale
vocali = 0
i=0

while i < len(a) :
    vocali_da_i=0
    #j=1
    
    while i+vocali_da_i <len(a) and a[i+vocali_da_i] == 'aeiou':
        vocali_da_i +=1
       
    vocali+= vocali_da_i
    i+= vocali_da_i+1 #+= significa attribuire/sommare 

print(vocali)
'''
'---------------------------------------------------------------'
'''
#stessa cosa fatta con ciclo if
a='programmazione dei calcolatori' #variabile iniziale
vocali = 0
i=0

while i < len(a) :
    if a[i] in 'aeiou':
        vocali +=1
    i +=1
    
print(vocali)
'''
#-----------------------
a='ciao mi chiamo Eduard'
vocali=0 

for x in a: 
    if x in 'aeiou' :  #x è la variabile delle vocali
        vocali +=1

print(vocali)

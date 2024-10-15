
'''
print ( ord('a'), ord('b'))
print ( ord('A'), ord('B'))
print ( ord('0'), ord('1'))

print (chr(100))
'''

# In[]
#ord() è una funzione integrata che restituisce il valore numerico corrispondente al carattere passato come argomento, secondo la codifica Unicode.
#chr(), che converte un codice Unicode in un carattere.
'''
#da maiuscolo a minuscolo
c='D'

if c>= 'A' and c<='Z' : #c è maiuscolo
    delta=ord(c)-ord('A') 
    #ord('a')+delta
    c_min= chr(ord('a')+delta)
    print (c_min)
    '''
# In[radice quadrata]
#funzione che restituisce la radice quadrata di sqrt(numero scelto)
'''
x=144
def sqrt(x):
    g=x/2 
    c=0                    #variabili locali
    eps=0.00000000001
    c_max=1000

    while abs(g-x/g) > eps and c<c_max:
        c=c+1
        g=(g+x/g)/2
        
    print(g)
    #return g #senza il rsultato è null

ris=sqrt(144)
'''
# In[rad. quadrata con scelta parametri utente]
#valori della radice assegnati "dall'utente" tramite i valori assegnati nella variabile sqrt
'''
x=144
def sqrt(x, eps, c_max):
    g=x/2 
    c=0                    #variabili locali

    while abs(g-x/g) > eps and c<c_max:
        c=c+1
        g=(g+x/g)/2

    return g #senza il rsultato è null

ris=sqrt(144, 0.00000000001, 1000)
print(ris)
'''

# In[Problema]
# fare una stringa palindroma, che si legga uguale anche al contrario (es NATAN)
#booleani per restituire true quando fosse vero e falso quando è false

#algoritmo che confronta la prima lettera con l'ultima, la seconda con n-1 ecc.
#se già non sono uguali allora compaia false

'''
def palindromo(a): #funzione

    n=len(a)    #è una funzione built-in che restituisce la lunghezza (length) di un oggetto
    i=0
    
    while i<n/2 and a[i] == a[n-1-i]:
        i+=1
    
    if a[i] != a[n-1-i]:
        #print('Parola non palindroma')
    #else:
        #print('Parola palindroma')
        return False
    else:
        return True
    
risultato=(palindromo('012natan210'))
print ('la parola è palindroma?')
print((risultato))
'''
# In[]

a='0123456789'

print(a[-1]) #numero  posizioni -1
print(a[-3])

print(a[1:7]) #slicing
print(a[:7]) #prime sette posizioni
print(a[1:]) #tutte le posizioni dalla 1 in poi
print(a[:]) #tutte le posizioni
print(a[1:7:2]) 












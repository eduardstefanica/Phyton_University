# In[]
'''
a= 'Eduardo'
#a[o] = 'E' non funziona perchè le strighe sono immutabili

a= 'E' + a[1:]
print (a)
'''

# In[Liste Phyton]
'''
a=[ 0, 'string', (1,2)]
#len, indicizzazione, slicing, concatenazione, iteraione, ripetizione, spacchettamento sono ammesse

print(a, len(a))

a[0]= '169' #assegno alla prima posizione un altro valore

print(a, len(a))

del(a[1]) #cancella il secondo elemento di a

print(a, len(a))
'''

# In[]
'''
a=[]
# append è la funzione che assegna i valori alla lista/array a
a.append(100) 
a.append(250)

print(a, len(a))

a=a.append(0) #ATTENZIONE, append ritorna none

print(a)
'''
# In[]


# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 09:14:29 2024

@author: gianluca
"""

# In[]

a = 'programmazione'

# a[0] = 'P'# le stringhe sono immutabili

a = 'P' + a[1:]

print(a)

# In[TUPLE]

a, b, c = 10, 12, 13

t = 10, 11, 12

print(t)

print(type(t))

t = ( 0, 'stringa', (1,2,3), 3.14 )
print(t)

print( len(t) )
print(t[2])
print(t[::-1])
print(2*t)
print(t+(1,2))

for x in t:
    print(x)
    
# immutabile come le stringhe
#t[1] = 0 no

t = ('a', 'b', 'c')

x, y, z = t # spacchettamento (unpacking)

print(y)

t = x, y, z # impacchettamento (packing)


a, b = 1, 2

t = (a, b)

a = 10

print(t)


# In[]

a = [ ('A', 2,7), ('B',3, -1), ('C', 0, 1), ('D', -2,-2) ]
r = 2.9

# n = len(a)

# creare una lista che contiene i nomi dei punti in a a distanza al 
# più r da (O, 0,0)

b = []

for nome, x, y in a:
    if x**2+y**2 <= r**2:
        b.append(nome) # tempo costante "in media" O(1)
    
print(b)

# complessità temporale



    










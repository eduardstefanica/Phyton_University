# In[]
'''
a= 'Eduardo'
#a[o] = 'E' non funziona perchè le strighe sono immutabili

a= 'E' + a[1:]
print (a)
'''
# In[]


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

a=[]
# append è la funzione che assegna i valori alla lista/array a
a.append(100) 
a.append(250)

print(a, len(a))

a=a.append(0) #ATTENZIONE, append ritorna none

print(a)

# In[]






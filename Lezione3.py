#Esercizio 3

# 1) stammpa a, e sotolineare con * le vocali e con # le cifre decimali 
# 2) sottolineare e scrivere una stringa in output sotto la stringa iniziale

a='ci40 mi ch1amo Edu4rd'
b =''

for x in a:
    if x in 'aeiouAEIOU':
        b+= '*'
    elif x >='0' and x <='9' :
        b += '#'
    else:
        b+=' '
        
print('la stringa inizializzata:')
print(a)
print(b)


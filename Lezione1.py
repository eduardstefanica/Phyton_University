#In[]
'''
x=2
g,c= x/2, 0 #assegnamento multiplo
eps, c_max= 0.00000000000001, 1000
while abs ( g -x / g) > eps and c < c_max :
    c=c+1
    g=(g+x/2)/2
    
print (g, c) #stampa degli output
'''
#------------------------------------------------
#In[]
# pezzo di codice che in ingresso ti da la possibilità di scrivere il nome della variabile a e rida la possibilità di riscriverla se la stringa in input fosse sbagliata

a="Eduard"
c=0

while a != input ("scrivi Eduard: "):
    c=c+1
    
#------------------------------------------------






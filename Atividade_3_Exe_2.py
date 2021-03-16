numero = 1
ListaPositiva=[]
ListaNegativa=[]
while numero != 0:
    
    numero = int(input())

    if(numero != 0):
        if numero > 0:
            ListaPositiva.append(str(numero))
        else:
            ListaNegativa.append(str(numero))


print(ListaNegativa)
print(ListaPositiva)



numero = 0
Digitado =[]
ListaPar=[]
ListaImpar=[]
for x in range(20):
    
    numero = int(input())
    Digitado.append(int(numero))
    divisao = numero % 2
    if divisao > 0:
            ListaImpar.append(numero)
    else:
            ListaPar.append(numero)


print(*Digitado)
print(*ListaImpar)
print(*ListaPar)

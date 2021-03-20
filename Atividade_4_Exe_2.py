#Faça um programa que cria uma matriz, A, 5 x 5 com números inteiros em sequência e, então, exiba a matriz transposta de A ( At  ). 

#Determinar a transposta de uma matriz é reescrevê-la de forma que suas linhas e colunas troquem de posições ordenadamente, isto é, a primeira linha é reescrita como a primeira coluna, a segunda linha é reescrita como a segunda coluna e assim por diante, até que se termine de reescrever todas as linhas na forma de coluna.

A = []
At =[]
n = 1
i = 1
for _ in range(5):
    An = []
    An1 = []
    for _ in range(5):
        An.append(n)
        n = n + 1
    A.append(An)
n = 1
for linha in range(len(A)):
    An1 = []
    An1.append(i)
    n = i + 5
    for _ in range(4):
        An1.append(n)
        n = n + 5
    i = i + 1
    At.append(An1)
print(A)
print(At)
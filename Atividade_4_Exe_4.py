#Crie um programa que realize a soma de todos os elementos da diagonal principal de uma matriz 4 x 4, 5 x 5, etc, preenchida com números de 1 até o tamanho da matriz.

N = int(input("Digite o tamanho da matriz: "))
M =[]
n = 1
val = 0

for _ in range(N):
    linha=[]
    for _ in range(N):
        linha.append(n)
        n = n + 1
    M.append(linha)

for lin in range(N):
    val += M[lin][lin]

print(M)
print(val)
#Faça um programa que multiplica duas matrizes de tamanho 3 x 3, sendo que a primeira matriz tem valores de 1 a 9, e a segunda deverá ser digitada pelo usuário.
Ma = []
Mb = []
Mx = [[0,0,0],[0,0,0],[0,0,0]]

linha = []
n = 1
i = 1

for _ in range(3):
    linha = []
    for _ in range(3):
        linha.append(n)
        n = n + 1
    Ma.append(linha)
    
for _ in range(3):
    linha = []
    for _ in range(3):
        n = int(input())
        linha.append(n)
    Mb.append(linha)

for i in range(3):
    for lin in range(3):
        for col in range(3):
            Mx[i][lin] +=Ma[i][col]*Mb[col][lin]

print(Ma)
print(Mb)
print(Mx)
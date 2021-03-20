#Faça um programa que crie uma lista contendo listas, onde cada lista contem a sequência de Fibonacci, sempre iniciando em 0.
#O usuário deverá informar a sequência desejada.
#A Sequência de Fibonacci é uma sequência de números inteiros iniciada em 0, na qual cada termos subsequente corresponde à soma dos dois anteriores

N = int(input("Digite a sequência desejada: "))

F = []
linha = []
Nlinha = []

anterior = 0
proximo = 0

for _ in range(N):
    
    linha =[]+ Nlinha
    
    linha.append(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior
    if proximo == 0:
        proximo = proximo + 1

    Nlinha = linha
    F.append(linha)
    
print(F)
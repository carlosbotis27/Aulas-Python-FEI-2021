import statistics

lista = []

TamanhoLista = int(input("Qual o tamanho da lista: "))

Soma = 0

for x in range(TamanhoLista):
        Num = int(input("Digite os valores: "))
        lista.append(Num)

media = statistics.mean(lista)
desvio = statistics.pstdev(lista)
print("Média = %.2f" % media, " e Desvio = %.4f" %desvio)
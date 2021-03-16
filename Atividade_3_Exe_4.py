u=[]
v=[]

ProdutoEscalar = 0

print("Digite o vetor 1:")
for x in range(3):
    u.append(int(input()))
    
print("Digite o vetor 2:")
for x in range(3):
    v.append(int(input()))

for x in range(3):
    ProdutoEscalar = ProdutoEscalar + u[x]*v[x]
    
print(ProdutoEscalar)


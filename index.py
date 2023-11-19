entrada = open("G1.txt", "r")

linha = entrada.readlines()
grafoDeEntrada = linha[0].split()

listaDeVertices = []
relacionamentoDosVertices = {}
vetorD = []
vetorF = []

numeroVertices = int(grafoDeEntrada[0])
numeroArestas = int(grafoDeEntrada[1])
nomeDoGrafo = grafoDeEntrada[2]

for i in range(1, len(linha)):
    vetorDaLinha = linha[i].split()

    if (linha[i][0] not in listaDeVertices):
        relacionamentoDosVertices[linha[i][0]] = []
        listaDeVertices.append(linha[i][0])

    relacionamentoDosVertices[linha[i][0]].append(linha[i][1])

listaDeVertices.sort(key=lambda v: len(relacionamentoDosVertices[v]), reverse=True)
relacionamentoDosVerticesOrdenado = dict(sorted(relacionamentoDosVertices.items()))

print(relacionamentoDosVerticesOrdenado)
print(listaDeVertices)

cor = {}
def DFS(G):
    global mark
    for u in G:
        cor[u] = "BRANCO"
    mark = 0

    for u in G:
        if cor[u] == "BRANCO":
            DFS_VISIT(u)
    
    
def DFS_VISIT(u):
    global mark
    cor[u] = "CINZA"
    mark = mark + 1
    vetorD.append(mark)


    for v in relacionamentoDosVerticesOrdenado[u]:
        if cor[v] == "BRANCO":
            DFS_VISIT(v)
    
    cor[u] = "PRETO"
    mark = mark + 1
    vetorF.append(mark)

DFS(listaDeVertices)

print("vetor d:",  vetorD)
print("vetor f:" , vetorF)


entrada.close()

entrada = open("G1.txt", "r")

linha = entrada.readlines()
grafoDeEntrada = linha[0].split()

cor = {}
listaDeVertices = []
relacionamentoDosVertices = {}

numeroVertices = int(grafoDeEntrada[0])
numeroArestas = int(grafoDeEntrada[1])
nomeDoGrafo = grafoDeEntrada[2]

vetorD = [0]*numeroVertices
vetorF = [0]*numeroVertices

for i in range(1, len(linha)):
    vetorDaLinha = linha[i].split()

    if linha[i][0] not in listaDeVertices:
        relacionamentoDosVertices[linha[i][0]] = []
        listaDeVertices.append(linha[i][0])
    elif linha[i][1] not in listaDeVertices:
        relacionamentoDosVertices[linha[i][1]] = []
        listaDeVertices.append(linha[i][1])

    if linha[i][1] not in relacionamentoDosVertices[linha[i][0]]:
        relacionamentoDosVertices[linha[i][0]].append(linha[i][1])

listaDeVertices.sort()
mapeamentoIndices = {v: i for i, v in enumerate(listaDeVertices)}

listaDeVertices.sort(key=lambda v: len(relacionamentoDosVertices[v]), reverse=True)

relacionamentoDosVerticesOrdenado = dict(sorted(relacionamentoDosVertices.items()))

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
    vetorD[mapeamentoIndices[u]] = mark

    for v in relacionamentoDosVerticesOrdenado[u]:
        if cor[v] == "BRANCO":
            DFS_VISIT(v)
    
    cor[u] = "PRETO"
    mark = mark + 1
    vetorF[mapeamentoIndices[u]] = mark

DFS(listaDeVertices)

print("vetor d:",  vetorD)
print("vetor f:" , vetorF)

entrada.close()

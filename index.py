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

print(numeroVertices)
print(numeroArestas)
print(nomeDoGrafo+"\n")

for i in range(1, len(linha)):
    vetorDaLinha = linha[i].split()

    if (linha[i][0] not in listaDeVertices):
        relacionamentoDosVertices[linha[i][0]] = []
        listaDeVertices.append(linha[i][0])

    relacionamentoDosVertices[linha[i][0]].append(linha[i][1])

relacionamentoDosVerticesOrdenado = dict(sorted(relacionamentoDosVertices.items()))
print(relacionamentoDosVerticesOrdenado)

entrada.close()

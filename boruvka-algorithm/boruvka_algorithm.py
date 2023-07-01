# Este codigo teve como referencia a pagina web GeeksforGeeks sobre o algoritmo de Boruvka
# URL: https://www.geeksforgeeks.org/boruvkas-algorithm-greedy-algo-9/
# Este codigo teve a contribuicao de Neelam Yadav

# Algoritmo de Boruvka para encontrar a arvore geradora minima de um grafo conexo e ponderado

# Code edited by Marco da Costa, António Canto and Carlos Monteiro
# Este codigo foi editado e adaptado por Marco da Costa, António Canto and Carlos Monteiro
# Análise e Síntese de Algortimos, UniCV 2023

from collections import defaultdict

#Classe para representar um grafo
class Graph:

    # Metodo construtor+
    def __init__(self,vertices):
        # inicializa o grafo ao atribuir um numero de vertices
        self.V = vertices 
        # lista vazia para adicionar as arestas aos seus respetivos vertices 
        # e as guardar # default dictionary to store graph
        self.graph = []

    # funcao para adicionar uma aresta ao grafo
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    # funcao auxiliar para encontrar o conjunto a que um elemento pertence
    # Faz uso da tecnica path compression
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # funcao auxiliar para efetuar a uniao de dois subgrafos/conjuntos
    # Faz uso da tecnica union by rank
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Unir a arvore de rank menor na raiz da arvore de rank maior
        # Attach smaller rank tree under root of high rank tree
        # (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        
        # Se as ranks forem iguais, escolhe-se uma e incrementa-se
        # o rank rank++
        # If ranks are same, then make one as root and increment
        # its rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1

    # Funcao principal para construir a AGM fazendo uso do algoritmo de Kruskal
    def boruvkaMST(self):
        parent = []; rank = [];

        # arrays que guardam os vertices e os pesos das arestas da AGM
        uMST = []; vMST = []; wMST = [];

        # Um array para guardar o indice da aresta de menor custo do subgrafo
        # Guarda o vertice, a aresta e o peso para cada componente
        # Guarda [u,v,w] para cada componente
        cheapest =[]


        # Inicialmente tem-se V arvores diferentes
        # No final ter-se-a apenas uma arvore que sera a AMG
        numTrees = self.V
        MSTweight = 0

        # Cria-se V subgrafos com apenas 1 elemento
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
            cheapest =[-1] * self.V


        # Junta-se todos os componentes ate que todos estiverem combinados numa AGM
        while numTrees > 1:

            # Itera-se sobre todos as arestas e atualiza-se a aresta de custo minimo
            # para todos os componentes
            for i in range(len(self.graph)):

                # Find components (or sets) of two corners
                # of current edge
                u,v,w = self.graph[i]
                set1 = self.find(parent, u)
                set2 = self.find(parent ,v)

                # Se as duas pontas da aresta atual pertencerem 
                # ao mesmo conjunto, ignora-se a aresta atual
                # Caso contrario, verifica-se se a aresta atual 
                # é mais proxima das arestas anteriores 
                # de menor custo do conjunto 1 e conjunto 2

                if set1 != set2:

                    if cheapest[set1] == -1 or cheapest[set1][2] > w :
                        cheapest[set1] = [u,v,w]

                    if cheapest[set2] == -1 or cheapest[set2][2] > w :
                        cheapest[set2] = [u,v,w]


            # Considera-se as arestas de menor custo escolhidos acima
            # e adiciona-as na AGM 
            for node in range(self.V):
                
                # Verifica-se se o menor custo para o elemento existe
                if cheapest[node] != -1:
                    u,v,w = cheapest[node]
                    set1 = self.find(parent, u)
                    set2 = self.find(parent ,v)

                    if set1 != set2 :
                        MSTweight += w
                        self.union(parent, rank, set1, set2)
                        uMST.append(u)
                        vMST.append(v)
                        wMST.append(w)
                        print ("Aresta %d-%d com peso %d incluido na AGM" % (u,v,w))
                        numTrees = numTrees - 1

            # zera-se o array de menor custo
            # reset cheapest array
            cheapest =[-1] * self.V


        print ("O peso da AGM é %d" % MSTweight)
        return uMST, vMST, wMST

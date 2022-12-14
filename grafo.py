from functools import reduce
from math import floor
############################################ Aula 01 ############################################
# 1
class Graph():
    """Construa uma classe Digrafo para representar o grafo orientado utilizando a matriz de adjacência."""
    def __init__(self, v : int = 0, e = None, direcionado = False, usaMatriz = False):
        self.v = v
        self.le = e
        self.direcionado = direcionado
        self.usaMatriz = usaMatriz
        self.cria_lista_adjacencia()

    def cria_lista_adjacencia(self):
        if not self.usaMatriz:
            self.e = [[] for _ in range(self.v)]
        else:
            self.e = [[0 for _ in range(self.v)] for _ in range(self.v)]

        
        if self.le != None:
                for u,w in self.le:
                    self.insere(u,w)


    def insere(self, u, w):

        if not self.usaMatriz:
            self.e[u].append(w)
            if not self.direcionado:
                self.e[w].append(u)
        else:
            self.e[u][w] = 1
            if not self.direcionado:
                self.e[w][u] = 1

    def remov(self, u, w):
        if not self.usaMatriz:
            self.e[u][w] = 0
            if not self.direcionado:
                self.e[w][u] = 0
        else:
            self.e[u].remove(w)
            if not self.direcionado:
                self.e[w].remove(u)

    def mostra(self):
        print(f"V =  {self.v}")
        if self.usaMatriz:
            print(f"E = \n")
            for i in self.e:
                print(i)
        else:
            for i,v in enumerate(self.e):
                print(f"{i} -> {v}")

    ### 3 
#     Escreva um método grau entrada() que calcula o grau de
# entrada de um vértice v de um digrafo. Escreva também a função
# grau saida() que calcula o grau de saída de v no digrafo. As
# funções devem ser implementadas na classe Digrafo que utiliza
# uma matriz de adjacência.
    def grau_entrada(self, v):
        """Escreva um método grau entrada() que calcula o grau de
# entrada de um vértice v de um digrafo."""
        gr = 0
        if self.usaMatriz:
            for i in range(self.v):
                gr += self.e[i][v]
        else:
            for i in range(self.v):
                gr += 1 if (v in self.e[i]) else 0

        return gr
            
    
    def grau_saida(self, v):
        """Escreva também a função
# grau saida() que calcula o grau de saída de v no digrafo."""
        if self.usaMatriz:
            return reduce(lambda a, b: a + b, self.e[v])
        else:
            return len(self.e[v])
    ### fim 3

    ### 4
    def compara_grafos(g, h):
        """Escreva uma função que decida se dois grafos são iguais.
A função deve ser implementada para classe Grafo que utiliza
matriz e listas de adjacência."""
        if g.v != h.v: return False

        if g.usaMatriz == True and h.usaMatriz == True:
            return _compara_matriz(g, h)
        elif g.usaMatriz == False and h.usaMatriz == False:
            return _compara_lista(g, h)
        else: 
            if g.usaMatriz == True and h.usaMatriz == False:
                j = Graph(h.v)
                j.e = h.e.copy()
                j.direcionado = h.direcionado
                j.usaMatriz = h.usaMatriz

                j = lista_para_matriz(j)
                return _compara_matriz(g, j)
            else:
                j = Graph(g.v)
                j.e = g.e.copy()
                j.direcionado = g.direcionado
                j.usaMatriz = g.usaMatriz


                j = lista_para_matriz(j)
                return _compara_matriz(j, h)
    ### fim 4

    ### 6
    def inverte_lista_adjacencia(self, u):
        """ Escreva uma função que recebe um digrafo armazenado em
        listas de adjacência e inverta as listas de todos os vértices do
        grafo."""
        if self.usaMatriz: print("Não usa lista de adjacencia"); return

        return list(reversed(self.e[u]))
    ### fim 6

### 5
def lista_para_matriz(g):
    """Escreva uma função que converta uma representação de grafo
em outra, por exemplo, converta um grafo armazenado em uma
matriz de adjacência em uma lista de adjacência."""
    matriz = [[ 0 for _ in range(g.v)] for _ in range(g.v)]

    for i in range(g.v):
        for j in g.e[i]:
            matriz[i][j-1] = 1

    g.e = matriz.copy()
    g.usaMatriz = True
    return g

def matriz_para_lista(g):
    """Escreva uma função que converta uma representação de grafo
em outra, por exemplo, converta um grafo armazenado em uma
matriz de adjacência em uma lista de adjacência."""
    lista = [[] for _ in range(g.v)]

    for i in range(g.v):
        for j in range(g.v):
            if g.e[i][j]:
                lista[i].append(j+1)
            
    g.e = lista.copy()
    g.usaMatriz = False
    return g
### fim 5

### 7
def le_arquivo_grafo_direcionado(filename):
    """
    Um grafo pode ser armazenado em um arquivo com o seguinte
    formato:

    Onde na primeira linha contém um inteiro V (vértice), na segunda contém um inteiro A (arestas) e nas demais linha contém
    dois inteiros pertencentes ao intervalo 0 . . V − 1. Se interpretarmos cada linha do arquivo como uma aresta, podemos dizer que
    o arquivo define um grafo com vértices 0 . . V − 1. Escreva uma
    função que receba um nome de arquivo com o formato acima e
    construa uma representação (matriz e listas de adjacência) do
    grafo.

    """
    f = open(filename, "r")
    v = int(f.readline())
    n_e = int(f.readline())
    e = []
    for _ in range(n_e):
        u_v = f.readline()
        u_v = u_v.split()
        e.append((int(u_v[0]), int(u_v[1])))

    f.close()

    return Graph(v=v, e = e, direcionado = True, usaMatriz = False)
### fim 7

### 8
def eh_fonte(g: Graph, v):
    """
    Escreva uma função que receba um dígrafo e um vértice
    como parâmetro e retorne 1 se vértice for uma fonte (grau de
    saída maior que zero e grau de entrada igual a 0), ou 0 caso
    contrário. A função deve ser implementada para a classe Grafo
    que utilizam matriz e listas de adjacência.
    """
    if not g.direcionado: return 0

    saida, entrada = 0, 0

    if g.usaMatriz:
        saida = reduce(lambda a,b: a + b, g.e[v])
        entrada = reduce(lambda a,b: a + b, [g.e[i][v] for i in range(g.v)])
    else:
        saida = len(g.e[v])
        entrada = reduce(lambda a,b: a + b, [1 if v in g.e[i] else 0 for i in range(g.v)])

    if saida > 0 and entrada == 0:
        return 1
    else:
        return 0
### fim 8

### 9
def eh_sorvedouro(g: Graph, v):
    """ Escreva uma função que receba um dígrafo e um vértice
    como parâmetro, retorne 1 se vértice for uma sorvedouro (grau
    de entrada maior que zero e grau de saída igual a 0), ou 0 caso
    contrário. A função deve ser implementada para a classe Grafo
    que utiliza matriz e listas de adjacência
    """
    if not g.direcionado: return 0

    saida, entrada = 0, 0

    if g.usaMatriz:
        saida = reduce(lambda a,b: a + b, g.e[v])
        entrada = reduce(lambda a,b: a + b, [g.e[i][v] for i in range(g.v)])
    else:
        saida = len(g.e[v])
        entrada = reduce(lambda a,b: a + b, [1 if v in g.e[i] else 0 for i in range(g.v)])

    if saida == 0 and entrada > 0:
        return 1
    else:
        return 0
### fim 9

### 10

def eh_simetrico(g: Graph):
    """
    Escreva uma função que retorna 1 se o dígrafo for simétrico
    e 0 caso contrário. Um dígrafo é simétrico se cada uma das
    arestas é anti-paralela a outra. A função deve ser implementada
    para classe Grafo que utilizam matriz e listas de adjacência.

    Exemplo: o grafo G = (V, E), com V = {1, 2, 3} e arestas E =
    {(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2), } é um dígrafo simétrico.
    """
    if not g.direcionado: return 1

    if g.usaMatriz:
        for i in range(g.v):
            for j in range(g.v - i):
                if g.e[i][i+j] != g.e[i+j][i]: return 0
        return 1
    else:
        for i in range(g.v):
            for j in g.e[i]:
                if not (i in g.e[j] and j in g.e[i]): return 0
        return 1
### fim 10

def _compara_matriz(g, h):
    for i in range(g.v):
        for j in range(g.v):
            if g.e[i][j] != h.e[i][j]:
                return False
    return True

def _compara_lista(g ,h):
    for i in range(g.v):
        if len(g.e[i]) != len(h.e[i]):
            return False
        for j in range(len(g.e[i])):
            if g.e[i][j] != h.e[i][j]:
                return False
    return True

def remove_no(g, v):
    if g.usaMatriz:
        for i in range(g.v):
            g.e[i][v] = 0
            g.e[v][i] = 0
    else:
        g.e[v] = []
        for i in range(g.v):
            if i in g.e[i]:
                g.e[i].remove(v)


############################################ Aula 02 #######################################################
### 1
def tem_caminho(g: Graph, cam: list[int]):
    """Escreva uma função que verifique se uma dada sequência
    seq[0..k] de vértices de um grafo é um caminho. A função
    devolve 1 caso a sequencia seja um caminho e 0 caso contrário.
    Faça duas versões do método:supõe que o grafo dado por sua
    matriz de adjacência e outra supõe que o grafo é dado por listas
    de adjacência."""
    if g.usaMatriz:
        for i in range(0, len(cam)-1):
            if not g.e[cam[i]][cam[i+1]]: return 0
        return 1
    else:
        for i in range(0, len(cam)-1):
            if not cam[i+1] in g.e[cam[i]]: return 0
        return 1
### fim 1

### 2
def tem_caminho_simples(g:Graph, cam: list[int]):
    """Escreva uma função que verifique se uma dada sequência
    seq[0..k] de vértices de um grafo é um caminho simples. A
    função devolve 1 caso a sequencia seja um caminho e 0 caso
    contrário. Faça duas versões do método:supõe que o grafo dado
    por sua matriz de adjacência e outra supõe que o grafo é dado
    por listas de adjacência.
    """
    res = tem_caminho(g, cam) and (len(set(cam)) == len(cam))
    return 1 if res else 0
### fim 2


### 3
def caminho(g: Graph, s: int, t: int):
    """Dados vértices s e t de um grafo G, escreva uma função que
    retorna 1 se existe um caminho ou 0 se não existe um caminho
    de s a t em G. Faça duas versões: uma supõe que o grafo é
    dado por sua matriz de adjacência e outra supõe que o grafo
    é dado por listas de adjacência.
    """
    if s == t: return 1

    if g.usaMatriz:
        for j in range(g.v):
            if g.e[s][j] == 1:
                if s == j: continue
                else: 
                    if caminho(g, j, t): return 1
    else:
        for j in g.e[s]:
            if caminho(g, j, t): return 1
    # return False
### fim 3


### 4
def mostra_caminho(g: Graph, s: int, t: int) -> int:
    """Dados vértices s e t de um grafo G, escreva uma função que
    encontra e exibe (caso exista) um caminho de s a t. Faça duas
    versões da função: uma supõe que o grafo é dado por sua matriz
    de adjacência e outra supõe que o grafo é dado por listas de
    adjacência.
    """
    if s == t: print(s); return 1

    if g.usaMatriz:
        print(s)
        for j in range(g.v):
            if g.e[s][j] == 1:
                if s == j: continue
                else: 
                    if mostra_caminho(g, j, t): return 1
    else:
        print(s)
        for j in g.e[s]:
            if mostra_caminho(g, j, t): return 1
    # return False
### fim 4

### 5
def dfs_iterativo(g: Graph):
    """
    Escreva uma versão iterativa para a busca em profundidade
    para grafos representados por uma matriz de adjacência e por
    uma listas de adjacência. Dica utilize uma pilha como estrutura
    auxiliar
    """
    visitado = [0 for _ in range(g.v)]
    stack = []

    if g.usaMatriz:
        for u in range(g.v):
            if not visitado[u]:
                print(u)
                stack.append(u)
                visitado[u] = 1
                while len(stack) > 0:
                    v = stack.pop()
                    for z, w in enumerate(g.e[v]):
                        if w == 1:
                            if not visitado[z]:
                                print(z)
                                visitado[z] = 1
                                stack.append(z)
    else:
        for u in range(g.v):
            if not visitado[u]:
                print(u)
                stack.append(u)
                visitado[u] = 1
                while len(stack) > 0:
                    v = stack.pop()
                    for w in g.e[v]:
                        if not visitado[w]:
                            print(w)
                            visitado[w] = 1
                            stack.append(w)

### fim 5

### Exercicio
"""
Escreva um método receba dois vértices v e w em V (G), e verifique se existe um arco v − w em G. Caso positivo devolva
a classificação do arco (arborescência, descendente, retorno ou
cruzado).
"""
 
def dfs_visita_tipo_arco(g, u, visitados, tempo, d, f, pai):
    visitados[u] = True

    tempo += 1
    d[u] = tempo

    for w in g.e[u]:
        if not visitados[w]:
            pai[w] = u
            tempo = dfs_visita_tipo_arco(g, w, visitados, tempo, d, f, pai)    

    tempo += 1
    f[u] = tempo
    return tempo

def dfs_tipo_arco(g: Graph, v: int, w: int):

    if not caminho(g, v, w): return "Não tem caminho entre os vertices"

    
    visitado = [False for _ in range(g.v)]
    d = [-1 for _ in range(g.v)]
    f = [-1 for _ in range(g.v)]
    pai = [-1 for _ in range(g.v)]

    tempo = 0

    for u in range(g.v):
        if not visitado[u]:
            pai[u] = u
            dfs_visita_tipo_arco(g, u, visitado, tempo, d, f, pai)

    if d[v] < d[w] < f[w] < f[v] and pai[w] == v:
        return "Arborecência"
    elif d[v] < d[w] < f[w] and pai[w] != v:
        return "Descendente"
    elif d[w] < d[v] < f[v] < f[w]:
        return "Retorno"
    elif d[w] < f[w] < d[v] < f[v]:
        return "Cruzado"
    else:
        return "Deu ruim"


############################################ Aula 03 #######################################################

def dfs(g):
    visitados = [False for _ in range(g.v)]
    for u in range(len(g.e)):
        if not visitados[u]:
            dfs_visita(g, u, visitados)

def dfs_visita(g, u, visitados):
    visitados[u] = True
    print(u)
    for w in g.e[u]:
        if not visitados[w]:
            dfs_visita(g, w, visitados)

#######
### 1
"""
Escreva um método que verifica se um dado digrafo contém um
ciclo. O método devolve 1 se existe um ciclo e devolve 0 em
caso contrário.
Implemente a detecção do ciclo utilizando a função de caminho.
"""

def tem_ciclo(g):
    for i in range(g.v):
        if ciclo(g, i, i): return True
    
    return False

def ciclo(g, s, e):
    if g.usaMatriz:
        for j in range(g.v):
            if g.e[s][j] == 1:
                if j == e: return True
                if ciclo(g, j, e): return True
    else:
        for j in g.e[s]:
            if j == e: return True
            if ciclo(g, j, e): return True
    return False

### 2
"""
Escreva um método que verifica se um dado digrafo contém um
ciclo. O método devolve 1 se existe um ciclo e devolve 0 em
caso contrário.
Implemente a detecção do ciclo utilizando classificação de arcos
"""

def tem_arco_de_retorno(g, u, tempo, d, f):
    
    d[u] = tempo
    tempo += 1

    for w in g.e[u]:
        if d[w] == -1:
            if tem_arco_de_retorno(g, w, tempo, d, f):
                return 1
        elif f[w] == -1:
            return 1

    f[u] = tempo
    tempo += 1
    return 0

def tem_ciclo_classi_arcos(g: Graph):
    d = [-1 for _ in range(g.v)]
    f = [-1 for _ in range(g.v)]

    tempo = 0

    for u in range(g.v):
        if d[u] == -1:
            if tem_arco_de_retorno(g, u, tempo, d, f):
                return 1

    return 0

### 3
"""
Escreva um método que verifica se um dado digrafo contém um
ciclo. O método devolve 1 se existe um ciclo e devolve 0 em
caso contrário.
Implemente a detecção do ciclo utilizando cores.
"""
BRANCO = "branco"
CINZA = "cinza"
PRETO = "preto"

def tem_arco_de_retorno_cor(g, u, cores):
    
    cores[u] = CINZA

    for w in g.e[u]:
        if cores[w] == CINZA:
            return 1
        if cores[w] == BRANCO:
            if tem_arco_de_retorno_cor(g, w, cores):
                return 1
        
    cores[u] = PRETO
    return 0

def tem_ciclo_cor(g: Graph):
    # d = [-1 for _ in range(g.v)]
    # f = [-1 for _ in range(g.v)]
    cores = [BRANCO for _ in range(g.v)]

    for u in range(g.v):
        if cores[u] == BRANCO:
            if tem_arco_de_retorno_cor(g, u, cores):
                return 1

    return 0






def dfs_visita_tempo(g, u, visitados, tempo, d, f, pai):
    visitados[u] = True

    tempo += 1
    d[u] = tempo

    for w in g.e[u]:
        if not visitados[w]:
            pai[w] = u
            tempo = dfs_visita_tempo(g, w, visitados, tempo, d, f, pai)    

    tempo += 1
    f[u] = tempo
    return tempo

def dfs_tempo(g: Graph):
    # for u in range(g.v):
    #     visitado[u] = 0
    #     d[u] = -1
    #     f[u] = -1
    #     pai[u] = -1

    visitado = [False for _ in range(g.v)]
    d = [-1 for _ in range(g.v)]
    f = [-1 for _ in range(g.v)]
    pai = [-1 for _ in range(g.v)]

    tempo = 0

    for u in range(g.v):
        if not visitado[u]:
            pai[u] = u
            dfs_visita_tempo(g, u, visitado, tempo, d, f, pai)

    return d, f, pai

############################################ Aula 04 #######################################################    

def ordenacao_topologica(g: Graph):
    """
    Implemente o algoritmo de ordenação topológica utilizando busca
    em profundidade.
    """
    h = Graph(g.v,None, g.direcionado, g.usaMatriz)
    h.e = g.e.copy()

    ordem = []
    usado = [0 for _ in range(h.v)]

    while reduce(lambda a, b: a+b, usado, 0) != h.v:
        for i in range(h.v):
            if h.grau_entrada(i) == 0 and not usado[i]:
                ordem.append(i)
                usado[i] = 1
                remove_no(h ,i)
    return ordem

############################################ Aula 05 #######################################################    
### 1 
"""
1. Dado o grafo G = (V, E) a seguir:

"""

def grafo_induzido(g: Graph, v = []):
    """ 
    a) Apresente o subgrafo G1 de G induzido por V = {a, b, c, d, e, f}. 

    e 
    4. Dado um grafo não orientado G = (V, E), escreva um método
    que receba um conjunto de vértices V' ∈ V e devolva um grafo
    induzido por V'. Caso não seja possível gerar o grafo induzido,
    apresente uma mensagem de erro.
    """
    if g.direcionado: exit("PRECISA SER NAO DIRECIONADO")

    for i in v:
        if i not in range(g.v): exit("Vértice não pertence ao grafo")

    qtd_v = g.v - len(v)

    vertices_restantes = list(set([i for i in range(g.v)])- set(v))
    vertices_restantes.sort()

    h = Graph(qtd_v, e= None, direcionado= False, usaMatriz=False)

    for i, vr in enumerate(vertices_restantes):
        h.e[i] = g.e[vr].copy()

        for vretirado in v:
            if vretirado in h.e[i]:
                h.e[i].remove(vretirado)


    return h

def grafo_aresta_induzido(g: Graph, e = []):
    """ 
    b) Apresente o subgrafo G2 de G aresta-induzido por
    E0 = {{a, g}, {b, g}, {c, g}, {d, g}, {e, g}, {f, g}}.
    """
    if g.direcionado: exit("PRECISA SER NAO DIRECIONADO")

    h = Graph(g.v, e= None, direcionado= False, usaMatriz=g.usaMatriz)
    h.e = g.e.copy()

    if g.usaMatriz:
        for u,v in e:
            h.e[u][v] = 0
            h.e[v][u] = 0
    else:
        for u,v in e:
            if v in h.e[u]: h.e[u].remove(v)
            if u in h.e[v]: h.e[v].remove(u)

    return h

### 2 
def eh_subgrafo(g: Graph, h: Graph):
    """ 2. Dado um grafo não orientado G = (V, E), escreva um método
    que receba um grafo G1 = (V, E) e devolva verdadeiro se G1 ⊆ G,
    e falso caso contrário.
    """
    """Checa se h é sub grafo de g"""
    if g.direcionado or h.direcionado: exit("PRECISA SER NAO DIRECIONADO")

    for i in range(h.v):
        for j in h.e[i]: 
            if not j in g.e[i] :
                return False

    return True

### 3
def eh_subgrafo_gerador(g: Graph, h: Graph):
    """
    3. Dado um grafo não orientado G = (V, E), escreva um método
    que receba um grafo G1 = (V, E) e devolva verdadeiro se G1 é
    um subgrafo gerador de G, e falso caso contrário.
    """
    if eh_subgrafo(g, h):
        for i in range(h.v):
            if not i in range(g.v): return False
        return True

    return False

### 5
def componentes(g: Graph):
    """ 5. Dado um grafo não orientado, construa um método que
    devolve o número de componentes de G.
    """
    cc = [-1 for _ in range(g.v)]

    comp = 0

    for v in range(g.v):
        if cc[v] == -1:
            dfs_componentes(g, v, comp, cc)
            comp += 1
    
    return comp

def dfs_componentes(g: Graph, v: int, comp: int, cc: list[int]):
    cc[v] = comp

    for w in g.e[v]:
        if cc[w] == -1:
            dfs_componentes(g, w, comp, cc)
### fim 5

### 6
def eh_conexo(g: Graph):
    """
    6. Dado um grafo não orientado, utilize o método que devolve
    o número de componentes do grafo construído no exercício anterior para construir um outro método que devolva verdadeiro se
    o grafo é conexo e falso caso o grafo seja desconexo.
    """
    return componentes(g) == 1


### 7 
"""
Dado um digrafo D = (V, E), escreva um programa que determine os componentes fortemente conexos utilizando o algoritmo
de Kosaraju
"""
# TODO


############################################ Aula 06 #######################################################    

### 1
def eh_bipartido(g: Graph):
    """
    Escreva um programa que verifique se o grafo é bipartido,
    caso seja bipartido, apresente quais são os vértices que da cor
    azul e quais vértices da cor vermelho.
    """
    visitado = [False for _ in range(g.v)]
    cores = [-1 for _ in range(g.v)]
    cor = 0

    qual_cor = {0:[], 1:[]}

    for u in range(g.v):
        if not visitado[u]:
            dfs_bipartido(g, u, visitado, cor, cores)
    
    bipart = True
    for u in range(g.v):
        qual_cor[cores[u]].append(u)

        for v in g.e[u]:
            if cores[v] == cores[u]: bipart = False
        
    print(f"Azul: {qual_cor[0]}")
    print(f"Vermelho: {qual_cor[1]}")
    return bipart


def dfs_bipartido(g, u, visitados, cor, cores):
    visitados[u] = True
    cores[u] = cor

    for w in g.e[u]:
        if not visitados[w]:
            dfs_bipartido(g, w, visitados, 0 if cor else 1, cores)    
### fim 1


############################################ Aula 07 #######################################################    
### 1
def detectar_pontes(g: Graph):
    """ Implemente o algoritmo de detectar pontes"""
    tempo = 0
    pre = [-1 for _ in range(g.v)]
    pai = [-1 for _ in range(g.v)]
    low = [-1 for _ in range(g.v)]

    for v in range(g.v):
        if pre[v] == -1:
            pai[v] = v
            dfs_visita_ponte(g, v, tempo, pre, pai, low)

def dfs_visita_ponte(g: Graph, v, tempo, pre, pai, low):
    tempo += 1
    pre[v] = tempo
    low[v] = pre[v]

    for w in g.e[v]:
        if pre[w] == -1:
            pai[w] = v
            dfs_visita_ponte(g, w, tempo, pre, pai, low)
            low[v] = min(low[v], low[w])
            if low[w] == pre[w]:
                print(v, w)
        elif w != pai[v]:
            low[v] = min(low[v], pre[w])
### fim 1

### 2
def detectar_articulacoes(g: Graph):
    """ Implemente o algoritmo de detectar pontos de articulação"""
    tempo = 0
    pre = [-1 for _ in range(g.v)]
    pai = [-1 for _ in range(g.v)]
    low = [-1 for _ in range(g.v)]

    for v in range(g.v):
        if pre[v] == -1:
            pai[v] = v
            dfs_visita_articulacoes(g, v, tempo, pre, pai, low)

def dfs_visita_articulacoes(g: Graph, v, tempo, pre, pai, low):
    tempo += 1
    pre[v] = tempo
    low[v] = pre[v]
    filhos = 0
    eh_articulacao = False

    for w in g.e[v]:
        if pre[w] == -1:
            pai[w] = v
            filhos += 1
            dfs_visita_articulacoes(g, w, tempo, pre, pai, low)
            low[v] = min(low[v], low[w])
            if low[w] >= pre[w]:
                eh_articulacao = True
        elif w != pai[v]:
            low[v] = min(low[v], pre[w])
    
    if(pai[v] != -1 and eh_articulacao) or (pai[v] == -1 and filhos > 0):
        print(v)

############################################ Aula 08 #######################################################    
### 1
def eh_euleriano(g: Graph):
    """
    Considere um grafo não-dirigido conexo G, escreva um método que devolva True caso G for euleriano e False caso contrário.
    Um grafo conexo é euleriano se e somente se todo vértice
    tem grau par.
    """
    # 0: grau par, 1: grau ímpar
    graus = {0: 0, 1: 0}

    for v in range(g.v):
        graus[g.grau_saida(v) % 2] += 1

    if graus[1] == 0:
        return True
    
    return False

### 2 
def tem_trilha_euleriana(g: Graph):
    """
    Seja G um grafo não-dirigido conexo. Escreva um método que devolva Ture se G tem uma trilha euleriana e False caso contrário.
    Um grafo conexo tem uma trilha euleriana se e somente se
    tem exatamente 2 vértices de grau ímpar.
    """
    # 0: grau par, 1: grau ímpar
    graus = {0: 0, 1: 0}

    for v in range(g.v):
        graus[g.grau_saida(v) % 2] += 1

    if graus[1] == 2:
        return True
    
    return False

### 3 
def fleury(g: Graph):
    # 0: grau par, 1: grau ímpar
    graus = {0: [], 1: []}

    for v in range(g.v):
        graus[g.grau_saida(v) % 2].append(v)

    v = 0

    if len(graus[1]) != 2:
        print("Não existe trilha de Euler")
        return
    elif len(graus[1]) == 0:
        v = 0
    else:
        v = graus[1][0]

    trilha = []
    mostra_trilha_euleriana(g, v, trilha)
    print(trilha)

def mostra_trilha_euleriana(g: Graph, v: int, trilha):
    trilha.append(v)
    if len(g.e[v]) == 0: return

    for w in g.e[v]:
        if eh_ponte(g, v, w) == False:
            remove_no(g, v, w)
            mostra_trilha_euleriana(g, w, trilha)
            return

def eh_ponte(g:Graph, v: int, w: int):
    remove_no(g, v, w)
    if len(g.e[v]) == 1:
        return False
    if eh_conexo(g):
        resultado = True
    else:
        resultado = False
    
    g.insere(v, w)
    return resultado

###
# hierholzer
#TODO

###
# hamiltoniano
# TODO

############################################ Aula 09 #######################################################    

def bfs(g: Graph, s):
    """ Implemente o algoritmo de Busca em profundidade (BFS) """
    
    visitado = [False for _ in range(g.v)]
    visitado[s] = True

    queue = []
    queue.append(s)
    while len(queue) != 0:
        v = queue.pop(0)
        for w in g.e[v]:
            if not visitado[w]:
                visitado[w] = True
                queue.append(w)

def bfs_cor(g: Graph, s):
    """Implemente o algoritmo de Busca em profundidade (BFS)
    utilizando cores."""
    cor = [BRANCO for _ in range(g.v)]
    pai = [None for _ in range(g.v)]

    cor[s] = CINZA

    queue = [s]

    while len(queue) != 0:
        v = queue.pop(0)

        for w in g.e[v]:
            if cor[w] == BRANCO:
                cor[w] = CINZA
                pai[w] = v
                queue.append(w)
        cor[v] = PRETO

############################################ Aula 10 #######################################################    
###
def dijkstra(g: Graph, s: int, p):
    INF = float('inf')
    d = [INF for _ in range(g.v)]
    pi = [None for _ in range(g.v)]
    d[s] = 0
    queue = []
    n = g.v
    
    while n > 0:
        u = extrai_minimo(queue, d, g)
        queue.append(u)

        for v in g.e[u]:
            if d[v] > d[u] + p[u][v]:
                d[v] = d[u] + p[u][v]
                pi[v] = u
        n -= 1

def extrai_minimo(S, d, g):
    menor = float('inf')
    min = 0

    for u in range(g.v):
        if u not in S and d[u] < menor:
            menor = d[u]
            min = u
    
    return min
###

###

def pai(i): return i/2
def esq(i): return 2*i
def dir(i): return 2*i + 1

def sobe_heap(i, A):
    j = pai(i)
    while j <= 1 and A[i] < A[j]:
        A[i], A[j] = A[j], A[i]
        j = pai(i)

def insere_heap(A, n, item):
    n += 1
    A[n] = item
    sobe_heap(n, A)

def desce_heap(A, n, i):
    while 2 * i <= n:
        e = esq(i)
        d = dir(i)

        if d <= n and A[d] < A[e]:
            j = d
        else:
            j = e
        
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]
            i = j
        else:
            i = n + 1

def extrai_min(A, n):
    min = A[1]
    A[1] = A[n]
    desce_heap(A, n-1, 1)
    return min

def constroi_heap(A, n):
    for i in range(floor(n/2), 1, -1):
        desce_heap(A, n, i)


############################################ Aula 11 #######################################################    

def relaxar(u, v, p, d, pi):
    if d[v] > d[u] + p[u][v]:
        d[v] = d[u] + p[u][v]
        pi[v] = u

def todas_arestas(g: Graph):
    res = []
    for i in range(g.v):
        for j in g.e[i]:
            res.append((i,j))
    
    return res

def bellman_ford(g: Graph, s, p):
    d = [float('inf') for _ in range(g.v)]
    pi = [None for _ in range(g.v)]

    d[s] = 0

    for i in range(1, g.v-1, 1):
        for (u,v) in todas_arestas(g):
            relaxar(u, v, p, d, pi)
        
    for (u,v) in todas_arestas(g):
        if d[v] > d[u] + p[u][v]:
            return False
    
    return True

############################################ Aula 12 #######################################################    

#https://www.programiz.com/dsa/floyd-warshall-algorithm
# Algorithm implementation
def floyd_warshall(g: Graph):
    distance = list(map(lambda i: list(map(lambda j: j, i)), g))

    # Adding vertices individually
    for k in range(g.v):
        for i in range(g.v):
            for j in range(g.v):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)


# Printing the solution
def print_solution(g: Graph, distance):
    INF = float('inf')
    for i in range(g.v):
        for j in range(g.v):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


############################################ Aula 13 #######################################################    

###
def prim(g: Graph, s, p):
    chave = [float('inf') for _ in range(g.v)]
    cor = [CINZA for _ in range(g.v)]
    pi = [None for _ in range(g.v)]

    chave[s] = 0

    queue = [s]

    while len(queue) != 0:
        u = queue.pop(0)

        for v in g.e[u]:
            if cor[v] == CINZA and chave[v] > p[u][v]:
                chave[v] = p[u][v]
                pi[v] = u
                queue.append(v)
        
        cor[v] = PRETO
###        

###
def make_set(id, x):
    id[x] = x

def find(id, x):
    if id[x] == x:
        return x
    
    return find(id, id[x])

def union(id, x, y):
    x = find(id, x)
    y = find(id, y)
    id[y] = x

def ordena_arestas_por_peso(arestas, pesos):
    are = list(map(lambda x: (x[0], x[1], pesos[x[0]][x[1]]), arestas))
    ar = sorted(are, key= lambda x: x[2])

    return list(map(lambda x: (x[0], x[1]), ar))


def kruskal(g:Graph, pesos):
    arestas = todas_arestas(g)
    arestas = ordena_arestas_por_peso(arestas, pesos)

    a = set()
    id = [0 for _ in range(g.v)]
    for v in range(g.v):
        make_set(id, v)
    
    for (u, v) in arestas:
        if find(id, u) != find(id, v):
            a.add((u,v))
            union(id, u,v)

    return a
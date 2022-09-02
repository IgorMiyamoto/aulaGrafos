from functools import reduce

class Graph():
    def __init__(self, v = None, e = None, direcionado = False, usaMatriz = False):
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


    def grau_entrada(self, v):
        gr = 0
        if self.usaMatriz:
            for i in range(self.v):
                gr += self.e[i][v]
        else:
            for i in range(self.v):
                gr += 1 if (v in self.e[i]) else 0

        return gr
            
    
    def grau_saida(self, v):
        if self.usaMatriz:
            return reduce(lambda a, b: a + b, self.e[v])
        else:
            return len(self.e[v])

    def compara_grafos(g, h):
        if g.v != h.v: return False

        if g.usaMatriz == True and h.usaMatriz == True:
            return _compara_matriz(g, h)
        #   for i in range(g.v):
        #     for j in range(g.v):
        #       if g[i][j] != h[i][j]:
        #         return False
        #   return True
        elif g.usaMatriz == False and h.usaMatriz == False:
            return _compara_lista(g, h)
        #   for i in range(g.v):
        #     if len(g[i]) != len(h[i]):
        #       return False
        #     for j in range(len(g[i])):
        #       if g[i][j] != h[i][j]:
        #         return False
        #   return True
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

    def inverte_lista_adjacencia(self, u):
        if self.usaMatriz: print("Não usa lista de adjacencia"); return

        return list(reversed(self.e[u]))

def le_arquivo_grafo_direcionado(filename):
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

def lista_para_matriz(g):
    matriz = [[ 0 for _ in range(g.v)] for _ in range(g.v)]

    for i in range(g.v):
        for j in g.e[i]:
            matriz[i][j-1] = 1

    g.e = matriz.copy()
    g.usaMatriz = True
    return g

def matriz_para_lista(g):
    lista = [[] for _ in range(g.v)]

    for i in range(g.v):
        for j in range(g.v):
            if g.e[i][j]:
                lista[i].append(j+1)
            
    g.e = lista.copy()
    g.usaMatriz = False
    return g

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

    
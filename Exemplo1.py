# Programa Python3 para encontrar árvore geradora mínima
# de um gráfico usando algoritmo de exclusão reversa

# A classe Graph representa um gráfico direcionado
# usando representação de lista de adjacências
class Graph:
	def __init__(self, v):

		# Nº de vértices
		self.v = v
		self.adj = [0] * v
		self.edges = []
		for i in range(v):
			self.adj[i] = []

	# função para adicionar uma aresta ao gráfico
	def addEdge(self, u: int, v: int, w: int):
		self.adj[u].append(v) # Adicione w à lista de v.
		self.adj[v].append(u) # Adicione w à lista de v.
		self.edges.append((w, (u, v)))

	def dfs(self, v: int, visited: list):

		# Marque o nó atual como visitado e imprima-o
		visited[v] = True

		# Repita para todos os vértices adjacentes a este vértice
		# this vertex
		for i in self.adj[v]:
			if not visited[i]:
				self.dfs(i, visited)

	# Returns true if graph is connected
	# Retorna verdadeiro se determinado gráfico estiver conectado, caso contrário, falso
	def connected(self):
		visited = [False] * self.v

		# Encontre todos os vértices acessíveis do primeiro vértice
		self.dfs(0, visited)

		# Se o conjunto de vértices alcançáveis ​​inclui todos,retorne verdadeiro.
		for i in range(1, self.v):
			if not visited[i]:
				return False

		return True

	# Esta função assume que a aresta (u, v)
	# existe no gráfico ou não,
	def reverseDeleteMST(self):

		# Classifique as arestas em ordem crescente com base no custo
		self.edges.sort(key = lambda a: a[0])

		mst_wt = 0 #Inicializar peso do MST

		print("Edges in MST")

		# Iterar por todas as arestas classificadas em ordem decrescente de pesos
		for i in range(len(self.edges) - 1, -1, -1):
			u = self.edges[i][1][0]
			v = self.edges[i][1][1]

			# Remover borda do gráfico não direcionado
			self.adj[u].remove(v)
			self.adj[v].remove(u)

			# Adicionando a borda de volta se for removê-la
			# causa desconexão. Neste caso isso edge passa a fazer parte do MST.
			if self.connected() == False:
				self.adj[u].append(v)
				self.adj[v].append(u)

				# Essa borda faz parte do MST
				print("( %d, %d )" % (u, v))
				mst_wt += self.edges[i][0]
		print("O peso total do MST é", mst_wt)

# Código do motorista
if __name__ == "__main__":

	# crie o gráfico fornecido na figura acima
	V = 9
	g = Graph(V)

	# fazendo o gráfico mostrado acima
	g.addEdge(0, 1, 6)
	g.addEdge(0, 7, 9)
	g.addEdge(1, 2, 5)
	g.addEdge(1, 7, 8)
	g.addEdge(2, 3, 10)
	g.addEdge(2, 8, 3)
	g.addEdge(2, 5, 7)
	g.addEdge(3, 4, 4)
	g.addEdge(3, 5, 12)
	g.addEdge(4, 5, 11)
	g.addEdge(5, 6, 8)
	g.addEdge(6, 7, 2)
	g.addEdge(6, 8, 5)
	g.addEdge(7, 8, 1)

	g.reverseDeleteMST()
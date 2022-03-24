from grafo2dot import guardar_grafo
from grafo import Grafo




# Generacion de grafos Barabási-Albert 
grafo_babarasi_30_10 = Grafo(dirigido=False)
grafo_babarasi_30_10.grafo_barabasi_albert(30, 5)
guardar_grafo(grafo_babarasi_30_10, "babarasi_30_05") #30 nodos grado 05



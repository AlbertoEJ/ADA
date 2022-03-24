from grafo2dot import guardar_grafo
from grafo import Grafo

#Generacion de grafos de mallas
grafo_malla_30 = Grafo(dirigido=False)
grafo_malla_30.grafo_malla(5, 6) #Grafo de 5*6 nodos
guardar_grafo(grafo_malla_30, "malla30") 


grafo_malla_100 = Grafo(dirigido=False)
grafo_malla_100.grafo_malla(10, 10) #Grafo de 10*10 nodos
guardar_grafo(grafo_malla_100, "malla100")


grafo_malla_500 = Grafo(dirigido=False)
grafo_malla_500.grafo_malla(50, 10) #Grafo de 50*10 nodos
guardar_grafo(grafo_malla_500, "malla500")



# Generacion de grafos Erdös y Rényi
grafo_erdos_30_400 = Grafo(dirigido=False)
grafo_erdos_30_400.grafo_erdos_renyi(30, 400) #Grafo de 30 nodos con 400 aristas
guardar_grafo(grafo_erdos_30_400, "erdos_30_400")



grafo_erdos_100_1500 = Grafo(dirigido=False)
grafo_erdos_100_1500.grafo_erdos_renyi(100, 1500)
guardar_grafo(grafo_erdos_100_1500, "erdos_100_1500") #Grafo de 100 nodos con 400 aristas

grafo_erdos_500_4000 = Grafo(dirigido=False)
grafo_erdos_500_4000.grafo_erdos_renyi(500, 4000) #Grafo de 500 nodos con 4000 aristas
guardar_grafo(grafo_erdos_500_4000, "erdos_500_4000")



# Generacion de grafos de Gilbert 
grafo_gilbert_30_07 = Grafo(dirigido=False)
grafo_gilbert_30_07.grafo_gilbert(30, 0.7) #Grafo de 30 nodos con probabilidad 0.7
guardar_grafo(grafo_gilbert_30_07, "gilbert_30_07")

grafo_gilbert_100_06 = Grafo(dirigido=False)
grafo_gilbert_100_06.grafo_gilbert(100, 0.6) #Grafo de 100 nodos con probabilidad 0.6
guardar_grafo(grafo_gilbert_100_06, "gilbert_100_06")


grafo_gilbert_500_004 = Grafo(dirigido=False)
grafo_gilbert_500_004.grafo_gilbert(500, 0.04) #Grafo de 500 nodos con probabilidad 0.04
guardar_grafo(grafo_gilbert_500_004, "gilbert_500_004")


# Generacion de grafos modelo geográfico simple
grafo_geografico_30_04 = Grafo(dirigido=False)
grafo_geografico_30_04.grafo_geografico(30, 0.4)
guardar_grafo(grafo_geografico_30_04, "geografico_30_04") #30 nodos r=0.4


grafo_geografico_100_03 = Grafo(dirigido=False)
grafo_geografico_100_03.grafo_geografico(100, 0.3)
guardar_grafo(grafo_geografico_100_03, "geografico_100_03") #100 nodos, r=0.3


grafo_geografico_500_01 = Grafo(dirigido=False)
grafo_geografico_500_01.grafo_geografico(500, 0.1)
guardar_grafo(grafo_geografico_500_01, "geografico_500_01") #500 nodos, r=0.1


# Generacion de grafos Barabási-Albert 
grafo_babarasi_30_5 = Grafo(dirigido=False)
grafo_babarasi_30_5.grafo_barabasi_albert(30, 5)
guardar_grafo(grafo_babarasi_30_5, "babarasi_30_05") #30 nodos grado 05


grafo_babarasi_100_09 = Grafo(dirigido=False)
grafo_babarasi_100_09.grafo_barabasi_albert(100, 9) #100 nodos grado 9
guardar_grafo(grafo_babarasi_100_09, "babarasi_100_09")


grafo_babarasi_500_20 = Grafo(dirigido=False)
grafo_babarasi_500_20.grafo_barabasi_albert(500, 20) #500 nodos grado 20
guardar_grafo(grafo_babarasi_500_20, "babarasi_500_20")


# Generacion de grafos Dorogovtsev-Mendes 
grafo_dorogovtsev_mendes_30 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_30.dorogovtsev_mendes(30) #30 nodos
guardar_grafo(grafo_dorogovtsev_mendes_30, "dorogovtsev_mendes_30")

grafo_dorogovtsev_mendes_100 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_100.dorogovtsev_mendes(100) #100 nodos
guardar_grafo(grafo_dorogovtsev_mendes_100, "dorogovtsev_mendes_100")

grafo_dorogovtsev_mendes_500 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_500.dorogovtsev_mendes(500) #500 nodos
guardar_grafo(grafo_dorogovtsev_mendes_500, "dorogovtsev_mendes_500")





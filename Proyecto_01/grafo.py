from arista import Arista
from nodo import Nodo
import random
import itertools
import math
"""
Autor: Alberto Espinosa Juárez
Escuela: CIC IPN
Materia: Analisis y Diseño de Algoritmos
Ruta: D:\Escuela\CIC\Segundo\ADA\Proyecto_1
"""

class Grafo:
    """
    Creacion de la clase grafo, aqui se almacenaran todos los algoritmos y se crearan los grafos, para ello, 
    es necesario en primera instancia que las clases Nodo Y Arista se encuentren importadas correctamente
    """
    def __init__(self, dirigido=False):

        """
        Constructor de la clase
        """
        self.nodos = {}  # diccionario para almacenar los nodos con su etiqueta como llave
        self.__aristas = set()  # mantiene las aristas guardadas en un conjunto
        self.__dirigido = dirigido  # parametro para saber si el grafo es dirigido

    def __str__(self):  # sobreescritura del metodo string
        """
        Permite la creacion de objetos de tipo grafo (muestra)
        """
        imp_cadena = ""

        for llave in self.nodos:
            imp_cadena += str(self.nodos[llave]) + '\n'

        return imp_cadena

    def add_nodo(self, etiqueta): 
        """
        Metodo que nos permite crear un nodo

        Parametro: 
        Etiqueta

        Retorna

        Nodo con la etiqueta colocada
        """
        if etiqueta not in self.nodos:
            self.nodos[etiqueta] = Nodo(etiqueta, self.__dirigido)

    def add_arista(self, etiqueta_inicio, etiqueta_final):  

        """
        Metodo para la creacion de una arista. Regresara un mensaje si no se encuentra el nodo inicial o final

        Parametros:
        Nodo_inicio
        Nodo_final

        Retorna
        Arista que conecta nodo A--B 
        """
        nodo_fuente = self.get_nodo(etiqueta_inicio)
        nodo_final = self.get_nodo(etiqueta_final)
        mirror_edge = None
        if (nodo_fuente or nodo_final) is None:  # si no existe el nodo fuente o el nodo destino salta el error
            raise ValueError("El nodo inicio o final no existe, debes crearlo primero")
        if self.__dirigido:  # Si el grafo es dirigido se agrega la arista tal cual
            arista = Arista(nodo_fuente, nodo_final, self.__dirigido)
        else:
            for aristaen in self.get_aristas():
                nodo_fuente_arista = aristaen.get_nodo_fuente()
                nodo_destino_arista = aristaen.get_nodo_destino()
                if (nodo_destino_arista == nodo_fuente) and (nodo_fuente_arista == nodo_final):
                    mirror_edge = True
            if not mirror_edge:
                arista = Arista(nodo_fuente, nodo_final, self.__dirigido)
            else:
                arista = Arista(nodo_final, nodo_fuente, self.__dirigido)
        nodo_fuente.add_arista(arista)
        if nodo_fuente != nodo_final:
            nodo_final.add_arista(arista)

        self.__aristas.add(arista)

    def remove_arista(self, etiqueta_inicio, etiqueta_final):  
        """
        Metodo para eliminar una arista

        Parametros:
        Nodo_inciial
        Nodo_final

        Retorna:
        La eliminacion de la arista
        """
        nodo_fuente = self.get_nodo(etiqueta_inicio)
        nodo_destino = self.get_nodo(etiqueta_final)

        if (nodo_fuente or nodo_destino) is None:
            raise ValueError("No se encontro el nodo fuente o el nodo destino en el grafo")

        arista = Arista(nodo_fuente, nodo_destino, self.__dirigido)

        if arista not in self.__aristas:
            raise ValueError( "no se encuentra la arista  {0} en el grafo".format(str(Arista)))

        nodo_fuente.remove_arista(arista)
        nodo_destino.remove_arista(arista)
        self.__aristas.remove(arista)

    def remove_nodo(self, etiqueta_nodo): 

        """
        Metodo que permite la eliminacion del nodo en el grafo
        """
        if etiqueta_nodo not in self.nodos:
            raise ValueError("No se encontro el nodo {0} en el grafo".format(etiqueta_nodo))

        nodo = self.nodos[etiqueta_nodo]

        copia_aristas_entrantes = nodo.get_aristas_entrantes().copy()  # Removemos la entrada de las aristas entrantes
        for arista in copia_aristas_entrantes:
            nodo_adyacente = arista.get_nodo_fuente()
            nodo_adyacente.remove_arista(arista)

            if arista in self.__aristas:
                self.__aristas.remove(arista)

        copia_aristas_salientes = nodo.get_aristas_salientes().copy()
        for arista in copia_aristas_salientes:  # Removemos la entrada de las aristas salientes
            adjacent_vertex = arista.get_nodo_destino()
            adjacent_vertex.remove_arista(arista)

            if arista in self.__aristas:
                self.__aristas.remove(arista)

        self.nodos.pop(etiqueta_nodo)

        nodos = self.get_nodos()
        for nodo in nodos:
            aristas = nodos[nodo].get_aristas()
            copia_aristas = aristas.copy()
            for arista in aristas:
                nodo = arista.get_nodo_fuente()
                if nodo.get_etiqueta() == etiqueta_nodo:
                    copia_aristas.remove(arista)
                nodo.set_aristas(copia_aristas)


    def get_nodo(self, etiqueta):
        return self.nodos.get(etiqueta)

    def get_nodos(self):
        return self.nodos

    def get_aristas(self):
        return self.__aristas

    def get_grado(self, etiqueta):
        if self.es_dirigido():
            grado = len(self.get_nodo(etiqueta).get_aristas_entrantes()) + \
                    len(self.get_nodo(etiqueta).get_aristas_salientes())
        else:
            grado = len(self.get_nodo(etiqueta).get_aristas_salientes())
        return grado

    def es_dirigido(self):  # Metodo que regresa si el grafo es dirigido
        return self.__dirigido

    #Grafo Malla
    def grafo_malla(self, m, n):
        """
        Metodo que permite la creacion de un grafo en malla
        Parametros
        m
        n

        Devuelve

        Grafo en malla de m*n
        """
        for i in range(m * n):  # se comienza creando los n nodos
            self.add_nodo(str(i))
        for j in range(m):
            index_horizontal = j * n
            for i in range(index_horizontal, index_horizontal + n):
                if (i != (n - 1) + index_horizontal):
                    self.add_arista(str(i), str(i + 1))
                if j != (m - 1):
                    self.add_arista(str(i), str(i + n))
        return self
    #Grafo Erdos Renyi
    def grafo_erdos_renyi(self, n, m, dirigido=False, auto=False): 
        """
        Metodo que crea un grafo con el algoritmo Erdos Renyi
        Parametros:
        n
        m
        Direccion
        Auto 

        Retorna
        Grafo Erdos Renyi de n*m
        """
        self.__dirigido = dirigido
        for i in range(n):
            self.add_nodo(str(i))
        while len(self.get_aristas()) != m:
            n1 = (random.randrange(n))
            n2 = (random.randrange(n))
            if not auto:
                if n1 != n2:
                    self.add_arista(str(n1), str(n2))
            else:
                self.add_arista(str(n1), str(n2))
        print(len(self.get_aristas()))
        return self
    
    #grafo Gilbert
    def grafo_gilbert(self, n, p, dirigido=False, auto=False):

        """
        Metodo que permite crear un grafo con el algoritmo de Gilbert

        Parametros:
        n
        p
        Direccion
        Auto

        Devuelve:
        Grafo de n nodos con probabilidad p
        """
        self.__dirigido = dirigido
        for i in range(n):
            self.add_nodo(str(i))
        for i in range(n):
            for j in range(n):
                if not auto:
                    if (i != j):
                        if random.random() <= p:
                            self.add_arista(str(i), str(j))
        print(len(self.get_aristas()))
        return self

    def grafo_geografico(self, n, r, dirigido=False, auto=False):  # metodo para generar el modelo geografico

        """
        Metodo que permite la creacion de un grafo geografico

        Parametros:
        n
        r
        direccion
        auto

        Retorna
        Un grafo geografico de n nodos con distancia maxima r(0,1)
        """
        self.__dirigido = dirigido  # parametro dirigido
        for i in range(n):  # se crean n nodos
            self.add_nodo(str(i))
        posicion_nodos = {}  # diccionario para mantener las cordenadas de los nodos
        for nodo in self.get_nodos():  # asignamos cordenadas  a los nodos
            llave = nodo
            posicion_random = (random.random(), random.random())
            posicion_nodos.update({llave: posicion_random})
        combinaciones = itertools.combinations(posicion_nodos, 2)  # todos los posibles pares si el grafo es no dirigido
        permutaciones = itertools.permutations(posicion_nodos, 2)  # todos los posibles pares si el grafi es dirigido
        if not dirigido:  # si el grafo es no dirigido usamos las combinaciones para comparar la distancia de los pares
            for combinacion in combinaciones:
                nodo_fuente = combinacion[0]
                nodo_destino = combinacion[1]
                cordenadas_nodo_fuente = posicion_nodos.get(combinacion[0])
                cordenadas_nodo_destino = posicion_nodos.get(combinacion[1])
                nodo_fuente_x = cordenadas_nodo_fuente[0]
                nodo_fuente_y = cordenadas_nodo_fuente[1]
                nodo_destino_x = cordenadas_nodo_destino[0]
                nodo_destino_y = cordenadas_nodo_destino[1]
                # calculamos la distancia entre pares
                distancia = math.sqrt((nodo_destino_x - nodo_fuente_x) ** 2 + (nodo_destino_y - nodo_fuente_y) ** 2)
                # si la distancia es menor o igual a r se genera la arista ente pares
                if (distancia <= r):
                    self.add_arista(nodo_fuente, nodo_destino)
        else:  # lo mismo pero cuando el grafo es no dirigido usamos permutaciones
            for permutacion in permutaciones:
                nodo_fuente = permutacion[0]
                nodo_destino = permutacion[1]
                cordenadas_nodo_fuente = posicion_nodos.get(permutacion[0])
                cordenadas_nodo_destino = posicion_nodos.get(permutacion[1])
                nodo_fuente_x = cordenadas_nodo_fuente[0]
                nodo_fuente_y = cordenadas_nodo_fuente[1]
                nodo_destino_x = cordenadas_nodo_destino[0]
                nodo_destino_y = cordenadas_nodo_destino[1]
                distancia = math.sqrt((nodo_destino_x - nodo_fuente_x) ** 2 + (nodo_destino_y - nodo_fuente_y) ** 2)
                if (distancia <= r):
                    self.add_arista(nodo_fuente, nodo_destino)
        return self


    #grafo Dorogovtsev-Mendes
    def dorogovtsev_mendes(self, n, dirigido=False):
        """
        Metodo que permite la creacion de un grafo Dorogovtsev-Mendes

        Parametros
        n

        Retorna:
        Grafo de n nodos
        """
        self.__dirigido = dirigido
        for i in range(3):
            self.add_nodo(str(i))
        self.add_arista("0", "1")
        self.add_arista("0", "2")
        self.add_arista("1", "2")
        # print(self.get_grado("0"))
        while len(self.get_nodos()) != n:
            nodo_nuevo = str(len(self.get_nodos()) + 1)
            self.add_nodo(nodo_nuevo)
            arista_random = random.choice(list(self.get_aristas()))
            nodo_fuente = arista_random.get_nodo_fuente()
            etiqueta_nodo_fuente = nodo_fuente.get_etiqueta()
            nodo_destino = arista_random.get_nodo_destino()
            etiqueta_nodo_destino = nodo_destino.get_etiqueta()
            self.add_arista(nodo_nuevo, etiqueta_nodo_fuente)
            self.add_arista(nodo_nuevo, etiqueta_nodo_destino)
        print("numero de nodos: {}".format(len(self.get_nodos())))
        print("numero de aristas: {}".format(len(self.get_aristas())))
        return self

    #Grafo Barabási-Albert
    def grafo_barabasi_albert(self, n, d, dirigido=False, auto=False):

        """
        Metodo que permite crear un grafo Barabási-Albert

        Parametros:
        n
        d
        direccion
        auto

        Retorna:
        Grafo de Barabási-Albert con n nodos y grado maximo d
        """
        self.__dirigido = dirigido
        for i in range(n):  # se generan n nodos
            self.add_nodo(str(i))
        for i in range(n):  # iteramos entre todos los posibles pares
            for j in range(n):
                if not auto:  # si no se permiten autociclos
                    if i != j:
                        if (self.get_grado(str(j)) < d) and (self.get_grado(str(i)) < d):
                            p = 1 - (self.get_grado(str(j)) / d)
                            if random.random() <= p:  # si el numero random es menor o igual a la probailidad se crea
                                self.add_arista(str(i), str(j))
                else:  # lo  mismo pero si se permiten autociclos
                    if (self.get_grado(str(j)) < d) and (self.get_grado(str(i)) < d):
                        p = 1 - (self.get_grado(str(j)) / d)
                        if random.random() <= p:
                            self.add_arista(str(i), str(j))
        print(len(self.get_aristas()))
        return self


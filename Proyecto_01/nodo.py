"""
Autor: Alberto Espinosa Juárez
Escuela: CIC IPN
Materia: Analisis y Diseño de Algoritmos
Ruta: D:\Escuela\CIC\Segundo\ADA\Proyecto_1
"""

class Nodo:
    """
    Clase nodo de la cual se crearan los objetos de tipo nodo con atributos como su etiqueta, arista y si es o no dirigido
    """
    def __init__(self, etiqueta, dirigido=False):
        """
        Constructor de la clase nodo
        Atributos
        Etiqueta - ID del nodo
        No dirigido 

        Se utiliza un conjunto (set) para poder unir a los nodos con sus aristas
        """
        self.__etiqueta = etiqueta  # identificador del nodo
        self.__dirigido = dirigido  # parametro dirigido se usa para saber si el grafo es dirigido
        self.__aristas = set()  # Estructura de datos tipo set, util para mantener las aristas conectadas al nodo

    def __str__(self):  
        """
        Metodo __str__
        Recordemos que el metodo nativo de python str nos permite mostrar los objetos del tipo de la clase

        """
        
        cadena_retorno = ""
        for arista in self.__aristas:
            cadena_retorno += str(arista)

        return cadena_retorno

    def get_aristas(self): 
        """
        Regresa una arista especifica en el nodo
        """
        return self.__aristas

    def get_etiqueta(self):  
        """
        Rgresa la etiqueta que identifica al nodo
        """
        return self.__etiqueta


    def get_aristas_salientes(self):
        """
        # Si el grafo es dirigido regresa las aristas que salen del nodo
        """
        if not self.__dirigido:
            return self.__aristas

        aristas_salientes = []
        for arista in self.__aristas:
            if arista.get_nodo_fuente() == self:
                aristas_salientes.append(arista)

        return aristas_salientes

    def get_aristas_entrantes(self):
        """
        Si el grafo es dirigido regresa las aristas que entran al nodo
        """
        if not self.__dirigido:
            return self.__aristas

        aristas_entrantes = []
        for arista in self.__aristas:
            if arista.get_nodo_destino() == self:
                aristas_entrantes.append(arista)

        return aristas_entrantes


    def add_arista(self, arista):
        """
        Metodo que sirve para agregar una arista

        Atributos:
        Arista

        Retorna:

        Creacion de una arista
        """
        self.__aristas.add(arista)  # se agrega una arista al set que guarda las aristas del nodo

    def remove_arista(self, arista):
        """
        Metodo que elimina una arista

        Atributos:
        Arista

        Retorna:
        Eliminacion de una arista
        """
        
        if arista in self.__aristas:  # Si se encuentra la arista en el nodo se remueve la arista
            self.__aristas.remove(arista)  # se remueve una arista del set que guarda las aristas
        else:  # si no se encuentra la arista en el nodo lanza el sigueinte error
            raise ValueError(
                "No existe la arista {0} en el  nodo {1}".format(str(arista), str(self)))

    def set_aristas(self, aristas):  
        self.__aristas = aristas

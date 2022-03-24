"""
Autor: Alberto Espinosa Juárez
Escuela: CIC IPN
Materia: Analisis y Diseño de Algoritmos
Ruta: D:\Escuela\CIC\Segundo\ADA\Proyecto_1
"""

class Arista:

    """
    La clase arista sera la encargada de unir dos nodos.
    
    Parametros:
    Nodo inicio - Se indica el nodo que servira como fuente
    Nodo final - Se indica el nodo que servira como destino
    """
    def __init__(self, nodo_inicio, nodo_final, dirigido=False):

        """
        Constructor de la clase nodo

        Parametros
        Nodo inicio
        Nodo final
        No Dirigido
        """
        self.__nodo_inicio = nodo_inicio  # nodo inicio
        self.__nodo_final = nodo_final  # nodo final

        self.__dirigido = dirigido  # parametro para seber si el grafo es dirigido

    
    def __str__(self):
        """
        El metodo __str__ nos sevira para poder lograr una notacion en tipo dot de tipo -- o -> segun corresponda (no dirigido o dirigido)
        
        Retorna:
        1--2
        o
        1->2
        """
        if self.__dirigido:
            print_pattern = "{0}->{1}"
        else:
            print_pattern = "{0} -- {1} "
        return print_pattern.format(self.__nodo_inicio.get_etiqueta(), self.__nodo_final.get_etiqueta())

    
    def get_nodo_fuente(self):
        """
        Este metodo lo que hacees devolver el nodo inicial de la arista
        
        Ejemplo
        A--B

        Retorna
        A
        """
        return self.__nodo_inicio

    
    def get_nodo_destino(self):

        """
        Este metodo lo que hace es devolver el nodo final de la arista

        Ejemplo
        A--B
        Retorna
        B
        """
        return self.__nodo_final

    # Sobrecritura de los metodos hash y eq
    def __eq__(self, otro):

        """
        Este metodo es propio de Python y en este codigo esta sobreescrito
        Se sobreescribe para verificar la igualdad entre los nodos

        Parametros
        Propio
        Otro

        El parametro propio es nativo de eq, otro es el parametro nodo
        """
        nodo_inicio_igual = self.__nodo_inicio == otro.get_nodo_fuente()
        nodo_final_igual = self.__nodo_final == otro.get_nodo_destino()

        return nodo_inicio_igual == nodo_final_igual == True

    def __hash__(self):
        """
        Lo que hacemos aqui es sobrecargar el metodo hash esto se hace para
        generar un hash (codigo unico de cada nodo) para su etiqueta
        asi ningun nodo podra tener la misma etiqueta

        Retorna:

        Hash de la etiqueta del nodo inicial y final
        """
        return hash(self.__nodo_inicio.get_etiqueta() +
                    self.__nodo_final.get_etiqueta())

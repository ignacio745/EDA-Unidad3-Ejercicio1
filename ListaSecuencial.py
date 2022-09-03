import numpy as np

class ListaSecuencial:
    __dimension: int
    __arreglo: np.ndarray
    __ultimo: int

    def __init__(self, dimension: int, tipo:type) -> None:
        self.__dimension = dimension
        self.__arreglo = np.empty(self.__dimension, tipo)
        self.__ultimo = -1

    
    def insertar(self, elemento, posicion:int):
        posicion = posicion - 1
        if not self.__ultimo < self.__dimension-1:
            raise OverflowError("La lista está llena")
        if posicion < 0 or self.__ultimo < posicion-1:
            raise Exception("No se puede insertar en la posicion {0}, la lista solo tiene {1} componentes".format(posicion+1, self.__ultimo+1))
        
        for i in range(self.__ultimo - posicion + 1):
            self.__arreglo[self.__ultimo-i+1] = self.__arreglo[self.__ultimo-i]
        
        self.__arreglo[posicion] = elemento
        self.__ultimo += 1
    
    def recuperar(self, posicion:int):
        posicion = posicion - 1
        if posicion < 0 or posicion > self.__ultimo:
            raise Exception("No se puede recuperar un elemento en la posicion {0}, la lista solo tiene {1} elementos".format(posicion+1, self.__ultimo+1))
        return self.__arreglo[posicion]
    
    def vacia(self):
        return self.__ultimo == -1
    
    def suprimir(self, posicion:int):
        posicion = posicion - 1
        if self.vacia():
            raise Exception("No hay mas elementos en la lista")
        if posicion < 0:
            raise Exception("La posicion debe ser mayor o igual a 1")
        if posicion > self.__ultimo:
            raise Exception("No se puede suprimir un elemento de la posicion {0}, solo hay {1} elementos en la lista".format(posicion+1, self.__ultimo+1))
        
        elemento = self.__arreglo[posicion]
        for i in range(self.__ultimo - posicion):
            self.__arreglo[posicion+i] = self.__arreglo[posicion+i+1]
        
        self.__ultimo -= 1

        return elemento
    
    def primer_elemento(self):
        return self.__arreglo[0]
    
    def ultimo_elemento(self):
        return self.__arreglo[self.__ultimo]
    
    def siguiente(self, posicion):
        return self.recuperar(posicion+1)
    
    def anterior(self, posicion):
        return self.recuperar(posicion-1)
    
    def recorrer(self, operacion):
        for i in range(self.__ultimo+1):
            operacion(self.__arreglo[i])
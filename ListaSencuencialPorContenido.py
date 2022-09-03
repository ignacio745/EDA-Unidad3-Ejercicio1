import numpy as np

class ListaSecuencialPorContenido:
    __dimension: int
    __arreglo: np.ndarray
    __ultimo: int

    def __init__(self, dimension: int, tipo: type = int) -> None:
        self.__dimension = dimension
        self.__arreglo = np.empty(self.__dimension, tipo)
        self.__ultimo = -1
    
    def insertar(self, elemento):
        if self.__ultimo == self.__dimension - 1:
            raise OverflowError("La lista está llena")
        pos = 0
        while pos <= self.__ultimo and self.__arreglo[pos] < elemento:
            pos += 1
        
        # if pos > self.__ultimo:
        #     self.__arreglo[pos] = elemento
        # else:
        #     for i in range(self.__ultimo - pos + 1):
        #         self.__arreglo[self.__ultimo - i + 1] = self.__arreglo[self.__ultimo - i]
        #     self.__arreglo[pos] = elemento
        
        for i in range(self.__ultimo - pos + 1):
            self.__arreglo[self.__ultimo - i + 1] = self.__arreglo[self.__ultimo - i]
        self.__arreglo[pos] = elemento
        self.__ultimo += 1
    
    def vacia(self):
        return self.__ultimo == -1
    
    def suprimir(self, posicion):
        posicion -= 1
        if self.vacia():
            raise Exception("La lista esta vacia")
        if posicion < 0:
            raise Exception("La posicion debe ser mayor o igual a 1")
        if posicion > self.__ultimo:
            raise Exception("No se puede suprimir un elemento de la posicion {0}, solo hay {1} elementos en la lista".format(posicion+1, self.__ultimo+1))
        
        elemento = self.__arreglo[posicion]

        for i in range(self.__ultimo - posicion + 1):
            self.__arreglo[posicion + i] = self.__arreglo[posicion + i + 1]
        
        self.__ultimo -= 1
        
        return elemento
    
    def recuperar(self, posicion:int):
        posicion = posicion - 1
        if posicion < 0 or posicion > self.__ultimo:
            raise Exception("No se puede recuperar un elemento en la posicion {0}, la lista solo tiene {1} elementos".format(posicion+1, self.__ultimo+1))
        return self.__arreglo[posicion]    

    
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
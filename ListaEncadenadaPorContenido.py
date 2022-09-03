from Nodo import Nodo

class ListaEncadenadaPorContenido:
    __cabeza = None
    __cantidad = None

    def __init__(self) -> None:
        self.__cabeza = None
        self.__cantidad = 0
    
    def insertar(self, elemento):
        unNodo = Nodo(elemento)
        if self.__cantidad == 0:
            self.__cabeza = unNodo
        elif self.__cabeza.getElemento() > elemento:
            unNodo.setSig(self.__cabeza)
            self.__cabeza = unNodo
        else:
            anterior = self.__cabeza
            actual = self.__cabeza.getSig()
            while actual != None and actual.getElemento() < elemento:
                anterior = actual
                actual = actual.getSig()
            unNodo.setSig(actual)
            anterior.setSig(unNodo)
        self.__cantidad += 1

    
    def suprimir(self, posicion: int):
        if posicion < 1:
            raise Exception("La posicion debe ser mayor o igual a 1")
        if not (posicion <= self.__cantidad):
            raise Exception("No se puede suprimir un elemento de la posicion {0}, la lista tiene {1} elementos".format(posicion, self.__cantidad))
        
        if posicion == 1:
            elemento = self.__cabeza.getElemento()
            self.__cabeza = self.__cabeza.getSig()
        else:
            actual = self.__cabeza
            for i in range(posicion-2):
                actual = actual.getSig()
            elemento = actual.getSig().getElemento()
            actual.setSig(actual.getSig().getSig())
        self.__cantidad -= 1
        return elemento
    
    def vacia(self):
        return self.__cantidad == 0
    
    def recuperar(self, posicion: int):
        if not 1 <= posicion <= self.__cantidad:
            raise Exception("No hay elemento en la posicion {0}, la lista solo tiene {1} elementos".format(posicion, self.__cantidad))
        
        actual = self.__cabeza
        for i in range(posicion-1):
            actual = actual.getSig()
        
        return actual.getElemento()

    
    def primer_elemento(self):
        return self.__cabeza.getElemento()
    
    def ultimo_elemento(self):
        return self.recuperar(self.__cantidad)
    
    def siguiente(self, posicion):
        return self.recuperar(posicion+1)
    
    def anterior(self, posicion):
        return self.recuperar(posicion-1)
    
    def recorrer(self, operacion):
        actual = self.__cabeza
        for i in range(self.__cantidad):
            operacion(actual.getElemento())
            actual = actual.getSig()
    
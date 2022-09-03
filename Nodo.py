from __future__ import annotations

class Nodo:
    __elemento = None
    __sig = None

    def __init__(self, elemento) -> None:
        self.__elemento = elemento
        self.__sig = None

    def getElemento(self):
        return self.__elemento
    
    def setSig(self, sig):
        self.__sig = sig

    def getSig(self) -> Nodo:
        return self.__sig
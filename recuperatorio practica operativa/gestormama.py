from clasemamas import mamas
import csv
import numpy as np
class gestormama1:
    __gestormama = np.ndarray
    __dimension: int
    __incremento: int
    __cantidad: int
    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 1
        self.__gestormama = np.empty([0], dtype=mamas)

    def agregar(self, nuevamama):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__gestormama.resize(self.__dimension)
        self.__gestormama[self.__cantidad] = nuevamama
        self.__cantidad += 1
    def getarreglo(self):
        return self.__gestormama
    
    def inicializar(self):
        archivo=open("Mamas.csv")
        reader=csv.reader(archivo,delimiter=';')
        bandera = False
        for fila in reader:
            if bandera is False:
                bandera = True
            else:
                nuevamama = mamas(fila[0], (fila[2]), fila[1]) 
                self.agregar(nuevamama)
        archivo.close()
    def mostrar_arreglo(self):
         for mama in self.__gestormama:
              print(mama)
from clasenacimiento import nacimiento
import csv
class gestornacimiento1:
    __lista:list 

    def __init__(self):
        self.__lista=[]

    def agregar(self,nuevonacimiento):
        self.__lista.append(nuevonacimiento)
    def get_lista(self):
        return self.__lista
    def inicializar(self):
        archivo =open("Nacimientos.csv")
        reader=csv.reader(archivo,delimiter=';')
        bandera=False
        for fila in reader:
            if bandera is False:
                bandera = True
            else:
                nuevonacimiento=nacimiento(fila[0],fila[1],fila[2],fila[3],fila[4],int(fila[5]))
                self.agregar(nuevonacimiento)
        archivo.close()
    
    def mostrar_lista(self):
        for n in self.__lista:
            print(n)
    
    def datos(self,GM):
        dni=input("ingrese el DNI de una mama: ")
        bandera=False
        i=0
        while i<len(self.__lista) and not bandera:
            if self.__lista[i].get_dni_madre() ==dni:
                bandera = True
            else:
                i+=1
        if bandera == True:
            madres=GM.getarreglo()
            j=0
            while j< len(madres):
                if madres[j].get_dni() ==self.__lista[i].get_dni_madre():
                    print(f"""Apellido y Nombre: {madres[j].get_nombre_apellido()}
                          Edad: {madres[j].get_edad()}
                          Tipo de parto: {self.__lista[i].get_tipoparto()}
                          bebe/s:
                          peso: {self.__lista[i].get_peso()}\n 
                          altura: {self.__lista[i].get_altura()}
                          """)
                    break
                j+=1
        else: 
            print("el dni ingresado no existe en los archivos")


    def mostrar_partos_multiples(self, GM):
        multiples = []
        i = 0
        while i < len(self.__lista):
            nacimiento = self.__lista[i]
            j = 0
            while j < len(multiples):
                if multiples[j][0] == nacimiento:  
                    multiples[j].append(nacimiento)
                    break
                j += 1
            else:
                multiples.append([nacimiento])
            i += 1

        i = 0
        while i < len(multiples):
            parto_multiple = multiples[i]
            if len(parto_multiple) > 1:
                j = 0
                while j < len(GM.getarreglo()):
                    mama = GM.getarreglo()[j]
                    if mama.get_dni() == parto_multiple[0].get_dni_madre():
                        print(f"Mamá: {mama.get_nombre_apellido()}, DNI: {mama.get_dni()}, Edad: {mama.get_edad()}")
                        print(f"Fecha de parto múltiple: {parto_multiple[0].get_fecha()}")
                        k = 0
                        while k < len(parto_multiple):
                            nacimiento = parto_multiple[k]
                            print(f"  Tipo de parto: {nacimiento.get_tipoparto()}, Peso: {nacimiento.get_peso()}, Altura: {nacimiento.get_altura()}")
                            k += 1
                        break
                    j += 1
            i += 1

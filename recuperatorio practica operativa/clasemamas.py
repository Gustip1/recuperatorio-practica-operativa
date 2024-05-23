#Cada Mamá: DNI, edad, apellido y nombre
class mamas:
    __dni:str
    __edad:str
    __apellido_nombre:str
    

    def __init__(self,dni,nombre_apellido,edad):
        self.__dni=dni
        self.__edad=edad
        self.__apellido_nombre=nombre_apellido


    def get_dni(self):
        return self.__dni
    def get_edad(self):
        return self.__edad
    def get_nombre_apellido(self):
        return self.__apellido_nombre
   
    
    def __str__(self):
        return f"DNI: {self.__dni}, Edad: {self.__edad}, Nombre: {self.__apellido_nombre}"
    

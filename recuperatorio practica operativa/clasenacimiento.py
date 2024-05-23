# DNI de la mamá, tipo de parto (´N´- normal o ‘C’ – cesárea), Fecha y hora del nacimiento, peso (en kg) y altura del bebé (en cm).
class nacimiento:
    __dni_madre:str
    __tipodeparto:str
    __fecha:str
    __hora:str
    __peso:str
    __altura:int

    def __init__(self,dni,tipo_parto,fecha,hora,peso,altura):
        self.__dni_madre=dni 
        self.__tipodeparto=tipo_parto 
        self.__fecha=fecha
        self.__hora=hora
        self.__peso=peso 
        self.__altura=altura 
    def __eq__(self, other):
        return (self.__dni_madre, self.__fecha) == (other.__dni_madre, other.__fecha)
    def get_dni_madre(self):
        return self.__dni_madre
    def get_tipoparto(self):
        return self.__tipodeparto
    def get_fecha(self):
        return self.__fecha
    def get_hora(self):
        return self.__hora
    def get_peso(self):
        return self.__peso
    def get_altura(self):
        return self.__altura
    
    def __str__(self):
        return f"Dni de la madre {self.__dni_madre}, Tipo de parto{self.__tipodeparto}, Fecha:{self.__fecha}, Hora: {self.__hora}, Peso: {self.__peso}, Altura: {self.__altura}"
    

from gestormama import gestormama1
from gestornacimiento import gestornacimiento1

class unmenu:
    def __init__(self):
        self.GM=gestormama1()
        self.GN=gestornacimiento1()
    
    def run(self):
        while True:
            a = input("""MENU DE OPCIONES
                    1 para hacer carga:
                    2 para hacer el item a 
                    3 para hacer el item b
                    4 para salir
                        """)
            if a == '1':
                self.GM.inicializar()
                self.GN.inicializar()
                self.GN.mostrar_lista()
                self.GM.mostrar_arreglo()
            elif a =='2':
                incisoa=self.GN.datos(self.GM)
                print (incisoa)
            elif a =='3':
                self.GN.mostrar_partos_multiples(self.GM)    
            elif a =='4':
                break


            
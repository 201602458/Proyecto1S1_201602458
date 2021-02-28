import carga
import re
class Proceso:

    lista = []
    def __init__ (self, nombre):
        self.nombre=nombre
        self.archivo = carga.Carga_archivo.contenido


    def verificar(self):
        try:
           
            if (self.archivo.isspace() or len(self.archivo) <= 1):
                print("Error de archivo")
            else:
                print("Ejecutandose...")
                self.separar()
        except:
            print("Error de procesamiento")
        
    def separar(self):
        try:
            self.lista = re.split('<|>|=|'+chr(32)+'|'+chr(9)+'|'+chr(34)+'|\n|""',self.archivo) 
            print(self.lista)

            

        except:
            print("Error")

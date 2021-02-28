import proceso
import re
from array import *
class Carga_archivo:

    contenido = ""

    def __init__ (self,link):
        self.link=link 
        self.cont="" 
        #self.matriz = []    
        
        
    def cargar(self):
        try:       
            archivo = open(self.link, 'r')           
            Carga_archivo.contenido=archivo.read()
            #for x in range(0, len(lista)):
             #   print(lista[x])

            print("Archivo cargado satisfactoriamente")
            #proceso.Proceso(contenido)   
                    
        except:
            print("Ruta invalida")

    

   
    
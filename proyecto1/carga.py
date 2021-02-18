import proceso
class Carga_archivo:

    def __init__ (self,link):
        self.link=link

    def carga(self):
        try:       
            archivo = open(self.link, 'r')
            contenido = archivo.read()
            proceso.Proceso(contenido)           
        except:
            print("Ruta invalida")       

   
    
import carga
import proceso
import os.path
class Index:
    opcion="1"

    def __init__ (self, opcion):
        self.opcion=opcion

def main():

        menu='''Menu Principal:
        1.- Cargar Archivos
        2.- Procesar Archivo
        3.- Escribir Archivo Salida
        4.- Mostrar Datos Del Estudiante
        5.- Mostrar Grafica
        6.- Salir'''

        while True:
            print(menu)
            op=input("Ingrese una opcion: ")
            if op == '1':               
                rt=input("Ingrese la ruta del archivo: ")
                ext=os.path.splitext(rt)
                
                if ext[1]==".xml":
                    var=carga.Carga_archivo(rt)
                    var.cargar()                   
                else:
                    print("Archivo incorrecto")

            elif op == '2':
                rt=input("Ingrese el nombre de la matriz a operar... : ")
                var2=proceso.Proceso(rt)
                var2.verificar()
                          
            elif op == '3':
                print("op 3")
            elif op == '4':
                print("op 4")
            elif op == '5':
                print("op 5")
            elif op == '6':
                break
            else:
                print("Opcion Invalida")
                #break

if __name__ == "__main__":
    main()

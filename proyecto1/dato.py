class nodo_dato:

    def __init__(self, x, y, dato):
        self.dato=dato
        self.binario=0
        self.x=x
        self.y=y
        self.x_anterior=None
        self.x_siguiente=None
        self.y_arriba=None
        self.y_abajo=None

import lista
import proceso
class matriz_dato:
    var=""
    def __init__(self, m, n, nombre):
        
        self.inicio = nodo_dato( m, n, nombre)
        

    def crear(self, fila, columna):
        i=0
        j=0
        aux_x=self.inicio
        aux_y=self.inicio
        while i <= fila+1:            
            nuevo = nodo_dato(i, 0, 0)
            aux_x.x_siguiente=nuevo
            nuevo.x_anterior=aux_x
            aux_x=nuevo
            i=i+1

        while j <= columna+1:           
            nuevo = nodo_dato(0, j, 0)
            aux_y.y_abajo=nuevo
            nuevo.y_arriba=aux_y
            aux_y=nuevo
            j=j+1
        #### rellena
        i=1
        j=1
        
        aux_x=self.inicio.x_siguiente
        aux_y=self.inicio.y_abajo
        temp=aux_y         
        while i<= fila:            
            while j<= columna+1:
                nuevo = nodo_dato(i, j, "*")
                aux_x=self.verificar(aux_x)              
                aux_y.x_siguiente=nuevo
                nuevo.x_anterior=aux_y
                
                aux_x.y_abajo=nuevo
                nuevo.y_arriba=aux_x
                
                aux_y=nuevo
                aux_x=aux_x.x_siguiente
                
                j=j+1
            #while fin j
            temp=temp.y_abajo
            aux_y=temp
            aux_x=self.inicio.x_siguiente
            i=i+1
            j=1
            
        #fin I
        
        

    def verificar(self, nodo):
        regreso=nodo        
        while regreso.y_abajo != None:
            regreso=regreso.y_abajo        
        return regreso

    def verificar2(self, nodo):
        regreso=nodo
        while regreso.x_siguiente != None:
            regreso=regreso.x_siguiente
        return regreso

#whilee
    def recorrer(self):
        temporal=self.inicio.y_abajo
        aux=temporal.x_siguiente

        while temporal.y_abajo != None:
            while aux.x_siguiente != None:
                print(aux.x)
                print(aux.y)
                print(aux.dato)
                print(aux.binario)

                aux=aux.x_siguiente
            temporal=temporal.y_abajo
            aux=temporal.x_siguiente



    def reemplazo(self, i, j, dato):       
        temporal=self.inicio.y_abajo
        aux=temporal.x_siguiente

        while temporal.y_abajo != None:
            while aux.x_siguiente != None:
                
                if i == str(aux.x) and j == str(aux.y):
                    aux.dato=dato 
                    if int(aux.dato) > 0:
                        aux.binario=1
                    else:
                        aux.binario=0
                
                    
                aux=aux.x_siguiente
            temporal=temporal.y_abajo
            aux=temporal.x_siguiente

    def sumatoria(self):
        temporal=self.inicio.y_abajo
        aux=temporal.x_siguiente
        cadena_n=""
        cadena_b=""
        lista_n=[]
        lista_b=[]

        while temporal.y_abajo != None:
            while aux.x_siguiente != None:
                
                cadena_n=cadena_n+str(aux.dato)+'-'
                cadena_b=cadena_b+str(aux.binario)+'-'               
                    
                aux=aux.x_siguiente
            lista_n.append(cadena_n)
            lista_b.append(cadena_b)
            cadena_n=""
            cadena_b=""
            temporal=temporal.y_abajo
            aux=temporal.x_siguiente

        #print(lista_n)
        #print(lista_b)
        var =proceso.Proceso()
        var.sumatoria(lista_n,lista_b)
        


    def graficar(self):
        texto='''digraph g {\n
        node [shape = doublecircle, color=blue]; m, n;\n
        node [shape = circle, color=black]; \n        
        '''       
                  
        temporal=self.inicio    
        nombre=temporal.dato   
        tex='m[label="m='+str(temporal.x)+'"]'+'\n'+'n[label="n='+str(temporal.y)+'"]'+'\n'
        tex=tex+nombre+"->m;"+'\n'
        tex=tex+nombre+"->n;"+'\n'
        texto=texto+tex+"matriz->"+nombre

        temporal=self.inicio.x_siguiente       
        aux=temporal.y_abajo

        while temporal.x_siguiente !=None:
            if aux != None:
                if str(aux.dato)=="*":
                    break 
                raiz=str(aux.x)+str(aux.y)
                texto=texto+'->'+raiz+'\n'   
                      
            while aux != None:

                raiz=str(aux.x)+str(aux.y)
                texto=texto+str(raiz)
                texto=texto+'[label="'+str(aux.dato)+'"] ;'+'\n'
                aux=aux.y_abajo
                if aux == None:
                    texto=texto+nombre
                else:
                    receptor=str(aux.x)+str(aux.y)
                    texto=texto+str(receptor)
                    texto=texto+'[label="'+str(aux.dato)+'"] ;'+'\n'
                    texto=texto+raiz+"->"+receptor+";"+'\n'



            temporal=temporal.x_siguiente
            aux=temporal.y_abajo

        texto=texto+"}"

        self.var=lista.matriz_dato("nombre","texto")
        self.var.crear(nombre,texto)
        self.var.revisar()

    def buscar (self, nombre):
        self.var.buscar(nombre)

        



                


    
        
        
class nodo_dato:

    def __init__(self, dato, x, y):
        self.dato=dato
        self.x=x
        self.y=y
        self.x_anterior=None
        self.x_siguiente=None
        self.y_arriba=None
        self.y_abajo=None

class matriz_dato:
    def __init__(self, nombre, m, n):
        
        self.inicio = nodo_dato(nombre, n, m)
        self.lleno=0

    def crear(self, fila, columna):
        i=0
        j=0
        aux_x=self.inicio
        aux_y=self.inicio
        while i <= fila:
            nuevo = nodo_dato(i, 0, 0)
            aux_x.x_siguiente=nuevo
            nuevo.x_anterior=aux_x
            aux_x=nuevo
            i=i+1

        while j <= columna:
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

            while j<= columna:
                nuevo = nodo_dato(i, j, 0)
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
        #fin I
        

        
        
    def verificar(self, nodo):
        regreso=nodo
        while regreso != None:
            regreso=regreso.y_abajo
        return regreso

#whilee
    def recorrer(self):
                

        



    '''def insertar(self, dato, px, py):

        nuevo = nodo_dato(dato,px,py)

        # si es el primer dato que se incerta
        if self.lleno==0:
            self.primerox=nuevo
            self.primeroy=nuevo
            self.ultimox=nuevo
            self.ultimoy=nuevo
            
            self.lleno=self.lleno+1

        #si es el segundo dato que se incerta 
        elif self.lleno>0:
            self.aux_x=self.primerox
            self.aux_y=self.primeroy            
            
            #en x
            while True:

                #si x nuevo es igual a x auxiliar
                if nuevo.x == self.aux_x.x:
                    #agregar despues                    
                    break

                # si x nuevo es mayor a x auxiliar
                elif nuevo.x > self.aux_x.x:
                    self.aux_x=self.aux_x.siguientex
                    
                elif nuevo.x < self.aux_x.x:
                    self.aux_x=self.aux_x.anteriorx
            
            #en y
            while True:

                if nuevo.y = self.aux_y.y:
                    #agregar despues
                    # darle break
                elif nuevo.y > self.aux_y.y:
                    #cambiar aux al siguiente
                elif nuevo.y < self.aux_y.y:
                    #cambiar a anterior'''
            
            

            



import carga
import re
import dato
class Proceso:

    lista = []
    lista2=[]
    var=""
    cadena=""
    nombre=""
    def __init__ (self):
        
        self.archivo = carga.Carga_archivo.contenido


    def verificar(self):
        #try:
           
            if (self.archivo.isspace() or len(self.archivo) <= 1):
                print("Error de archivo")
            else:
                print("Ejecutandose...")
                self.separar()
        #except:
            #print("Error de procesamiento")
        
    def separar(self):
       # try:
            self.lista = re.split('<|>|=|'+chr(32)+'|'+chr(9)+'|'+chr(34)+'|\n|""',self.archivo) 
           
            conta=0
            for i in range(0, len(self.lista)):

                #con el matriz
                if self.lista[i]=="nombre":
                    if conta >= 1:
                        print("se repetira el ciclo de enviar la matriz//// aqui ma todo")
                    else:
                        print("primera vez que entra///")
                    nombre=self.lista[i+2] 
                    conta=conta+1 
                if self.lista[i]=="n":
                    n=int(self.lista[i+1])   
                if self.lista[i]=="m":
                    m=int(self.lista[i+1])      
                    self.var = dato.matriz_dato(n,m,nombre)
                    self.var.crear(n,m)
                    #var.recorrer()   

                if self.lista[i]=="x":
                    x=self.lista[i+1]
                if self.lista[i]=="y":
                    y=self.lista[i+1]
                if self.lista[i] == "/dato":
                    datos=self.lista[i-1]
                    self.var.reemplazo(x,y,datos)

            self.var.sumatoria()
            self.var.graficar()

    def sumatoria(self, m_n, m_b):
        #print(m_n)
        c1=0
        c2=c1+1
        i=len(m_b)-1
        j=len(m_b)-1
        
        while c1 <= i:
            #print(i)
            while c2 <= j:
                #print(m_n)

               # print(j)
                if m_b[c1]==m_b[c2]:
                    m_n[c1]=self.sum(m_n[c1],m_n[c2])
                    #print(self.sum(m_n[i],m_n[j]))
                    m_n.pop(c2)
                    m_b.pop(c2)

                j=len(m_b)-1
                i=len(m_b)-1
                c2=c2+1


            c1=c1+1 
            c2=c1+1
        #print(m_n)
        self.texto(m_n)
    
    def sum(self, m_1, m_2):       
        #total=0
        cadena=""
        l1 = re.split("-",m_1)
        l2 = re.split("-",m_2)
        
        for i in range(0, len(l1)-1):
            total=int(l1[i])+int(l2[i])
            cadena=cadena+str(total)+"-"
            #print(cadena)
        return cadena


    def buscar(self, nombre):
        self.var.buscar(nombre)
        self.nombre=nombre



    def texto(self, m_n):
        Proceso.cadena='<matriz nombre="'+self.nombre+'_Salida">\n'
        #print(m_n)

        for i in range(0, len(m_n)):
            l1 = re.split("-",m_n[i])
                
            for j in range(0, len(l1)-1):
                Proceso.cadena=Proceso.cadena+'<dato x='+str(i+1)+' y='+str(j+1)+'>'+str(l1[j])+'</dato>\n'
        
        Proceso.cadena=Proceso.cadena+'</matriz>'
        #print(self.cadena)

    def salida(self, ruta):
        file=open(ruta,"w")
        file.write(Proceso.cadena)
        file.close()


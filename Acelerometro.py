#*-*coding:utf-8 *-*
#qpy:kivy
import kivy 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
#from kivy.config import Config 
from kivy.uix.relativelayout import RelativeLayout
#import random
from kivy.clock import Clock, mainthread
from jnius import autoclass
import ast

class Acelerometro:

    def Disparador(self,*args):
          self.Acelerometro_on()
          self.Acelerometro_leer()
          return xf, y, zf


#___________VERIFICAR HARDWARE__________________
    def Hardware(self, *args):
        global Hardware

        try:
            Hardware = autoclass('org.renpy.android.Hardware')
            if True:
                #lbl1.text = "Si detecta el harware"
                print "si detecta el HARDWARE"
                #               lanzador1 = Clock.schedule_interval(self.Disparador, 0.1)	
                #                lanzador
                return True
            

        except:
        #    lbl1.text = "no soporta el hardware"
            print "No soporta el Hardware"
#            exit()
             return False

    # convierte una cadena string de numeros a float
    def Convertir_float(self, Valor):
         nodo1 = ast.parse(Valor, mode='eval')
         VAR1 = eval(compile(nodo1, '<string>', mode='eval'))
         return VAR1


    def Acelerometro_on(self):
        Encender = Hardware.accelerometerEnable(True) 
        pass

    def Acelerometro_off(self):
        global Apagar 
        Apagar = Hardware.accelerometerEnable(False) 
        pass

    def Acelerometro_leer(self):
        global Lectura 
        Lectura = Hardware.accelerometerReading()
        self.Lectura()

    def Verifica_espacios(self, cadena):
        Cadena = []
        pos_finalC = ""
        pos_inicialC = -1
        try:
            while True:
                pos_inicialC = cadena.index(' ', pos_inicialC+1)
                Cadena.append(pos_inicialC)
                
        except ValueError: 
            print 'Posiciones de la letra " " en la cadena 1:', Cadena
            for i in range(len(cadena)):
                ac_sex = cadena
                if ac_sex[i] == " ":
                    print "aca voy"
        
                else:
                    pos_finalC += ac_sex[i]

        rpt = pos_finalC
        print rpt
        return rpt


    #_______________ PROPIEDADES FUNCIONES ________________
    
    def Lectura(self):
        global x1 
        global y 
        global z1 
        global xf
        global zf
        leer = list()
        leer.append(Lectura)
        leer2= str(leer)
        separa = leer2.split(",")
        x1 = separa[0]
        y =  separa[1]
        z1 = separa[2]
        #LLamo a las funciones aceleracion y las asigno a una variable 

        xl = self.Corregir_x()
        print "xl", xl
        zl = self.Corregir_z()
        print "zl", zl
        xa = self.Convertir_float(xl)
        print "convirtio xa"
        print "y = " , y
        xf = round(xa,3)
    
        print "x = ", xf
        print "y = ", y   
        
	ys = self.Verifica_espacios(y)
        print "convirtio y a string ", ys
        y = self.Convertir_float(ys)
        print "convirtio yf a float ",round(y,3)
        print "y = ", round(y, 3)
        y=round(y,3)
        zs = self.Verifica_espacios(zl)
        print "convirtio zf a string ",zs
        zf= self.Convertir_float(zs)
        print "convirtio zf a float ", round(zf, 3)
        print "z = ", round(zf, 3)
        zf=round(zf,3)    
        print "x = ", xf
        print "y = ", y
        print "z = ", zf
        #        Vector_r = xf + " " + uy
        
        Vector_aceleracion = str(xf) + " \n " + str(y) + "\n" + str(zf)
        #        lbl1.text = str(pos_final)
        #     lbl1.text = str(Vector_aceleracion)        
        print "este es el vector aceleracion: ", Vector_aceleracion
        





# quita los simbolos [ y convierte a un string de numeros 
    def Corregir_x(self):
        lista0 = []
        pos_finalx = ""
        pos_inicialx = -1
        try:
            while True:
                pos_inicialx = x1.index('[', pos_inicialx+1)
                lista0.append(pos_inicialx)
                
        except ValueError: 
            print 'Posiciones de la letra "[" en la cadena 1:', lista0
            for i in range(len(x1)):
                ac_sex = x1
                if ac_sex[i] == "[":
                    print "aca voy"
        
                else:
                    pos_finalx += ac_sex[i]

        xf = pos_finalx
        return xf


# quita los simbolos ] y convierte a un string de numeros 
    def Corregir_z(self):
        lista1 = []
        pos_finalz = ""
        pos_inicialz = -1
        try:
            while True:
                pos_inicialz = z1.index(']', pos_inicialz+1)
                lista1.append(pos_inicialz)
                
        except ValueError: 
            print 'Posiciones de la letra "]" en la cadena 3:', lista1
            for i in range(len(z1)):
                ac_sez = z1
                if ac_sez[i] == "]":
                    print "aca voy"
                    
                else:
                    pos_finalz += ac_sez[i]    

        zf = pos_finalz
        return zf

    def __init__(self):
        if (self.Hardware() is True):
            print self.Disparador()
        else: 
            print False
           
#esto = Acelerometro()
#esto.Disparador()



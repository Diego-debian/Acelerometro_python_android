#*-*coding:utf-8 *-*
#qpy:kivy
#kivy.require('1.4.0')

from Acelerometro import * 
import kivy 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config 
from kivy.uix.camera import Camera
from kivy.uix.relativelayout import RelativeLayout
import random
from kivy.clock import Clock, mainthread
from kivy.uix.image import Image
from jnius import autoclass

#Config.set("graphics", "width", "700") #ancho
#Config.set("graphics", "height", "480") #Alto

class Camara_acelerometro(App):

    def Accion1(self):
        self.acx = 0
        self.acy = 0
        self.acz = 0
        self.opcionRAT=0
        global maquina
        global acx, acy, acz
        try:
            maquina = Acelerometro()
            if (maquina.Hardware() == True):
                HILO1 = Clock.schedule_interval(self.Accion2, 0.3)
                HILO2 = Clock.schedule_interval(self.ordena, 0.3)

                
            else:
                print "No es COMPATIBLE"
        except:
            print "NO DETECTADO !!!"
            pass

    def Accion2(self, *args):
        
        print "Acelerometro encontrado"
        print "Empezando la captura"
        acx, acy, acz = maquina.Disparador()
        print "aceleracion en x", acx
        print "aceleracion en y", acy
        print "aceleracion en z", acz
        self.acx = acx
        self.acy = acy
        self.acz = acz
        Vector_aceleracion = "Aceleracion en x: " + str(acx) + "\nAceleracion en y: " + str(acy) + "\nAceleracion en z: " + str(acz) 
        #lbl1.text =  Vector_aceleracion



    def Label1(self):
        global lbl1
        lbl1 = Label()
     #   lbl1.text = "Esperando instrucciones para seguir ..."
        lbl1.pos = 300, 100
        self.WIDGET1.add_widget(lbl1)


    def Camara(self):
        camwidget = Widget()  #Create a camera Widget
        cam = Camera()        #Get the camera
        cam.resolution=(640,480)
        cam.size= 1000,800
        cam.pos=(-100,-100)

        cam.play=True         #Start the camera

        camwidget.add_widget(cam) 
        self.WIDGET1.add_widget(camwidget) 


 
    def ordena(self, *args):     
        if (self.opcionRAT==1):
            self.imagenwidget.remove_widget(self.Anim)  
            self.WIDGET1.remove_widget(self.imagenwidget)
            self.opcionRAT =0
            

        if self.opcionRAT == 0:
            self.Animacion1()
            self.opcionRAT = 1
            

    def Animacion1(self, *args):
        global Anim
        global imagenwidget
        self.imagenwidget = Widget()
        self.Anim = Image()
        self.Anim.source = "img/caballo.zip"
        self.Anim.anim_delay=(0.15)
    #    Anim.pos_hint= {"x": -0.1, "center_y": -1}
#        self.Anim.pos = self.escalaA(self.acx), self.escalaB(self.acy)
        self.Anim.pos = self.escalaA(self.acx), 80

   #     Anim.pos = 200, 400

        self.imagenwidget.add_widget(self.Anim)  
        self.WIDGET1.add_widget(self.imagenwidget)

    def escalaA(self, a):
        if (a >= -10)&(a <= 10):
            X = 35*a + 350
            return X
        
        X = 0
        return X

    def escalaB(self, b):
        if (b >= -10)&(b <= 10):
            Y = 35*b + 240
            return Y
        Y = 0 
        return Y


    def build(self): 
        self.WIDGET1 = Widget() 
        self.Camara()
        self.Label1()
        self.Accion1()
#        self.Animacion1()
        return self.WIDGET1
        
if __name__ == '__main__':
    Camara_acelerometro().run()


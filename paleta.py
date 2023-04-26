import kivy
from tkinter.messagebox import showinfo
from kivy import *
kivy.require("1.9.1")
from kivy.app import *
from kivy.core.window import *
from kivy.uix.button import *
from kivy.uix.relativelayout import *
from kivy.uix.gridlayout import *
from kivy.config import *
from kivy.uix.textinput import *
from kivy.uix.label import *
from kivy.uix import *
from kivy.properties import ObjectProperty, StringProperty
from funcoes import *

Window.size = (900, 900)
pincel = ''

class RootWidget(RelativeLayout):
    def gerar(self):
        self.paleta1.background_color=(0,0,0) 
        self.paleta2.background_color=cores_aleatorias()
        self.paleta3.background_color=cores_aleatorias()
        self.paleta4.background_color=cores_aleatorias()

    def selecionar1(self):
        global pincel
        self.fundo1.background_color = (1,0,0)
        pincel = self.paleta1.background_color
        self.fundo2.background_color = (0,0,0)
        self.fundo3.background_color = (0,0,0)
        self.fundo4.background_color = (0,0,0)

    def selecionar2(self):
        global pincel
        self.fundo2.background_color = (1,0,0)
        pincel = self.paleta2.background_color
        self.fundo1.background_color = (0,0,0)
        self.fundo3.background_color = (0,0,0)
        self.fundo4.background_color = (0,0,0)

    def selecionar3(self):
        global pincel
        self.fundo3.background_color = (1,0,0)
        pincel = self.paleta3.background_color
        self.fundo2.background_color = (0,0,0)
        self.fundo1.background_color = (0,0,0)
        self.fundo4.background_color = (0,0,0)

    def selecionar4(self):
        global pincel
        self.fundo4.background_color = (1,0,0)
        pincel = self.paleta4.background_color
        self.fundo2.background_color = (0,0,0)
        self.fundo3.background_color = (0,0,0)
        self.fundo1.background_color = (0,0,0)            

    def pintar(self,a):
        a.background_color = pincel

    def resetar(self):
        self.fundo1.background_color = (0,0,0)
        self.fundo2.background_color = (0,0,0)
        self.fundo3.background_color = (0,0,0)
        self.fundo4.background_color = (0,0,0)

        self.paleta1.background_color = (1,1,1)
        self.paleta2.background_color = (1,1,1)
        self.paleta3.background_color = (1,1,1)
        self.paleta4.background_color = (1,1,1)

        self.quadro1.background_color = (1,1,1)
        self.quadro2.background_color = (1,1,1)
        self.quadro3.background_color = (1,1,1)
        self.quadro4.background_color = (1,1,1)
        self.quadro5.background_color = (1,1,1)

        self.quadro6.background_color = (1,1,1)
        self.quadro7.background_color = (1,1,1)
        self.quadro8.background_color = (1,1,1)
        self.quadro9.background_color = (1,1,1)
        self.quadro10.background_color = (1,1,1)

        self.quadro11.background_color = (1,1,1)
        self.quadro12.background_color = (1,1,1)
        self.quadro13.background_color = (1,1,1)
        self.quadro14.background_color = (1,1,1)
        self.quadro15.background_color = (1,1,1)

        self.quadro16.background_color = (1,1,1)
        self.quadro17.background_color = (1,1,1)
        self.quadro18.background_color = (1,1,1)
        self.quadro19.background_color = (1,1,1)
        self.quadro20.background_color = (1,1,1)

        self.quadro21.background_color = (1,1,1)
        self.quadro22.background_color = (1,1,1)
        self.quadro23.background_color = (1,1,1)
        self.quadro24.background_color = (1,1,1)
        self.quadro25.background_color = (1,1,1)

class PaletadeCores2App(App): 

    def build(self):
        return RootWidget()

myApp = PaletadeCores2App()
myApp.run()
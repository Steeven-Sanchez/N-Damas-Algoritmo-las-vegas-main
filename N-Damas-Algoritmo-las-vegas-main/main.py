import pygame,sys
from pygame.locals import *
from random import randint
from numpy import *
from collections import *
from tkinter import *
from tkinter import ttk, font
import getpass
from maestrovegas import*
from interfaz import*
from time import time


pygame.init()
#gargar una imagenes:
tablero_ajedrez=pygame.image.load("15x15.png")
reina=pygame.image.load("r.png")





          

#_______________MAIN___________________________
ins_logica = Logica
ins_interfaz= Interfaz
boleano = ins_interfaz.menu()



#NOTA:
#se mostrara por pantalla la matriz final resualta de manare exitosa.
#se mostrara por Giu el tablero suelto con sus damas de manera exitosa.
#
# SI desea ver el procedimiento de paso a paso como coloca las damas y se reinicia,
# entonces ir  a maestroVegas.py y descomentar el recuadro que se lee  ***VER***
#esto solo si desea ver graficamente o matricialmente el procedimiento , tambien leer las ultimas
#lineas de esa clase...

if boleano :
    
    n = ins_interfaz.get_tamaño()
    window=pygame.display.set_mode ((n*40,n*40))
    
    tiempo_inicial = time () 
    guarde_damas= ins_logica.valida_horizontal_vertical(n,n,True)
    tiempo_final = time()
    
    print ("Tiempo que tardo en resolver :3  ->", tiempo_final-tiempo_inicial, "  segundos" )
    ins_interfaz.muestre_tablero(n,guarde_damas,window,True)


        

  

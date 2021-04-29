import pygame,sys
from pygame.locals import *
from random import randint
from numpy import *
from collections import *
from tkinter import *
from tkinter import ttk, font
import getpass


#gargar una imagenes:
tablero_ajedrez=pygame.image.load("15x15.png")
reina=pygame.image.load("r.png")



class Interfaz :
  n=0
  
  
  def get_tamaño ():
     global n
     
     return n 
  
  def menu ():
       global n 
       
      #_________________________________________________________________________________________________
       def cuatro ():
            global n
            n =4
            menu.destroy ()
       def cinco ():
            global n
            n =5
            menu.destroy ()
       def seis ():
            global n
            n =6
            menu.destroy ()
       def ocho ():
            global n
            n =8
            menu.destroy ()    
       def diez ():
            global n
            n =10
            menu.destroy ()
       def doce ():
            global n
            n =12
            menu.destroy ()
       def quince ():
            global n
            n =15
            menu.destroy ()      

      #_________________________________________________________________________________________________     
       menu=Tk ()
       menu.geometry ( "400x300" )
       menu.title("bienvenido")

       
       Label (menu ,text= "Problema de damas",fg='white',bg='brown',relief='solid',font= ( "arial",15,"bold") ).place(x=110, y=10 )
       Label (menu ,text= "seleccione el tamaño del tablero ",font= ( "arial",10,"bold") ).place(x=100, y=50 )

       Button (menu , text= "4", width=5 , bg='brown', fg ='white', command= cuatro).place(x=140,y=100)
       Button (menu , text= "5", width=5 , bg='brown', fg ='white', command= cinco).place(x=190,y=100)
       Button (menu , text= "6", width=5 , bg='brown', fg ='white', command= seis).place(x=240,y=100)
       Button (menu , text= "8", width=5 , bg='brown', fg ='white', command= ocho).place(x=140,y=130)
       Button (menu , text= "10", width=5 , bg='brown', fg ='white', command= diez).place(x=190,y=130)
       Button (menu , text= "12", width=5 , bg='brown', fg ='white', command= doce).place(x=240,y=130)
       Button (menu , text= "15", width=5 , bg='brown', fg ='white', command= quince).place(x=190,y=160)
       
       
       salir= Button (menu , text= "salir ", width=12 , bg='brown', fg ='white', command= exit ).place(x=280,y=250)
       print (cuatro )


       menu .mainloop()
       return True

      
      
  def pinte_damas (n,guarde_damas,window,boleano):
        
        i = 0
        #para disminuir la velocidad de ejecucion
        reloj = pygame.time.Clock()
        while (n>0) :
          if boleano :
             reloj.tick(30)
          window.blit(reina,(i*40,(guarde_damas[i]*40)))
          i+=1
          n-=1
          
          
  def muestre_tablero (n,guarde_damas,window,boleano) :
    
    pygame.init()
    
    
    #while True :
        

        #pinta imagen de tablero ajedrez
    window.blit(tablero_ajedrez,(0,0))
        
    Interfaz.pinte_damas (n ,guarde_damas,window,boleano)
        
        
    #for evento in pygame.event.get():

                  #si pulsan la X
     #          if evento.type == QUIT :
      #               pygame.quit()
       #              sys.exit()
                 
    pygame.display.update()


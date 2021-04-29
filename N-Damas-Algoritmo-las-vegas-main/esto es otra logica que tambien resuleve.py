import pygame,sys
from pygame.locals import *
from random import randint
from numpy import *
from collections import *
from tkinter import *
from tkinter import ttk, font
import getpass


class Logica :

      
      guarde_damas = []
      matriz = ()
      dama_puestas=0
      
      def valida_horizontal_vertical ( fila,columna):
            

            global matriz
            global guarde_damas
            #global dama_puestas
            
            fila,columna = int(fila), int(columna)
            #llenar tablero de ceros
            matriz= zeros ( ( fila,columna ))
            #para saber si ya estaran todas las reinas puestas
            
            
            global guarde_damas

            guarde_damas= [99]*fila
            
            j=0       
            while (j < fila):
              i=0   
              while (i <  columna):
                #validar que las reinas no se crucen...
                #...horizontal o verticalmente
                donde=randint(0,fila-1)
               
                if guarde_damas[donde]==99 :
                     #reemplaze por su valor en la posicion i
                     #esto para saber que filas ya tinen dama
                     guarde_damas[donde]=i
                     matriz [i] [donde] =5
                     i+=1
                     #damas_puestas+=1 
                 
              j+=11
              
      
            
            
            #print (damas_puestas )
            
            return guarde_damas 
      ##________________________________________
          
      def valide_diagonales (fila,columna):
        
        global matriz
        global guarde_damas
        
        valido = True
        
        j=0
        

        print (guarde_damas)
        print (matriz )
        
        while ( j < fila ):
            i = guarde_damas[j]
            
            #angulo 45°
            k= j 
            
            while (k < columna-1 )and ( i > 0 ):
                print ("i ----  ",i)
                print ("j ----  ",j)
                i-=1
                k+=1
                
                
                if (matriz[i][k]==0 ) :
                  valido = True
                  print ( "entro ", valido )
                
                else:
                  valido= False
                  print (valido)
                  return False
                
            #angulo 135°
            k= j 
            
            while (k > 0)and ( i > 0 ):
                print ("i ----  ",i)
                print ("j ----  ",j)
                i-=1
                k-=1
                
                
                if (matriz[i][k]==0 ) :
                  valido = True
                  print ( "entro ", valido )
                
                else:
                  valido= False
                  print (valido)
                  return False    
                
                
            j+=1
              
          
          
        #guarde_damas = Logica.matriz_con_damas ( fila,columna)
        
        return True
        
      ##________________________________________     
            ##_____________________fin metodo bloques __________________________________##
ins_logica = Logica
ins_logica.valida_horizontal_vertical(5,5)

while not(ins_logica.valide_diagonales (5,5) ) :
  ins_logica.valida_horizontal_vertical(5,5)
  


# Importe de las clases necesarias
from datetime import datetime
from random import randrange
import os
import time
import File as fl
import menu as mn
#Esta es la clase Bitacora
class logBook:
# Crea la bitácora y pone el título
    def iniLogBook():
        if os.path.exists("Bitacora.txt"):
            pass
        else:
            file = open("Bitacora.txt",'a')
            file.write("--------------------REGISTRO GENERAL DE EJECUCIONES--------------------\n\n")
        
#Escribe la hora y fecha actual a la bitacora
    def writeDate():
        file = open("Bitacora.txt",'a')
        file.write(f"fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"+"\r")
        file.close

#Coloca un id a la bitacora
    def putId():
        file = open("Bitacora.txt",'a')
        file.write(f"ID: {randrange(100)}"+"\r")    
        file.close  

#Agrega a la bitacora la ruta del origen de los archivos 
    def sourceCapture():
        file = open("Bitacora.txt",'a')
        originName=os.path.basename(fl.origin)
        file.write(f"Nombre de la Carpeta Origen: {originName}"+"\r")
        file.close

#Agrega a la bitacora la ruta del destino de los archivos
    def sourceDestiny():
        file = open("Bitacora.txt",'a')
        destinyName=os.path.basename(fl.destiny)
        file.write(f"Nombre de la carpeta Destino: {destinyName}"+"\r")
        file.close

#Agrega una lista a la bitacora sobre los archivos copiados 
    def captureCopyfiles(filesListco):
        n=1
        file = open("Bitacora.txt",'a')
        file.write("Archivos copiados: "+"\r")
        for line in filesListco:
            file.write(f"{n}: {line}"+"\r")
            n+=1
        file.write(f"La cantidad de archivos copiados es de: {n-1}"+"\r")
        file.write("------------------------------------------------------------------------------"+"\r")
        file.close

#Agrega una lista a la bitacora sobre los archivos que se movieron 
    def captureMovedfiles(fileListmo):
        n=1
        file = open("Bitacora.txt",'a')
        file.write("Archivos movidos: "+"\r")
        for line in fileListmo:
            file.write(f"{n}: {line}"+"\r")
            n+=1
        file.write(f"La cantidad de archivos movidos es de: {n-1}"+"\r")
        file.write("------------------------------------------------------------------------------"+"\r")
        file.close
        
#Agrega el tiempo programado a la bitacora
    def progratime(seconds):
        file = open("Bitacora.txt",'a')
        file.write(f"Tiempo Programado: {seconds} Segundos"+"\r")
        file.close

#Agrega el titulo del movimiento a la bitacora
    def successMove():
        file = open("Bitacora.txt",'a')
        file.write("MOVIMIENTO REALIZADO CON EXITO"+"\r")
        file.close

#Agrega el titulo del copiado a la bitacora
    def successCopy():
        file = open("Bitacora.txt",'a')
        file.write("COPIADO REALIZADO CON EXITO"+"\r")
        file.close

#Realiza la lectura de la bitacora
    def logReading():
        log = open("Bitacora.txt",'r')
        lisLog = log.readlines()
        for x in lisLog:
            print(x)
        log.close
        time.sleep(5)
        mn.showMenu()
        
#Realiza los llamados de varios metodos de la bitacora para que se ejecuten en orden
    def writeLogbook():
        logBook.putId()
        logBook.writeDate()
        logBook.sourceCapture()
        logBook.sourceDestiny()
        

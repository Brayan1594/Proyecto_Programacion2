# Importe de las clases necesarias
from datetime import datetime
from random import randrange
import File as fl
#Esta es la clase Bitacora
class logBook:
#Escribe la hora y fecha actual a la bitacora
    def writeDate():
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"+"\r")
        archivo.close

#Coloca un id a la bitacora
    def putId():
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"ID: {randrange(20)}"+"\r")    
        archivo.close  

#Agrega a la bitacora la ruta del origen de los archivos 
    def sourceCapture():
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"Origen: {fl.origin}"+"\r")
        archivo.close

#Agrega a la bitacora la ruta del destino de los archivos
    def sourceDestiny():
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"Destino: {fl.destiny}"+"\r")
        archivo.close

#Agrega una lista a la bitacora sobre los archivos copiados 
    def captureCopyfiles(filesListco):
         archivo = open("Bitacora.txt",'a')
         archivo.write(f"Archivos copiados : {filesListco}"+"\r")
         archivo.write("-----------------------------------------------------------------------------"+"\r")
         archivo.close

#Agrega una lista a la bitacora sobre los archivos que se movieron 
    def captureMovedfiles(fileListmo):
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"Archivos movidos: {fileListmo}"+"\r")
        archivo.write("------------------------------------------------------------------------------"+"\r")
        archivo.close

#Agrega el tiempo programado a la bitacora
    def progratime(seconds):
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"Tiempo Programado: {seconds} Segundos"+"\r")
        archivo.close

#Agrega el titulo del movimiento a la bitacora
    def successMove():
        archivo = open("Bitacora.txt",'a')
        archivo.write("MOVIMIENTO REALIZADO CON EXITO"+"\r")
        archivo.close

#Agrega el titulo del copiado a la bitacora
    def successCopy():
        archivo = open("Bitacora.txt",'a')
        archivo.write("COPIADO REALIZADO CON EXITO"+"\r")
        archivo.close

#Realiza la lectura de la bitacora
    def logReading():
        log = open("Bitacora.txt",'r')
        lisLog = log.readlines()
        for x in lisLog:
            print(x)
        log.close
        
#Realiza los llamados de varios metodos de la bitacora para que se ejecuten en orden
    def writeLogbook():
        logBook.putId()
        logBook.writeDate()
        logBook.sourceCapture()
        logBook.sourceDestiny()
        

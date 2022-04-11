# Importe de las clases necesarias
from datetime import datetime
import File as fl
class logBook:
    
    def escribeFecha():
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"+"\r")
        archivo.close

    def poneid():
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"ID: {1}"+"\r")    
        archivo.close  

    def capturaOrigen():
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"Origen: {fl.origin}"+"\r")
        archivo.close

    def capturaDestino():
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"Destino: {fl.destiny}"+"\r")
        archivo.close

    def capturaArchivosco():
         archivo = open("Bitacora.txt",'a')
         archivo.write(f"Archivos copiados : {fl.copyFiles}"+"\r")
         archivo.close

    def capturaArchivosmo(fileList):
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"Archivos movidos: {fileList}"+"\r")
        archivo.write("--------------------------------------------------------------------"+"\r")
        archivo.close

    def TimeMovement(seconds):
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"Tiempo Programado: {seconds} Segundos"+"\r")
        archivo.close

    def llenabita():
        logBook.poneid()
        logBook.escribeFecha()
        logBook.capturaOrigen()
        logBook.capturaDestino()
        

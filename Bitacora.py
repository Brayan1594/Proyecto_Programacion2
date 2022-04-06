from datetime import datetime
import Archivo as ar
class Bitacora:
    
    def escribeFecha():
        archivo = open("Bitacora.txt",'a')
        archivo.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\r")
        archivo.close

    def poneid():
        ar.readFile()
        archivo = open("Bitacora.txt",'a')
        archivo.write("1"+"\r")    
        archivo.close  

    def capturaOrigen():
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"Origen: {ar.origin}"+"\r")
        archivo.close

    def capturaDestino():
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"Destino: {ar.destiny}"+"\r")
        archivo.close

    def capturaArchivosco():
         archivo = open("Bitacora.txt",'a')
         archivo.write(f"Archivos copiados : {ar.copyFiles}"+"\r")
         archivo.close

    def capturaArchivosmo():
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"Archivos movidos: {ar.moveFiles}"+"\r")
        archivo.close

#para hacer pruebas
'''Bitacora.poneid()  
Bitacora.escribeFecha()
Bitacora.capturaOrigen()
Bitacora.capturaDestino()
Bitacora.capturaArchivosco()
Bitacora.capturaArchivosmo()'''
from datetime import datetime
import Archivo as ar
class Bitacora:
    
    def escribeFecha():
        ar.Archivo.lectura()
        archivo = open("Bitacora.txt",'a')
        archivo.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\r")
        archivo.close

    def poneid():
        archivo = open("Bitacora.txt",'a')
        archivo.write("1"+"\r")    
        archivo.close  

    def capturaOrigen():
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"Origen: {ar.origen}"+"\r")
        archivo.close

    def capturaDestino():
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"Destino: {ar.destino}"+"\r")
        archivo.close

    def capturaArchivosco():
         archivo = open("Bitacora.txt",'a')
         archivo.write(f"Archivos copiados : {ar.extension_copia}"+"\r")
         archivo.close

    def capturaArchivosmo():
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"Archivos movidos: {ar.extension_movimiento}"+"\r")
        archivo.close

Bitacora.poneid()  
Bitacora.escribeFecha()
Bitacora.capturaOrigen()
Bitacora.capturaDestino()
Bitacora.capturaArchivosco()
Bitacora.capturaArchivosmo()
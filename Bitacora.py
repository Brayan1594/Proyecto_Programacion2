from datetime import datetime
import File as fl
class Bitacora:
    
    def escribeFecha():
        archivo = open("Bitacora.txt",'a')
        archivo.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\r")
        #archivo.close

    def poneid():
        fl.readFile()
        archivo = open("Bitacora.txt",'a')
        archivo.write("1"+"\r")    
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

    def capturaArchivosmo():
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"Archivos movidos: {fl.moveFiles}"+"\r")
        archivo.close

#para hacer pruebas
'''Bitacora.poneid()  
Bitacora.escribeFecha()
Bitacora.capturaOrigen()
Bitacora.capturaDestino()
Bitacora.capturaArchivosco()
Bitacora.capturaArchivosmo()'''
# Importe de las clases necesarias
from datetime import datetime
import File as fl
class logBook:
    
    def writeDate():
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"+"\r")
        archivo.close

    def putId():
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"ID: {1}"+"\r")    
        archivo.close  

    def sourceCapture():
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"Origen: {fl.origin}"+"\r")
        archivo.close

    def sourceDestiny():
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"Destino: {fl.destiny}"+"\r")
        archivo.close

    def captureCopyfiles(filesListco):
         archivo = open("Bitacora.txt",'a')
         archivo.write(f"Archivos copiados : {filesListco}"+"\r")
         archivo.write("-----------------------------------------------------------------------------"+"\r")
         archivo.close

    def captureMovedfiles(fileListmo):
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"Archivos movidos: {fileListmo}"+"\r")
        archivo.write("------------------------------------------------------------------------------"+"\r")
        archivo.close

    def progratime(seconds):
        archivo = open("Bitacora.txt",'a')
        archivo.write(f"Tiempo Programado: {seconds} Segundos"+"\r")
        archivo.close

    def successMove():
        archivo = open("Bitacora.txt",'a')
        archivo.write("MOVIMIENTO REALIZADO CON EXITO"+"\r")
        archivo.close
    
    def successCopy():
        archivo = open("Bitacora.txt",'a')
        archivo.write("COPIADO REALIZADO CON EXITO"+"\r")
        archivo.close
    
    def writeLogbook():
        logBook.putId()
        logBook.writeDate()
        logBook.sourceCapture()
        logBook.sourceDestiny()
        

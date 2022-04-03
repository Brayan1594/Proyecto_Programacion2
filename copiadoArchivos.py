import shutil
import os
import Archivo as ar
import threading

class copiaArchivo:
    ar.Archivo.lectura()

    def copiadoArchivosfil():
        lista_archivos = os.listdir(ar.origen)
        for linea in lista_archivos:
             if linea.endswith(f".{ar.extension_copia}".split(",")[0]) or linea.endswith(f".{ar.extension_copia}".split(",")[1]):
                shutil.copy(f"{ar.origen}/{linea}",ar.destino)
                
    def copiadoArchivosto():
        lista_archivos = os.listdir(ar.origen)
        for linea in lista_archivos:
             shutil.copy(f"{ar.origen}/{linea}",ar.destino)

    #Metodo para el copiado de archivos por filtro
    def controlTempocop():
        print("Digite el tiempo en que quiere que se copien los archivos")
        segundos = int(input()) 
        tiempo2 = threading.Timer(segundos, copiaArchivo.tiempoco)
        tiempo2.start()

    def tiempoco():
        copiaArchivo.copiadoArchivosfil()
        print("Copiado de archivos con exito")
#para hacer pruebas
#copiaArchivo.controlTempocop()
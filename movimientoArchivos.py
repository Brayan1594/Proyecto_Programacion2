import shutil
import os
import threading
import Archivo as ar

class movimientoArchivos:
    ar.Archivo.lectura()

    def moverArchivosfiltro():
        
        lista_archivos = os.listdir(ar.origin)
        for linea in lista_archivos:
            if linea.endswith(f".{ar.moveFiles}"):
                shutil.move(f"{ar.origin}/{linea}",ar.destiny)

    def moverTodosarchivos():
        lista_archivos = os.listdir(ar.origin)
        for linea in lista_archivos:
             shutil.move(f"{ar.origin}/{linea}",ar.destino)

    #mueve los archivos con el filtro
    def controltimovifil():
        print("Digite el tiempo en que quiere que se muevan los archivos: ")
        segundos = int(input())
        tiempo2 = threading.Timer(segundos, movimientoArchivos.ejecutaMo)
        tiempo2.start()

    #actua en conjunto con el codigo de arriba
    def ejecutaMo():
         movimientoArchivos.moverArchivosfiltro()
         print("Movimiento realizado con exito")

movimientoArchivos.controltimovifil()



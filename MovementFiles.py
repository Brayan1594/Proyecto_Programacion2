# Importe de las clases necesarias
import shutil
import os
import threading
import time
import File as fl 
import menu
import logBook as lb

# Clase de movimiento de archivos
class fileMovement:

# Mueve archivos según filtro
    def moveFilter():
        fl.Archivo.lecturaArchivo()
        fileListmo = []
        print("\nEsta es la lista de archivos movidos: ")
        file_list = os.listdir(fl.origin)
        for x in fl.moveFiles.split(","):
            for line in file_list:
                if line.endswith(f".{x}"):
                    fileListmo.append(line)
                    shutil.move(f"{fl.origin}/{line}",fl.destiny)
                    print(line)
        lb.logBook.writeLogbook()
        lb.logBook.captureMovedfiles(fileListmo)
# Mueve todos los archivos de la ruta dada        
    def moveAll():
        fl.Archivo.lecturaArchivo()
        fileListmo = []
        print("\nEsta es la lista de archivos movidos: ")
        file_list = os.listdir(fl.origin)
        for line in file_list:
            fileListmo.append(line)
            shutil.move(f"{fl.origin}/{line}",fl.destiny)
            print(line)
        lb.logBook.writeLogbook()
        lb.logBook.captureMovedfiles(fileListmo)
# Asigna el tiempo del movimiento del método moveFilter
    def movementTime1():
        print("Digite el tiempo para comenzar el movimiento de archivos: ")
        seconds = int(input())
        time1 = threading.Timer(seconds, fileMovement.runMoveFilter)
        lb.logBook.successMove()
        lb.logBook.progratime(seconds)
        time1.start()

# Asigna el tiempo de ejecución del método "movementTime1"
    def runMoveFilter():
         fileMovement.moveFilter()
         print("\nMOVIMIENTOS REALIZADOS CON EXITO")
         time.sleep(2)
         print("\nPor favor digite la opción que desea realizar: \n")
         menu.showMenu()   

# Asigna el tiempo del movimiento del método moveAll
    def movementTime2():
        print("Digite el tiempo para comenzar el movimiento de archivos: ")
        seconds = int(input())
        lb.logBook.successMove()
        lb.logBook.progratime(seconds)
        time2 = threading.Timer(seconds, fileMovement.runMoveAll)
        time2.start()
       
# Asigna el tiempo de ejecución del método "movementTime2"
    def runMoveAll():
         fileMovement.moveAll()
         print("\nMOVIMIENTOS REALIZADOS CON EXITO")
         time.sleep(2)
         print("\nPor favor digite la opción que desea realizar: \n")
         menu.showMenu()

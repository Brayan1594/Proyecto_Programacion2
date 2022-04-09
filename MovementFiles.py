# Importe de las clases necesarias
import shutil
import os
import threading
import File as fl   

# Clase de movimiento de archivos
class fileMovement:

# Mueve archivos según filtro
    def moveFilter():
        print("\nEsta es la lista de archivos movidos: ")
        file_list = os.listdir(fl.origin)
        for x in fl.moveFiles.split(","):
            for line in file_list:
                if line.endswith(f".{x}"):
                    shutil.move(f"{fl.origin}/{line}",fl.destiny)
                    print(line)

# Mueve todos los archivos de la ruta dada        
    def moveAll():
        print("\nEsta es la lista de archivos movidos: ")
        file_list = os.listdir(fl.origin)
        for line in file_list:
            shutil.move(f"{fl.origin}/{line}",fl.destiny)
            print(line)
    
# Asigna el tiempo del movimiento del método moveFilter
    def movementTime1():
        print("Digite el tiempo para comenzar el movimiento de archivos: ")
        seconds = int(input())
        time1 = threading.Timer(seconds, fileMovement.runMoveFilter)
        time1.start()

# Asigna el tiempo de ejecución del método "movementTime1"
    def runMoveFilter():
         fileMovement.moveFilter()
         print("\nMOVIMIENTOS REALIZADOS CON EXITO")


# Asigna el tiempo del movimiento del método moveAll
    def movementTime2():
        print("Digite el tiempo para comenzar el movimiento de archivos: ")
        seconds = int(input())
        time2 = threading.Timer(seconds, fileMovement.runMoveAll)
        time2.start()

# Asigna el tiempo de ejecución del método "movementTime2"
    def runMoveAll():
         fileMovement.moveAll()
         print("\nMOVIMIENTOS REALIZADOS CON EXITO")

#fileMovement.movementTime1()
#fileMovement.movementTime2()

# Importe de las clases necesarias
import shutil
import os
import time
import threading
import File as fl
import logBook as lb
import menu



# Clase para el copiado de archivos
class CopyFiles:

#Realiza el copiado de archivos por filtro y muestra la lista de archivos copiados
    def copyFilter():
        fileListco = []
        print("\nEsta es la lista de archivos copiados: ")
        file_list = os.listdir(fl.origin)
        for x in fl.copyFiles.split(","):
            for line in file_list:
                if line.endswith(f".{x}"):
                    fileListco.append(line)
                    shutil.copy(f"{fl.origin}/{line}",fl.destiny)
                    print(line)
        lb.logBook.writeLogbook()
        lb.logBook.captureCopyfiles(fileListco)

#Realiza el copiado de todos los archivos
    def copyAll():
        fileListco = []
        print("\nEsta es la lista de archivos copiados: ")
        file_list = os.listdir(fl.origin)
        for line in file_list:
                fileListco.append(line)
                shutil.copy(f"{fl.origin}/{line}",fl.destiny)
                print(line)
        lb.logBook.writeLogbook()
        lb.logBook.captureCopyfiles(fileListco)
           
# Asigna el tiempo de ejecusión del copiado por filtro
    def copyTimefilter():
        print("\nDigite el tiempo para comenzar copiado de archivos")
        seconds = int(input())
        lb.logBook.progratime(seconds) 
        time1 = threading.Timer(seconds, CopyFiles.timeCopyfilter)
        time1.start()

# Ejecuta el método según el tiempo asignado al copiado por filtro
    def timeCopyfilter():
        CopyFiles.copyFilter()
        print("\033[4;32m"+"\nCOPIADO DE ARCHIVOS EXITOSO"+"\033[0m")
        time.sleep(2)
        print("\nPor favor digite la opción que desea realizar: \n")
        menu.showMenu()
# Asigna el tiempo de ejecusión del copiado de todos los archvos
    def copyTimeall():
        print("\nDigite el tiempo para comenzar copiado de archivos")
        seconds = int(input())
        lb.logBook.progratime(seconds) 
        time1 = threading.Timer(seconds, CopyFiles.timeCopyall)
        time1.start()
# # Ejecuta el método según el tiempo asignado al copiado de todos los archivos
    def timeCopyall():
        CopyFiles.copyAll()
        print("\033[4;32m"+"\nCOPIADO DE ARCHIVOS EXITOSO"+"\033[0m")
        time.sleep(2)
        print("\nPor favor digite la opción que desea realizar: \n")
        menu.showMenu()
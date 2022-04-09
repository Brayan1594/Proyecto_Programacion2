# Importe de las clases necesarias
import shutil
import os
import File as fl
import threading

# Clase para el copiado de archivos
class CopyFiles:

#Realiza el copiado de archivos y muestra la lista de archivos copiados
    def iniCopyFiles():
        print("\nEsta es la lista de archivos copiados: ")
        file_list = os.listdir(fl.origin)
        for x in fl.copyFiles.split(","):
            for line in file_list:
                if line.endswith(f".{x}"):
                    shutil.copy(f"{fl.origin}/{line}",fl.destiny)
                    print(line)
                
# Asigna el tiempo de ejecusión del copiado 
    def copyTime():
        print("\nDigite el tiempo para comenzar copiado de archivos")
        seconds = int(input()) 
        time1 = threading.Timer(seconds, CopyFiles.timeCopy)
        time1.start()

# Ejecuta el método según el tiempo asignado
    def timeCopy():
        CopyFiles.iniCopyFiles()
        print("\nCOPIADO DE ARCHIVOS EXITOSO")

#CopyFiles.copyTime()
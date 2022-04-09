import shutil
import os
import File as fl
import threading

class CopyFiles:
    def iniCopyFiles():
        print("\nEsta es la lista de archivos copiados: ")
        file_list = os.listdir(fl.origin)
        for x in fl.copyFiles.split(","):
            for line in file_list:
                if line.endswith(f".{x}"):
                    shutil.copy(f"{fl.origin}/{line}",fl.destiny)
                    print(line)
                
    #Metodo para el copiado de archivos por filtro
    def copyTime():
        print("\nDigite el tiempo para comenzar copiado de archivos")
        seconds = int(input()) 
        time1 = threading.Timer(seconds, CopyFiles.timeCopy)
        time1.start()

    def timeCopy():
        CopyFiles.iniCopyFiles()
        print("\nCOPIADO DE ARCHIVOS EXITOSO")

#CopyFiles.copyTime()
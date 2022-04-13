# Importe de las clases necesarias
import os
from datetime import datetime
import menu
import time
import CreateConfiguration as CC

# Clase para limpieza de batchs
class clearBaths:

# Registra el borrado en la bitácora
    def backupConfig():
        try:
            File = open("ConfiguracionProyecto.txt","r")
            List = File.readlines()
            forCopying = open("Bitacora.txt",'a')
            forCopying.write("----------LIMPIEZA DE CONFIGURACION----------\n")
            forCopying.write("Fecha y hora del movimiento:   ")
            forCopying.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\n")
            forCopying.write("Información borrada\n")
            for x in List:
                forCopying.write(x)
            forCopying.close()
        except BaseException():
            print("----------ERROR DEL SISTEMA----------")

# Restaura la configuración del aplicativo
    def restoreConfig():
        try:
            CC.createFileConfiguration.createFile()
            CC.createFileConfiguration.readFile1()
        except BaseException():
            print("----------ERROR DEL SISTEMA----------")

# Realiza el borrado de batchs
    def clearConfig():
        clearBaths.backupConfig()
        try:
            os.remove("Pruebas.txt")
            print("----------LIMPIEZA DE BATCHS EXITOSA----------\n")
            print("Por favor elija una opción para continuar\n")
            print("1. Restablecer una configuración----")
            print("2. Volver a menú inicial------------")
            while(True):
                option = input()
                if (not(option.isnumeric())): 
                    print("ERORR: La opción proporcionada es incorrecta por favor digite uno de los números del menú") 
                    continue
                x = int(option)
                if x == 1: 
                    clearBaths.restoreConfig()
                    time.sleep(2)
                    menu.startMenu()
                elif x == 2:
                    print("Volviendo al menú principal")
                    time.sleep(2)
                    menu.startMenu()
        except BaseException():
            print("----------ERROR DEL SISTEMA----------")


    


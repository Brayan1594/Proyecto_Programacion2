# Importe de las clases necesarias
from asyncio import sleep
from tkinter import Y
import ClearConfiguration as CL
import MovementFiles as MF
import CopyingFiles as CF
import time

# Muestra el menú
def showMenu():
    print("\033[;34m"+"------------------------------MENU PRINCIPAL------------------------------"+"\n\n\n")
    print("-----------------OPCION 1:   COPIAR ARCHIVOS.--------------------------")
    print("-----------------OPCION 2:   MOVER ARCHIVOS.---------------------------")
    print("-----------------OPCION 3:   LIMPIAR BATCHS.-----------------------------")
    print("-----------------OPCION 4:   CONSULTAR BITACORA.-----------------------------")
    print("-----------------OPCION 5:   SALIR DEL PROGRAMA.--------------------------")
    print("--------------------------------------------------------------------------\n"+"\033[0m")

#Crea el menú principal
def startMenu():
    showMenu()
    try:
        while(True):
            optionMenu = input("Por favor digite la opción que desea realizar: \n")
            if (not(optionMenu.isnumeric())): 
                print("\033[;31m"+"ERORR: "+"\033[0m"+"La opción proporcionada no es un número, por favor digite uno de los números del menú") 
                continue
            x = int(optionMenu)
            if x == 1: 
               print("\n----------INICIO DE LECTURA DE ARCHIVO MADRE----------\n\n")
               time.sleep(1) 
               CF.CopyFiles.copyTime()
            elif x == 2:
               print("\n----------INICIO DE LECTURA DE ARCHIVO MADRE----------\n\n")
               time.sleep(1)
               print("\nElija una opción para continuar con el movimiento de archivos\n")
               print("\033[;34m"+"1. MOVER ARCHIVOS POR FILTRO DE CONFIGURACIÓN-----")
               print("2. MOVER TODOS LOS ARCHIVOS DEL ORIGEN--------\n"+"\033[0m")
               optMov = input()
               y = int(optMov)
               if y == 1:
                    MF.fileMovement.movementTime1()
                    print("Por favor espere")
               elif y == 2:
                    MF.fileMovement.movementTime2()
                    print("Por favor espere")
               else:
                   print("\033[;31m"+"ERORR: "+"\033[0m"+"La opción digitada no existe")
                   startMenu()
            elif x == 3:
                CL.clearBaths.clearConfig()
            elif x == 4:
                exit()
            elif x == 5:
                print("\033[4;33m"+"GRACIAS POR UTILIZAR LA APP"+"\033[0m")
                time.sleep(2)
                exit()
            else:
                print("\033[;31m"+"ERORR: "+"\033[0m"+"La opción digitada no es válida, por favor digite una opción presente en el menú")
    except BaseException():
        print("--------------ERROR DEL SISTEMA---------------")
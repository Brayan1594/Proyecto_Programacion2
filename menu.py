# Importe de las clases necesarias
import time
import os
import ClearConfiguration as CL 
import MovementFiles as MF
import CopyingFiles as CF
import logBook as lb
import File as fl

# Muestra el menú
def showMenu():
    print("\n------------------------------MENU PRINCIPAL------------------------------"+"\n\n")
    print("-----------------OPCION 1:   COPIAR ARCHIVOS.--------------------------------")
    print("-----------------OPCION 2:   MOVER ARCHIVOS.---------------------------------")
    print("-----------------OPCION 3:   LIMPIAR BATCHS.----------------------------------")
    print("-----------------OPCION 4:   CONSULTAR BITACORA.-------------------------------")
    print("-----------------OPCION 5:   SALIR DEL PROGRAMA.-------------------------------")
    
#Crea el menú principal
def startMenu():
    showMenu()
    try:
        while(True):
            optionMenu = input("Por favor digite la opción que desea realizar: \n")
            if (not(optionMenu.isnumeric())): 
                print("ERORR: La opción proporcionada no es un número, por favor digite uno de los números del menú") 
                continue
            x = int(optionMenu)
# Ejecuta las opciones copiar
            if x == 1: 
               print("\n----------INICIO DE LECTURA DE ARCHIVO MADRE----------\n\n")
               time.sleep(1.5) 
               print("\nElija una opción para continuar con el copiado de archivos\n")
               print("1. COPIAR ARCHIVOS POR FILTRO DE CONFIGURACION-----")
               print("2. COPIAR TODOS LOS ARCHIVOS DEL ORIGEN--------\n")
               optCop = input()
               z = int(optCop)
# Menu interno copiado
               if z == 1:
                    CF.CopyFiles.copyTimefilter()
                    print("Por favor espere")
               elif z == 2:
                    CF.CopyFiles.copyTimeall()
                    print("Por favor espere")
               else:
                   print("ERORR: La opción digitada no existe")
                   startMenu()
# Ejecuta las opciones mover
            elif x == 2:
               print("\n----------INICIO DE LECTURA DE ARCHIVO MADRE----------\n\n")
               time.sleep(1.5)
               print("\nElija una opción para continuar con el movimiento de archivos\n")
               print("1. MOVER ARCHIVOS POR FILTRO DE CONFIGURACION-----")
               print("2. MOVER TODOS LOS ARCHIVOS DEL ORIGEN--------\n")
               optMov = input()
               y = int(optMov)
# Menu interno mover
               if y == 1:
                    MF.fileMovement.movementTime1()
                    print("Por favor espere")
               elif y == 2:
                    MF.fileMovement.movementTime2()
                    print("Por favor espere")
               else:
                   print("ERORR: La opción digitada no existe")
                   startMenu()
# Ejecuta opción de borrar baths
            elif x == 3:
                fl.Archivo.lecturaArchivo()
                CL.clearBaths.clearConfig()
# Ejecuta ioción de consultar bitácora
            elif x == 4:
                if os.path.exists('Bitacora.txt'):
                     lb.logBook.logReading()
                else:
                     print("LA BITACORA SE ENCUENTRA VACIA")
# Ejecuta la salida de la app
            elif x == 5:
                print("GRACIAS POR UTILIZAR LA APP")
                time.sleep(2)
                exit()
# Ejecuta la salida del menu
            else:
                print("ERORR: La opción digitada no es válida, por favor digite una opción presente en el menú")
    except BaseException():
        print("--------------ERROR DEL SISTEMA---------------")
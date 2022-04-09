# Importe de las clases necesarias
import os

# Clase que crea la configuración del aplicativo
class createFileConfiguration:

# solicita la configuración al usuario
    def createFile():
        origin = input("Introduzca la ruta origen del  nuevo archivo: \n")
        destiny = input("\nIntroduzca la ruta destino del  nuevo archivo: \n")
        copyFiles = input("\nIntroducca las extenciones que desea copiar: ")
        moveFiles = input("Introducca las extenciones que desea mover: ")
# Crea y escribe el archivo de configuración
        file = open("Pruebas.txt","a")
        file.write("Origin="+origin)
        file.write("\nDestiny="+destiny)
        file.write("\nCopyFiles="+copyFiles)
        file.write("\nMoveFiles="+moveFiles)
        file.close()

# Lee el archivo de configuración
    def readFile1():
        print("\n-----NUEVA CONFIGURACION DEL PROGRAMA-----\n")
        file = open("Pruebas.txt","r")
        list = file.readlines()
        for x in list:
            print(x)
        file.close()

# Importe de las clases necesarias
import os
# Lee el archivo configuración y captura las variables principales
class Archivo:

    def lecturaArchivo():
        global origin
        global destiny
        global copyFiles
        global moveFiles
        File = open("ConfiguracionProyecto.txt",'r')
        List = File.readlines()
        for x in List:
            if (x.split("=")[0].strip() == "Origin"):
                origin = x.split("=")[1].strip()
            elif (x.split("=")[0].strip() == "Destiny"):
                destiny = x.split("=")[1].strip()
            elif (x.split("=")[0].strip() == "CopyFiles"):
                copyFiles = x.split("=")[1].strip()
            elif(x.split("=")[0].strip() == "MoveFiles"):
                moveFiles = x.split("=")[1].strip()         
                File.close()
# Muestra los archivos de la carpeta origen    
    def showOrigin():
        print("Los datos en el archivo de configuración son")
        existingFiles = os.listdir(origin)
        for line in existingFiles:
             print(line)

# Muestra los archivos de la carpeta destino    
    def showDestiny():
        print("Los datos en el archivo de configuración son")
        existingFiles = os.listdir(destiny)
        for line in existingFiles:
            print(line)



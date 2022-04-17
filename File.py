# Importe de las clases necesarias
import os
import menu as mn
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
#Crea la nueva configuracion 
    def newConfiguration():
        newArch = open("ConfiguracionProyecto.txt",'a')
        newArch.write(f"Origin={origin}"+"\r")
        newArch.write(f"Destiny={destiny}"+"\r")
        print("Word=docx  Exel=xlsx  Powerpoint=pptx  Archivo=txt  Imagenes=PNG Archivo comprimido=rar Archivo python=py\n")
        newCopyfiles =input("Introduzca las extensiones para el filtro de copiado separadas de una coma: \n")
        newArch.write(f"CopyFiles={newCopyfiles}"+"\r")
        print("Word=docx  Exel=xlsx  Powerpoint=pptx  Archivo=txt  Imagenes=PNG Archivo comprimido=rar Archivo python=py\n")
        newmoveFiles=input("Introduzca las extensiones para el filtro de movimiento separadas de una coma: \n")
        newArch.write(f"MoveFiles={newmoveFiles}")
        mn.showMenu()
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
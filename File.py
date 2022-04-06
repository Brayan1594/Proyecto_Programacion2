# Importación de las clases necesarias
import os

print("\n----------INICIO DE LECTURA DE ARCHIVO MADRE----------\n\n")

# A partir de acá se lee el archivo configuración y se capturan las instrucciones principales
File = open(r"C:\Users\LUIS\Documents\Prueba Python\Proyecto_Programacion2\Origen\ConfiguracionProyecto.txt","r")
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
# Método para mostrar los archivos de la carpeta origen    
def showOrigin():
    print("Los datos en el archivo de configuración son")
    existingFiles = os.listdir(origin)
    for line in existingFiles:
        print(line)

# Método para mostrar los archivos de la carpeta destino    
def showDestiny():
    print("Los datos en el archivo de configuración son")
    existingFiles = os.listdir(destiny)
    for line in existingFiles:
        print(line)


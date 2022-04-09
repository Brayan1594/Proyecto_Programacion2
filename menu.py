# Importe de las clases necesarias
import ClearConfiguration as CL

# Muestra el menú
def showMenu():
    print("------------------------------MENU PRINCIPAL------------------------------"+"\n\n\n")
    print("-----------------OPCION 1:   MOVER ARCHIVOS.--------------------------")
    print("-----------------OPCION 2:   LIMPIAR BATCHS.---------------------------")
    print("-----------------OPCION 3:   CONSULTAR BITACORA.-----------------------------")
    print("-----------------OPCION 4:   SALIR DEL PROGRAMA.-----------------------------"+"\n\n")
    print("--------------------------------------------------------------------------")

#Crea el menú principal
def startMenu():
    showMenu()
    try:
        while(True):
            optionMenu = input("Por favor digite la opción que desea realizar: ")
            if (not(optionMenu.isnumeric())): 
                print("La opción proporcionada es incorrecta por favor digite uno de los números del menú") 
                continue
            x = int(optionMenu)
            if x == 1: 
               print("\n----------INICIO DE LECTURA DE ARCHIVO MADRE----------\n\n") 
               print("1")
            elif x == 2:
               CL.clearBaths.clearConfig()
            elif x == 3:
                print("3")
            elif x == 4:
                exit()
            else:
                print("La opción digitada no es válida. Por favor digite una opción presente en el menú")
    except BaseException():
        print("--------------ERROR DEL SISTEMA---------------")
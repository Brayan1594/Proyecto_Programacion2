# Importe de las clases necesarias
import menu

# Presentación del aplicativo
def startSalute():
    print("\n\n"+"      -------------------------------------BIENVENIDO A LA APP PROYECTO FINAL-------------------------------------"+"\n\n")
    print("---Desarrolladores---"+"\n")
    print("Cristel González Zapata"+"\n"+"Brayan Alvarez Araya"+"\n"+"Luis Salazar Benavides"+"\n"+"Rafael Rivera Vargas"+"\n\n\n") 

# Crea el menú de saludo
    try:
        while(True):
            print("\033[;34m"+"Opción 1-------CONTINUAR ")
            print("Opción 2-------SALIR\n"+"\033[0m")
            Continuar = input("Por favor digite alguna de las opciones: ")
            if (not(Continuar.isnumeric())): 
                print("\033[;31m"+"ERORR: "+"\033[0m"+"La opción proporcionada es incorrecta, por favor digite uno de los números del menú: "+"\n") 
                continue
            x = int(Continuar)
            if x == 1:
                menu.startMenu()
                break
            elif x == 2:
                exit()
            else:
                print("\033[;31m"+"ERORR: "+"\033[0m"+"La opción digitada no es válida, por favor digite una opción presente en el menú: "+"\n")
    except BaseException():
        print("--------------ERROR DEL SISTEMA---------------")
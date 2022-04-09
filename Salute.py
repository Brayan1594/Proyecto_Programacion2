import menu
def startSalute():
    print("\n\n"+"      -------------------------------------BIENVENIDO A LA APP PROYECTO FINAL-------------------------------------"+"\n\n")
    print("---Desarrolladores---"+"\n")
    print("Cristel González Zapata"+"\n"+"Brayan Alvarez Araya"+"\n"+"Luis Salazar Benavides"+"\n"+"Rafael Rivera Vargas"+"\n\n\n") 
#Creamos el munú de saludo
    try:
        while(True):
            print("Opción 1-------CONTINUAR ")
            print("Opción 2-------SALIR"+"\n")
            Continuar = input("Por favor digite alguna de las opciones: "+"\n")
            if (not(Continuar.isnumeric())): 
                print("La opción proporcionada es incorrecta, por favor digite uno de los números del menú: "+"\n") 
                continue
            x = int(Continuar)
            if x == 1:
                menu.startMenu()
                break
            elif x == 2:
                exit()
            else:
                print("La opción digitada no es válida, por favor digite una opción presente en el menú: "+"\n")
    except BaseException():
        print("--------------ERROR DEL SISTEMA---------------")
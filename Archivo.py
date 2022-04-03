import os
class Archivo:

    def lectura():
        global origen
        global destino
        global extension_copia 
        global extension_movimiento 
        archivo = open("configuracion.txt","r")
        lista_parametros = archivo.readlines()
        for n in lista_parametros:
            if (n.split("=")[0]=="origen"):
                origen = n.split("=")[1].strip()
            if (n.split("=")[0]=="destino"):
                destino = n.split("=")[1].strip()
            if (n.split("=")[0]=="copyfiles"):
                extension_copia = n.split("=")[1].strip()
            if (n.split("=")[0]=="movefiles"):
                extension_movimiento = n.split("=")[1].strip()
                
    def muestraContenido():
        lista_archivos = os.listdir(origen)
        print ("Los archivos que se encuentran son: ")
        for linea in lista_archivos:
            print(linea)
    
    
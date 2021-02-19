
def main():
    #################################### Funciones complementarias
    #Función para controlar los menus
    def pedirNumeroEntero():   
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("Introduce un numero entero: "))
                correcto=True
            except ValueError:
                print('Error, introduce un numero entero')    
        return num
 
    #Función crear la figuras
    def menu_figuras():
        salir2 = False
        while not salir2:
            print("----------------------------------")     
            print ("1.- Crear Cuadrado")
            print ("2.- Crear Triangulo")
            print ("3.- Crear Circulo")               
            print ("4.- Salir")
                            
            print ("Elige una opcion")
            
            opcion2 = pedirNumeroEntero()
            print("----------------------------------") 
                  
            if opcion2 == 1:
                print("")
            elif opcion2 == 2:
                print("")
            elif opcion2 == 3:
                print("")
            elif opcion2 == 4:
                salir2 = True
            else:
                print ("Introduce un numero entre 1 y 4")
        print ("Usted dejo de crear figuras")
    #################################### Variables que controlan el programa principal
    salir = False
    opcion = 0
    #################################### Programa
    while not salir:
        print("----------------------------------")    
        print ("1.- Crear figura")
        print ("2.- Listar una clasificación de figuras")
        print ("3.- Listar todas las figuras")
        print ("4.- Mostrar suma de todas las áreas")
        print ("5.- Mostrar la suma de todos los perímetros")
        print ("6.- Limpiar lista")
        print ("0.- Salir")
        
        print ("Elige una opcion")
    
        opcion = pedirNumeroEntero()
        print("----------------------------------") 
        #Salir del Programa
        if opcion == 0:
            print("Usted Salio")
            salir = True
        #Crear figura
        elif opcion == 1:
            menu_figuras()           
        elif opcion == 2:
            print("")
        elif opcion == 3:
            print("")
        elif opcion == 4:
            print("")
        else:
            print ("Introduce un numero entre 0 y 6")
    print ("Fin")
    
main()
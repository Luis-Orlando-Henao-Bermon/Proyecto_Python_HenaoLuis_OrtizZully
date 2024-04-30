import json
from os import system #esto lo voy a usar para limpiar pantalla

system("clear") #esto es para que se limpie todo lo que hay en la terminal

#a continuacion estaran las funciones de los menus que se van a necesitar
def menuCamper():
    print("/////////////////////////////////////////////////\n-------------- Bienvenido",archivo["Campers"][i]["nombres"],"""----------------------------
          1). Verificar el riego del camper.
          2). Cambiar usuarios y contraseñas.
          3). Cambiar informacion.
          4). Salir
    -------------------------------------------------
    /////////////////////////////////////////////////
""")

def menuCamperOpc1():
    print("""
    ---------------------REPORTES---------------------
          1). Mostrar datos del Camper.
          2). Riesgo del camper.
          3). Ruta del camper.
          4). Trainer del camper
          5). Modulo en el que se encuetra el camper.
    --------------------------------------------------
""")

def menuCamperOpc3():
    print("""
    ----------------- Cambiar información ------------------
          1). Cambiar dirección.
          2). Cambiar telefono movil.
          3). Cambiar telefono fijo.
    --------------------------------------------------------
""")

def menuTrainer():
    print("///////////////////////////////////////////////////\n----------- BIENVENIDO", archivo["Trainers"][q]["nombres"],"""--------------------
          1). Cambiar usuario y contraseña
          2). Ruta de entrenamiento.
          3). Cambiar información.
          4). Salir
    ---------------------------------------------------
    ///////////////////////////////////////////////////
""")

def munuTrainerOpc3():
    print("""
    ----------------- Cambiar información ---------------
          1). Cambiar dirección.
          2). Cambiar telefono movil.
          3). Cambiar telefono fijo 
    -----------------------------------------------------
""")

def menuCoordinador():
    print("//////////////////////////////////////////////////////////////////////\n    ---------------- Bienvenido",archivo["Coordinador"][0]["nombres"],"""----------------------------
          1). Cambiar usuarios y contraseñas de todo el sistema educativo.
          2). Cambiar informacion de todo el sistema educativo.
          3). Agregar nota de examen de aprobación.
          4). Agregar nota de filtro. 
          5). Consultar cuales campers se encuentra en riego.
          6). Reporte.
          7). Salir
    -----------------------------------------------------------------------
    ///////////////////////////////////////////////////////////////////////
""")

def menuCoordinadorOpc6():
    print("""
    ---------------------------------    Reporte   ----------------------------------------------------
          1). Listar los campers que se encuentre en estado inscrito.
          2). Listar los campers que aprobaron el examen final.
          3). Listar los trainers que se encuentre trabajando en Campusland. 
          4). Litar los campers que se encuentre en bajo rendimiento.
          5). Listar los campers y trainers que se encuentren asociados a una ruta de entretenimiento.
          6). Mostrar cuantos campers perdieron y aprobaron cada modulo. 
    ----------------------------------------------------------------------------------------------------
""")
    

with open("./Campusland.json", encoding="utf-8") as file:#con esto se abre el archivo de campusland.json que es donde esta toda la informacion
    archivo=json.load(file)

user=input("Ingrese el usuario\n")#se pide que ingrese el usuario

x=0#esto es para saber si hay alguien con ese usuario ya que si hay alguien con ese usuario x se volvera 1 y se terminara el bucle de while 

while x==0:#si no hay nadie con el usuario ingresado x seguira siendo 0 por lo tanto se repetira el bucle while (antes de repetir el bucle se pide que se ingrese de nuevo el usuario para poder ver si el ingresado nuevamente esta o no )
    for i in range(len(archivo["Campers"])):#se usa un bucle for para recorra cada una  de las pociciones de los campers

        if user==archivo["Campers"][i]["user"]["login"]:#se miran todas las pociciones de los campers y si el usuario (login) alguno de ellos coinciden con el ingresado x pasa a valer 1 y se rompe el bucle de while 

            x+=1
            passwordCamper=input("Ingresa la contraseña\n")#despues de saber cual es el camper con ese usuario se le pide la contraseña 

            while passwordCamper not in archivo["Campers"][i]["user"]["contraseña"]:#se usa un bucle while porque mientras que la contraseña ingresada no este en archivo["Campers"][i]["user"]["contraseña"] (que es la direcion en donde esta la contraseña en el archivo) se repetira el bucle que lo que hace es volver a pedirle la contraseña 
                passwordCamper=input("Contraseña incorrecta ingresela otra vez\n")

            menuCamper()#aca se llama al menu de las opciones de camper 
            try:
                opcMenuCamper=int(input("Ingresa tu opcion\n"))#se pide la opcion a escoger en el menu y en caso de que ingrese una letra para que no muestre un error se pide que ingrese una letra y se lee en la misma variable 
                while opcMenuCamper<1 or opcMenuCamper>4:
                    opcMenuCamper=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 3 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla 
            except ValueError:
                opcMenuCamper=int(input("Ingresa una opcion valida (Numero)\n"))
                while opcMenuCamper<1 or opcMenuCamper>4:
                    opcMenuCamper=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 3 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
            
            system("clear")
            #Crear otro booleano para que se repita las opciones del menu del camper
            campers=True
            while campers==True:
                #Si la opcion elegida del menu del camper es uno se hara lo siguiente
                if opcMenuCamper==1:

                    if archivo["Campers"][i]["estado"]=="aprobado" or archivo["Campers"][i]["estado"]=="cursando": # Si en las posiciones del camper se encuentra el estado aprobado o cursando se le mstrata al camper.
                        print("Te encuentras",archivo["Campers"][i]["riesgo"])#Se le mostrara al camper el riesgor que se encuentra
                    else:#Si el camper no se encuentra en aprobado o cursando se le notificara que se encuetra retirado
                        print("Te encuentras",archivo["Campers"][i]["estado"]),"por lo tanto no tienes riesgo"

                    menuCamper()#aca se llama al menu de las opciones de camper 
                    try:
                        opcMenuCamper=int(input("Ingresa tu opcion\n"))#se pide la opcion a escoger en el menu y en caso de que ingrese una letra para que no muestre un error se pide que ingrese una letra y se lee en la misma variable 
                        while opcMenuCamper<1 or opcMenuCamper>4:
                            opcMenuCamper=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 3 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla 
                    except ValueError:
                        opcMenuCamper=int(input("Ingresa una opcion valida (Numero)\n"))
                        while opcMenuCamper<1 or opcMenuCamper>4:
                            opcMenuCamper=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 3 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla

                elif opcMenuCamper==2:#Si la opcion elegida del menu del camper es dos se hara lo siguiente
                    newUser1=input("¿Cual es el nuevo usuario?\n")#Se le preguntara al camper cual va a ser el nuevo usuario
                    archivo["Campers"][i]["user"]["login"]=newUser1

                    newPass1=input("¿Ingrese la nueva contraseña?\n")#Se le preguntara al camper cual va a ser el nuevo usuario
                    archivo["Campers"][i]["user"]["contraseña"]=newPass1

                    menuCamper()#aca se llama al menu de las opciones de camper 
                    try:
                        opcMenuCamper=int(input("Ingresa tu opcion\n"))#se pide la opcion a escoger en el menu y en caso de que ingrese una letra para que no muestre un error se pide que ingrese una letra y se lee en la misma variable 
                        while opcMenuCamper<1 or opcMenuCamper>4:
                            opcMenuCamper=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 3 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla 
                    except ValueError:
                        opcMenuCamper=int(input("Ingresa una opcion valida (Numero)\n"))
                        while opcMenuCamper<1 or opcMenuCamper>4:
                            opcMenuCamper=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 3 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla

                elif opcMenuCamper==3:
                    menuCamperOpc3()
                    numOpc=int(input("Ingrese una de las opciones del menu anterior\n"))
                    if numOpc==1:
                        newAdress=input("Ingrese la nueva direccion\n")
                        archivo["Campers"][i]["direccion"]=newAdress

                    elif numOpc==2:
                        newPhone=input("Ingrese el nuevo telefono movil\n")
                        archivo["Campers"][i]["telefonoCelular"]=newPhone#

                    elif numOpc==3:
                        newFijo=input("Ingrese el nuevo telefono fijo\n")
                        archivo["Campers"][i]["telefonoFijo"]=newFijo
                        
                    menuCamper()#aca se llama al menu de las opciones de camper 
                    try:
                        opcMenuCamper=int(input("Ingresa tu opcion\n"))#se pide la opcion a escoger en el menu y en caso de que ingrese una letra para que no muestre un error se pide que ingrese una letra y se lee en la misma variable 
                        while opcMenuCamper<1 or opcMenuCamper>4:
                            opcMenuCamper=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 3 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla 
                    except ValueError:
                        opcMenuCamper=int(input("Ingresa una opcion valida (Numero)\n"))
                        while opcMenuCamper<1 or opcMenuCamper>4:
                            opcMenuCamper=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 3 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                elif opcMenuCamper==4:
                     campers=False
                    

    for q in range(len(archivo["Trainers"])):#se usa un bucle for para recorra cada una  de las pociciones de los trainers

        if user == archivo["Trainers"][q]["user"]["login"]:#se miran todas las pociciones de los trainers y si el usuario (login) alguno de ellos coinciden con el ingresado x pasa a valer 1 y se rompe el bucle de while

            x+=1
            passwordTrainer=input("Ingresa la contraseña\n")#despues de saber cual es el Trainer con ese usuario se le pide la contraseña 
            
            while passwordTrainer not in archivo["Trainers"][q]["user"]["contraseña"]:#se usa un bucle while porque mientras que la contraseña ingresada no este en ["Trainers"][q]["user"]["contraseña"] (que es la direcion en donde esta la contraseña en el archivo) se repetira el bucle que lo que hace es volver a pedirle la contraseña 
                passwordTrainer=input("Contraseña incorrecta ingresela otra vez\n")
            
            menuTrainer()
            try:
                opcMenuTrainer=int(input("Ingresa tu opcion\n"))#se pide la opcion a escoger en el menu y en caso de que ingrese una letra para que no muestre un error se pide que ingrese una letra y se lee en la misma variable
                while opcMenuTrainer<1 or opcMenuTrainer>4:
                    opcMenuTrainer=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 3 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla

            except ValueError:
                opcMenuTrainer=int(input("Ingresa una opcion valida (Numero)\n"))
                while opcMenuTrainer<1 or opcMenuTrainer>4:
                    opcMenuTrainer=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 3 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla

    if user == archivo["Coordinador"][0]["user"]["login"]:#como se sabe que solo hay un coordinador mira si en coordinador esta ese usuario ingresado 
        system("clear")
        x+=1
        passwordCoordinador=input("Ingresa la contraseña\n")#si el usuario ingresado es el del coordinador se le pide la contraseña

        while passwordCoordinador not in archivo["Coordinador"][0]["user"]["contraseña"]:#se usa un bucle while porque mientras que la contraseña ingresada no este en archivo["Coordinador"]["user"][0]["contraseña"] (que es la direcion en donde esta la contraseña en el archivo) se repetira el bucle que lo que hace es volver a pedirle la contraseña 
            passwordCoordinador=input("Contraseña incorrecta ingresela otra vez\n")

        system("clear")

        menuCoordinador()
        try:
            opcMenuCoordinador=int(input("Ingresa tu opcion\n"))
            while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                    opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
        except ValueError:
            opcMenuCoordinador=int(input("Ingresa una opcion valida (Numero)\n"))
            while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                    opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
        
        
        bol1=True
        while bol1== True:
            if opcMenuCoordinador==1:
                system("clear")
                print("----Usiarios----\nCampers\nTrainers\nCoordinador")#se le muestran los tipos de usuarios que hay y se le preguanta cual de esos quiere cambiar
                personaCambiar=input("¿Que usuario quieres cambiar?\n")
                while personaCambiar not in archivo:#mientras que el usuario que ingrese no este en archivo
                    personaCambiar=input("Ingresa un usuario de los que aparecen en pantalla\n")

                for r in range(len(archivo[personaCambiar])):
                    print("Nombre:",archivo[personaCambiar][r]["nombres"])
                    print("ID:",archivo[personaCambiar][r]["id"])

                print("Ingresa el id del", personaCambiar, "que quieres cambiar")
                user1=input()

                for w in range(len(archivo[personaCambiar])):
                    if user1== archivo[personaCambiar][w]["id"]:
                        newUser20=input("Cual es el nuevo usuario\n")
                        archivo[personaCambiar][w]["user"]["login"]=newUser20
                        newPassword20=input("Cual es la nueva contraseña\n")
                        archivo[personaCambiar][w]["user"]["contraseña"]=newPassword20
                     
                    

                
                menuCoordinador()
                try:
                    opcMenuCoordinador=int(input("Ingresa tu opcion\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                except ValueError:
                    opcMenuCoordinador=int(input("Ingresa una opcion valida (Numero)\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla

            elif opcMenuCoordinador==2:


                menuCoordinador()
                try:
                    opcMenuCoordinador=int(input("Ingresa tu opcion\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                except ValueError:
                    opcMenuCoordinador=int(input("Ingresa una opcion valida (Numero)\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla

            elif opcMenuCoordinador==3:


                menuCoordinador()
                try:
                    opcMenuCoordinador=int(input("Ingresa tu opcion\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                except ValueError:
                    opcMenuCoordinador=int(input("Ingresa una opcion valida (Numero)\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla

            elif opcMenuCoordinador==4:


                menuCoordinador()
                try:
                    opcMenuCoordinador=int(input("Ingresa tu opcion\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                except ValueError:
                    opcMenuCoordinador=int(input("Ingresa una opcion valida (Numero)\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla


            elif opcMenuCoordinador==5:


                menuCoordinador()
                try:
                    opcMenuCoordinador=int(input("Ingresa tu opcion\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                except ValueError:
                    opcMenuCoordinador=int(input("Ingresa una opcion valida (Numero)\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla

            elif opcMenuCoordinador==6:


                menuCoordinador()
                try:
                    opcMenuCoordinador=int(input("Ingresa tu opcion\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                except ValueError:
                    opcMenuCoordinador=int(input("Ingresa una opcion valida (Numero)\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
            
            elif opcMenuCoordinador==7:
                print ("Gracias por usar el programa")

                bol1=False

    if x==0:
        user=input("No se encontro el usuario ingreselo nuevamente\n")



json_archivo=json.dumps(archivo)
with open("./Campusland.json","w") as files:
    files.write(json_archivo)
#Desarrollado por Luis Henao c.c. 1093904929 y Zully Ortiz c.c.1092528097
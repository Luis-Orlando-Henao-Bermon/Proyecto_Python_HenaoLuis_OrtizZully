import json
from os import system #esto lo voy a usar para limpiar pantalla

system("clear") #esto es para que se limpie todo lo que hay en la terminal

#a continuacion estaran las funciones de los menus que se van a necesitar
def menuCamper():
    print("/////////////////////////////////////////////////\n-------------- Bienvenido",archivo["Campers"][i]["nombres"],"""----------------------------
          1). Reportes.
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

def menuTrainerOpc3():
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

user=input("Ingrese su usuario:\n")#se pide que ingrese el usuario

x=0#esto es para saber si hay alguien con ese usuario ya que si hay alguien con ese usuario x se volvera 1 y se terminara el bucle de while 

while x==0:#si no hay nadie con el usuario ingresado x seguira siendo 0 por lo tanto se repetira el bucle while (antes de repetir el bucle se pide que se ingrese de nuevo el usuario para poder ver si el ingresado nuevamente esta o no )
    for i in range(len(archivo["Campers"])):#se usa un bucle for para recorra cada una  de las pociciones de los campers

        if user==archivo["Campers"][i]["user"]["login"]:#se miran todas las pociciones de los campers y si el usuario (login) alguno de ellos coinciden con el ingresado x pasa a valer 1 y se rompe el bucle de while 

            x+=1
            passwordCamper=input("Ingresa su contraseña:\n")#despues de saber cual es el camper con ese usuario se le pide la contraseña 

            while passwordCamper != archivo["Campers"][i]["user"]["contraseña"]:#se usa un bucle while porque mientras que la contraseña ingresada no este en archivo["Campers"][i]["user"]["contraseña"] (que es la direcion en donde esta la contraseña en el archivo) se repetira el bucle que lo que hace es volver a pedirle la contraseña 
                passwordCamper=input("Contraseña incorrecta ingresela otra vez\n")

            menuCamper()#aca se llama al menu de las opciones de camper 
            bol2=True
            while bol2==True:
                try:
                    opcMenuCamper=int(input("Ingresa tu opcion\n"))
                    while opcMenuCamper<1 or opcMenuCamper>4:
                            opcMenuCamper=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                    bol2=False
                except ValueError:
                    print("Ingresa una opcion valida (Numero)\n")
            system("clear")
            #Crear otro booleano para que se repita las opciones del menu del camper
            campers=True
            while campers==True:
                #Si la opcion elegida del menu del camper es uno se hara lo siguiente
                if opcMenuCamper==1:
                    #Le mostrara el camper el submenu de la opcion uno 
                    menuCamperOpc1()
                    #El camper ingresara la opcion que desea observar 
                    newOpc1=int(input("Ingrese una opcion del menu anterior:\n"))
                    #Si la opcion elegida es uno se mostrara 
                    if newOpc1==1:#toda la informacion que tiene el camper, llamar desde json cada informacion del camper para que se muestre de una forma ordenada en la pantalla
                        print("Hola",archivo["Campers"][i]["nombres"],"estos son tus datos:\n")
                        print("Numero de identificaion:",archivo["Campers"][i]["numeroIdentificacion"])
                        print("Nombres:",archivo["Campers"][i]["nombres"])
                        print("Apellidos:",archivo["Campers"][i]["apellidos"])
                        print("Direccion:",archivo["Campers"][i]["direccion"])
                        print("Acudiente:",archivo["Campers"][i]["acudiente"])
                        print("Telefono celular:",archivo["Campers"][i]["telefonoCelular"])
                        print("Telefono fijo:",archivo["Campers"][i]["telefonoFijo"])
                        print("")
                        #Despues de mostrado lo anterior se lo mostrara otra vez el sudmenu por si el camper desea observar otra opción
                        menuCamperOpc1()#aca se llama al menu de las opciones de camper 
                        bol18=True#este booleano es por si el camper ingresa una letra no le finalice la plataforma si no que le indique que vuelva a ingresar el numero de la opcion y se le recordara que debe ingresar solo numero 
                        while bol18==True:
                            try:
                                opcMenuCamperOpc1=int(input("Ingresa tu opcion\n"))
                                while opcMenuCamperOpc1<1 or opcMenuCamperOpc1>5:
                                        opcMenuCamperopc1=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                                bol18=False
                            except ValueError:
                                print("Ingresa una opcion valida (Numero)\n")
                        system("clear")
                    #Si la opcion elegida es dos se hara:
                    elif newOpc1==2:
                        if archivo["Campers"][i]["estado"]=="aprobado" or archivo["Campers"][i]["estado"]=="cursando": 
                            # Si en las posiciones del camper se encuentra el estado aprobado o cursando se le mstrata al camper.   
                            print("Tu riesgo es:",archivo["Campers"][i]["riesgo"])#Se le mostrara al camper el riesgos que se encuentra
                        else:#Si el camper no se encuentra en aprobado o cursando se le mostrara en que estado se encuentra y se le aclarará que no tienes riesgo por lo mismo.
                            print("Tu estado es:",archivo["Campers"][i]["estado"],"por lo tanto no tienes riesgo")

                        menuCamperOpc1()#aca se llama al menu de las opciones de camper 
                        bol14=True#este booleano es por si el camper ingresa una letra no le finalice la plataforma si no que le indique que vuelva a ingresar el numero de la opcion y se le recordara que debe ingresar solo numero 
                        while bol14==True:
                            try:
                                opcMenuCamperOpc1=int(input("Ingresa tu opcion\n"))
                                while opcMenuCamperOpc1<1 or opcMenuCamperOpc1>5:
                                        opcMenuCamperopc1=int(input("Ingresa una opcion de las que aparecen en pantalla\n")) #se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                                bol14=False
                            except ValueError:
                                print("Ingresa una opcion valida (Numero)\n")
                        system("clear")
                    #Si la opcion elegida es tres se hara:
                    elif newOpc1==3:
                        print("Tu ruta es:",archivo["Campers"][i]["ruta"])#Se le mostara la ruta en el que se encuentra el camper

                        menuCamperOpc1()#aca se llama al menu de las opciones de camper 
                        bol15=True#este booleano es por si el camper ingresa una letra no le finalice la plataforma si no que le indique que vuelva a ingresar el numero de la opcion y se le recordara que debe ingresar solo numero 
                        while bol15==True:
                            try:
                                opcMenuCamperOpc1=int(input("Ingresa tu opcion\n"))
                                while opcMenuCamperOpc1<1 or opcMenuCamperOpc1>5:
                                        opcMenuCamperopc1=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                                bol15=False
                            except ValueError:
                                print("Ingresa una opcion valida (Numero)\n")
                        system("clear")
                    #Si la opcion elegida del camper es cuatro se hara: 
                    elif newOpc1==4:
                        print("Tu trainer es:",archivo["Campers"][i]["trainer"])#Se le mostrara el trainer del camper

                        menuCamperOpc1()#aca se llama al menu de las opciones de camper 
                        bol16=True#este booleano es por si el camper ingresa una letra no le finalice la plataforma si no que le indique que vuelva a ingresar el numero de la opcion y se le recordara que debe ingresar solo numero 
                        while bol16==True:
                            try:
                                opcMenuCamperOpc1=int(input("Ingresa tu opcion\n"))
                                while opcMenuCamperOpc1<1 or opcMenuCamperOpc1>5:
                                        opcMenuCamperopc1=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                                bol16=False
                            except ValueError:
                                print("Ingresa una opcion valida (Numero)\n")
                        system("clear")
                    #Si la opcion elegida es cinco se hara:
                    elif newOpc1==5:
                        print("El modulo que te encuentras actualmente es:",archivo["Campers"][i]["modulos"])#SSe mostrara el modulo que se encuentra actualmente el camper

                        menuCamperOpc1()#aca se llama al menu de las opciones de camper 
                        bol17=True#este booleano es por si el camper ingresa una letra no le finalice la plataforma si no que le indique que vuelva a ingresar el numero de la opcion y se le recordara que debe ingresar solo numero 
                        while bol17==True:
                            try:
                                opcMenuCamperOpc1=int(input("Ingresa tu opcion\n"))
                                while opcMenuCamperOpc1<1 or opcMenuCamperOpc1>5:
                                        opcMenuCamperopc1=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                                bol17=False
                            except ValueError:
                                print("Ingresa una opcion valida (Numero)\n")
                        system("clear")

                    
                    menuCamper()#aca se llama al menu de las opciones de camper 
                    bol3=True#Este booleano es por si el camper ingresa una letra en las opciones no se le permitira y se le recordara que solo puede ingresar numeros.
                    while bol3==True:
                        try:
                            opcMenuCamper=int(input("Ingresa tu opcion\n"))
                            while opcMenuCamper<1 or opcMenuCamper>4:
                                    opcMenuCamper=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                            bol3=False
                        except ValueError:
                            print("Ingresa una opcion valida (Numero)\n")
                    system("clear")

                elif opcMenuCamper==2:#Si la opcion elegida del menu del camper es dos se hara lo siguiente

                    newUser1=input("¿Cual es el nuevo usuario?\n")#Se le preguntara al camper cual va a ser el nuevo usuario
                    archivo["Campers"][i]["user"]["login"]=newUser1#ingresara las posiciones del camper donde esta el user y mira el login(usuario) del camper y lo cambia por el nuevo.

                    newPass1=input("¿Ingrese la nueva contraseña?\n")#Se le preguntara al camper cual va a ser el nuevo usuario
                    archivo["Campers"][i]["user"]["contraseña"]=newPass1#ingresara las posiciones del camper donde esta el user y mira la contraseña del camper y lo cambia por el nuevo que ingreso.

                    menuCamper()#aca se llama al menu de las opciones de camper 
                    bol4=True#Este booleano es por si el camper ingresa una letra en las opciones, no se le permitira seguir y se le recordara que solo puede ingresar numeros, hata que no lo haga bien el bucle no va a parar y se seguira repitiendo.
                    while bol4==True:
                        try:
                            opcMenuCamper=int(input("Ingresa tu opcion\n"))
                            while opcMenuCamper<1 or opcMenuCamper>4:
                                    opcMenuCamper=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                            bol4=False
                        except ValueError:
                            print("Ingresa una opcion valida (Numero)\n")
                    system("clear")

                elif opcMenuCamper==3:#Si la opcion elegida del camper se hara:

                    menuCamperOpc3()#Se llamara la funcion del menu camper opcion tres donde se le mostrara las opciones disponibles del menu.
                    numOpc=int(input("Ingrese una de las opciones del menu anterior\n"))#El ingresara la opcione que desee realizar del menu anterior 
                    if numOpc==1:#Si la opcion del menu es uno se hara:
                        newAdress=input("Ingrese la nueva direccion\n")#el camper ingresara la nueva direccion 
                        archivo["Campers"][i]["direccion"]=newAdress#Ingresara en las posiciones del camper y ingresara  a la direccion y asi se guardara el cambio de la nueva direccion 

                    elif numOpc==2:#Si la opcion del menu es dos se hara:
                        bol7=True#este boleano es para que el valor a ingresar a pantalla sea numero si no es numero se volvera a repetir el bucle y no le permitira seguir.
                        while bol7==True:
                            try:
                                newPhone=int(input("Ingrese el nuevo telefono movil\n"))#el camper ingresara el nuevo telefono movil 
                                bol7=False
                            except ValueError:   
                                newPhone=int(input("Ingrese un telefono movil valido (solo numeros)\n"))#el camper ingresara el nuevo telefono movil

                        archivo["Campers"][i]["telefonoCelular"]=newPhone#Ingresara en las posiciones del camper y ingresara donde esta el telefono movil y asi se guardara el cambio del nuevo dato ingresado.

                    elif numOpc==3:#Si la opcion elegida es tres se hara:
                        bol8=True#este boleano es para que el valor a ingresar a pantalla sea numero si no es numero se volvera a repetir el bucle y no le permitira seguir.
                        while bol8==True:
                            try:
                                newFijo=int(input("Ingrese el nuevo telefono fijo\n"))#el camper ingresara el nuevo telefono fijo
                                bol8=False
                            except ValueError:
                                newFijo=int(input("Ingrese un telefono fijo valido(solo numeros)\n"))#Si el camper ingresa alguna letra se le notificara y se le recordara que solo se acepta numero y se volvera a repetir 

                        archivo["Campers"][i]["telefonoFijo"]=newFijo#Ingresara en las posiciones del camper y ingresara donde se encuentra telefono fijo y asi se guardara el nuevo dato ingresado. 
                        
                    menuCamper()#aca se llama al menu de las opciones de camper 
                    bol5=True#Este booleano es por si el camper ingresa una letra en las opciones, no se le permitira seguir y se le recordara que solo puede ingresar numeros, hata que no lo haga bien el bucle no va a parar y se seguira repitiendo.
                    while bol5==True:
                        try:
                            opcMenuCamper=int(input("Ingresa tu opcion\n"))
                            while opcMenuCamper<1 or opcMenuCamper>4:
                                    opcMenuCamper=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                            bol5=False
                        except ValueError:
                            print("Ingresa una opcion valida (Numero)\n")
                    system("clear")

                elif opcMenuCamper==4:#Si la opcion del menu del camper es cuatro se finalizara la plataforma
                     campers=False
                    

    for q in range(len(archivo["Trainers"])):#se usa un bucle for para recorra cada una  de las pociciones de los trainers

        if user == archivo["Trainers"][q]["user"]["login"]:#se miran todas las pociciones de los trainers y si el usuario (login) alguno de ellos coinciden con el ingresado x pasa a valer 1 y se rompe el bucle de while

            x+=1
            passwordTrainer=input("Ingresa la contraseña\n")#despues de saber cual es el Trainer con ese usuario se le pide la contraseña 
            
            while passwordTrainer != archivo["Trainers"][q]["user"]["contraseña"]:#se usa un bucle while porque mientras que la contraseña ingresada no este en ["Trainers"][q]["user"]["contraseña"] (que es la direcion en donde esta la contraseña en el archivo) se repetira el bucle que lo que hace es volver a pedirle la contraseña 
                passwordTrainer=input("Contraseña incorrecta ingresela otra vez\n")
            
            menuTrainer()
            bol6=True#Este booleano es por si el camper ingresa una letra en las opciones, no se le permitira seguir y se le recordara que solo puede ingresar numeros, hata que no lo haga bien el bucle no va a parar y se seguira repitiendo.
            while bol6==True:
                try:
                    opcMenuTrainer=int(input("Ingresa tu opcion\n"))
                    while opcMenuTrainer<1 or opcMenuTrainer>4:
                            opcMenuTrainer=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero menor a 4 o mayor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                    bol6=False
                except ValueError:
                    print("Ingresa una opcion valida (Numero)\n")
            system("clear")

            trainers=True
            while trainers==True:
                #Si la opcion del menu del trainer es uno se hara:
                if opcMenuTrainer == 1:

                    newUser2=input("¿Cual es el nuevo usuario?:\n")#El trainer ingresara el nuevo usuario 
                    archivo["Trainers"][q]["user"]["login"]=newUser2 #en el archivo se posicionara donde estan los trainer e ingresara a user login(usuario) y se guardara el nuevo usuario que ingreso el trainer
                    newPass2=input("¿Cual es la nueva contraseña?:\n")#El trainer ingresara la nueva contraseña
                    archivo["Trainers"][q]["user"]["contraseña"]=newPass2#en el archivo se posicionara donde se encuantre los traines e ingresara a user contraseña y se guardara la nueva contraseña que ingreso el trainer 

                    menuTrainer()
                    bol9=True
                    while bol9==True: 
                        try:
                            opcMenuTrainer=int(input("Ingresa tu opcion\n"))
                            while opcMenuTrainer<1 or opcMenuTrainer>4:
                                opcMenuTrainer=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero menor a 4 o mayor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                            bol9=False
                        except ValueError:
                            print("Ingresa una opcion valida (Numero)\n")
                    system("clear")
                #Si la opcion del menu del trainer es dos se hara:
                elif opcMenuTrainer == 2:
                    print(archivo["Trainers"][q]["seciones"])
                    

                    menuTrainer()
                    bol9=True
                    while bol9==True: 
                        try:
                            opcMenuTrainer=int(input("Ingresa tu opcion\n"))
                            while opcMenuTrainer<1 or opcMenuTrainer>4:
                                    opcMenuTrainer=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                            bol9=False
                        except ValueError:
                            print("Ingresa una opcion valida (Numero)\n")
                    system("clear")
                #Si la opcion elegida es tres se hara:
                elif opcMenuTrainer==3:
                    #se le mostara el submenu de la opcion 3 al trainer 
                    menuTrainerOpc3()
                    newOpc=int(input("Ingrese unas de las opciones del menu anterior:\n"))#Ingresara una opcion del submenu anterior
                    if newOpc==1:#Si la opcion es uno se hara:
                        newAdress1=input("Ingrese la nueva dirección:\n")#El trainer ingresara la direccion nueva 
                        archivo["Trainers"][q]["direccion"]=newAdress1#en las pociciones del trainer en la posicion de direccion se le cambiara a la direccion nueva ingresada por el mismo.
                    #si la opcion elegida es dos se hara:
                    elif newOpc==2:
                        bol10=True#este booleano es por que el dato a ingresar debe ser entero por ende si el trainer ingresa una letra no se le aceptara y se le volvera a repetir el valor a ingresar hasta que no lo ingrese bien el bucle no parará.
                        while bol10==True:
                            try:
                                newPhone1=int(input("Ingrese el nuevo telefono movil:\n"))#El trainer ingresara el nuevo telefono movil
                                bol10=False
                            except ValueError:
                                newPhone1=int(input("Ingrese un telefono movil valido(solo numeros)\n"))
                        archivo["Trainers"][q]["telefonoCelular"]=newPhone1#En las posiciones del trainer en la posicion del telefono celular se guardara el dato que ingreso en trainer
                    #Si la opcion elegida es tres se hara: 
                    elif newOpc==3:
                        bol11=True#este booleano es por que el dato a ingresar debe ser entero por ende si el trainer ingresa una letra no se le aceptara y se le volvera a repetir el valor a ingresar hasta que no lo ingrese bien el bucle no parará.
                        while bol11==True:
                            try:
                                newFijo1=int(input("Ingrese el nuevo telefono fijo:\n"))#El trainer ingresara el nuevo telefono fijo
                                bol11=False
                            except ValueError:
                                newFijo1=int(input("Ingrese un telefono fijo valido (solo numeros)\n"))
                        archivo["Trainers"][q]["telefonoFijo"]=newFijo1#En las posiciones del trainer en la posicion del telefono fijo se guardara el dato que ingreso en trainer

                        menuTrainer()#Se le volvera a mostrar el menu principal al trainer
                        bol12=True
                        while bol12==True: 
                            try:
                                opcMenuTrainer=int(input("Ingresa tu opcion\n"))
                                while opcMenuTrainer<1 or opcMenuTrainer>4:
                                        opcMenuTrainer=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                                bol12=False
                            except ValueError:
                                print("Ingresa una opcion valida (Numero)\n")
                        system("clear")

                #si la opcion del menu del trainer es cuatro se hara:
                elif opcMenuTrainer == 4:
                    trainers=False#se finalizara la plataforma 
                    
            
    if user == archivo["Coordinador"][0]["user"]["login"]:#como se sabe que solo hay un coordinador mira si en coordinador esta ese usuario ingresado 
        system("clear")
        x+=1
        passwordCoordinador=input("Ingresa la contraseña:\n")#si el usuario ingresado es el del coordinador se le pide la contraseña

        while passwordCoordinador != archivo["Coordinador"][0]["user"]["contraseña"]:#se usa un bucle while porque mientras que la contraseña ingresada no este en archivo["Coordinador"]["user"][0]["contraseña"] (que es la direcion en donde esta la contraseña en el archivo) se repetira el bucle que lo que hace es volver a pedirle la contraseña 
            passwordCoordinador=input("Contraseña incorrecta ingresela otra vez\n")

        system("clear")

        menuCoordinador()
        bol21=True
        while bol21==True:
            try:
                opcMenuCoordinador=int(input("Ingresa tu opcion:\n"))
                while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                        opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 6 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                bol21=False
            except ValueError:
                print("Ingresa una opcion valida (Numero)\n")

        
        
        bol1=True
        while bol1== True:
            if opcMenuCoordinador==1:#si ecoge la opcion numero 1 hace el siguiente codigo
                system("clear")
                print("----Usuarios----\nCampers\nTrainers\nCoordinador")#se le muestran los tipos de usuarios que hay y se le preguanta cual de esos quiere cambiar
                personaCambiar=input("¿Que usuario quieres cambiar?:\n")
                while personaCambiar not in archivo:#mientras que el usuario que ingrese no este en archivo
                    personaCambiar=input("Ingresa un usuario de los que aparecen en pantalla (Tienes que escribirlos como se ven ahi):\n")
                print("-----Campers-----")
                for r in range(len(archivo[personaCambiar])):#este for se usa solo para que mire todas las personas que hay en el tipo de usuario quiere el cambiar (ejemplo: Campers)
                    print("------------------\n")
                    print("Nombre:",archivo[personaCambiar][r]["nombres"]) #siguiendo con el ejemplo le muestra todos los nombres que hay en Campers ya que recorre cada uno con el bucle for
                    print("ID:",archivo[personaCambiar][r]["id"])#siguiendo con el ejemplo le muestra todos los id que hay en Campers ya que recorre cada uno con el bucle for
                    print("------------------\n")

                bol22=True
                while bol22==True:
                    try:#se usa un bucle try dentro de un bucle while para que cada vez que mande error se repita el codigo y se pueda cometer ese error muchas veces 
                        print("Ingresa el id del", personaCambiar, "que quieres cambiar:")#se le pide el id de la persona que quiere cambiar usuario y contraseña  y se guarda en user1
                        user1=int(input())
                        bol22=False
                    except ValueError:
                        print("Ingresa un ID valido (solo numeros)")

                u=0#esta variable me va servir para saber si hay un usuario con ese id 
                while u==0:#mientras u siga valiendo 0 se va a repetir el bucle 
                    for t in range(len(archivo[personaCambiar])):#con el for se recorren todos loa puestos de las personas que hay en el tipo de usuario que quiere cambiar 
                        if user1==archivo[personaCambiar][t]["id"]:#mira si el id de algun usuario es igual al ingresado 
                            u=1#si hay un usuario igual al imgresado u va a valer 1 y se terminara el bucle de while 
                    
                    if u==0:#en caso de que no haya ninguan persona con ese id u seguira valiendo 0 por lo tanto se pide que vuelva a escribir el id 
                        
                        try:
                            user1=int(input("ID no encontrado por favor ingresa uno valido\n"))
                        except ValueError:
                            print("Ingresa un ID valido (solo numeros)")

                

                for w in range(len(archivo[personaCambiar])):#se usa un for para que mire las personas que hay en el tipo de usuario que quiere cambiar
                    if user1== archivo[personaCambiar][w]["id"]:

                        newUser20=input("Cual es el nuevo usuario\n")#se pregunta cual va a ser 
                        archivo[personaCambiar][w]["user"]["login"]=newUser20

                        newPassword20=input("Cual es la nueva contraseña\n")
                        archivo[personaCambiar][w]["user"]["contraseña"]=newPassword20
                    
                system("clear")
                print("Usuario y contraseña cambiado con exito")
                
                menuCoordinador()
                try:
                    opcMenuCoordinador=int(input("Ingresa tu opcion\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 7 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                except ValueError:
                    opcMenuCoordinador=int(input("Ingresa una opcion valida (Numero)\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 7 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla

            elif opcMenuCoordinador==2:


                system("clear")
                print("----Usuarios----\nCampers\nTrainers\nCoordinador")#se le muestran los tipos de usuarios que hay y se le preguanta cual de esos quiere cambiar
                personaCambiarInfo=input("¿A que usuario le quieres cambiar informacion?:\n")
                while personaCambiarInfo not in archivo:#mientras que el usuario que ingrese no este en archivo
                    personaCambiarInfo=input("Ingresa un usuario de los que aparecen en pantalla (Tienes que escribirlos como se ven ahi):\n")
                print("-----Campers-----")
                for r in range(len(archivo[personaCambiarInfo])):#este for se usa solo para que mire todas las personas que hay en el tipo de usuario quiere el cambiar (ejemplo: Campers)
                    print("------------------")
                    print("Nombre:",archivo[personaCambiarInfo][r]["nombres"]) #siguiendo con el ejemplo le muestra todos los nombres que hay en Campers ya que recorre cada uno con el bucle for
                    print("ID:",archivo[personaCambiarInfo][r]["id"])#siguiendo con el ejemplo le muestra todos los id que hay en Campers ya que recorre cada uno con el bucle for
                    print("------------------\n")
                if personaCambiarInfo=="Campers":
                    bol23=True
                    while bol23==True:
                        try:#se usa un bucle try dentro de un bucle while para que cada vez que mande error se repita el codigo y se pueda cometer ese error muchas veces 
                            print("Ingresa el ID del Camper al que le quieres cambiar la informacion:")#se le pide el id de la persona que quiere cambiar usuario y contraseña  y se guarda en user1
                            user2=int(input())
                            bol23=False
                        except ValueError:
                            print("Ingresa un ID valido (solo numeros)")

                    o=0#esta variable me va servir para saber si hay un usuario con ese id 
                    while o==0:#mientras u siga valiendo 0 se va a repetir el bucle 
                        for t in range(len(archivo[personaCambiarInfo])):#con el for se recorren todos loa puestos de las personas que hay en el tipo de usuario que quiere cambiar 
                            if user2==archivo[personaCambiarInfo][t]["id"]:#mira si el id de algun usuario es igual al ingresado 
                                o=1#si hay un usuario igual al imgresado u va a valer 1 y se terminara el bucle de while
                                confiInfor="si"
                                posicionCamperCambiar=t
                                if archivo[personaCambiarInfo][t]["estado"]== "graduado" or archivo[personaCambiarInfo][t]["estado"]== "expulsado" or archivo[personaCambiarInfo][t]["estado"]== "retirado":#con esto se mira si el estado del camper es graduado, expulsado o retirado si es asi se le dice que no se puede modificar nada de la informacion ya que ya no pertenece a la institucion
                                    print("El estado del camper es:",archivo[personaCambiarInfo][t]["estado"],",por lo tanto no se le puede cambiar la informacion")
                                    confiInfor="no"
                                else:
                                    confiInfor="si"
                        if o==0:#en caso de que no haya ninguan persona con ese id u seguira valiendo 0 por lo tanto se pide que vuelva a escribir el id 
                            
                            try:
                                user2=int(input("ID no encontrado por favor ingresa uno valido\n"))
                            except ValueError:
                                print("Ingresa un ID valido (solo numeros)")

                    
                    system("clear")
                    while confiInfor=="si":
                        print("Datos por cambiar\n1. ID\n2. Numero de Identificacion\n3. Nombres\n4. Apellidos\n5. Direccion\n6. Acudiente\n7. Telefono Celular\n8. Telefono fijo\n9. Estado\n\nLa siguiente informacion solo es valida para usuarios que ya estan cursando\n\n10. Fecha de inicio\n11. Fecha de cierre\n12. grupo\n13. Modulo actual\n14. Modulos\n15. Trainer")

                        #esta es la manera en la que se puede hacer repetir un error 
                        bol24=True
                        while bol24==True:
                            try:

                                opcCambioCamper=int(input("¿Que dato quieres cambiar?:\n"))
                                while opcCambioCamper<1 or opcCambioCamper>15:#este while es para que ingrese una opcion de las que hay en pantalla 
                                    opcCambioCamper=int(input("ingresa una opcion de las que hay en pantalla\n"))
                                bol24=False
                            except ValueError:
                                   print("Ingresa una opcion valida (Numeros)")

                        if opcCambioCamper==1:

                            #esta es la manera en la que se puede hacer repetir un error 
                            bol25=True
                            while bol25==True:
                                try:
                                    idCambiar=int(input("Ingresa el nuevo ID\n"))
                                    bol25=False
                                except ValueError:
                                    print("Ingresa un ID valido (Solo numeros)")
                            
                            archivo[personaCambiarInfo][posicionCamperCambiar]["id"]=idCambiar#despues de haber pedido el nuevo id solo remplaza el que ya esta por el nuevo

                            confiInfor=input("¿Quieres cambiar algo mas? si/no\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")

                        elif opcCambioCamper==2:

                            #esta es la manera en la que se puede hacer repetir un error 
                            bol26=True
                            while bol26==True:
                                try:
                                    identificacionCambiar=int(input("Ingresa el nuevo numero de identificacion\n"))
                                    bol26=False
                                except ValueError:
                                    print("Ingresa un numero de identificaion valido (Solo numeros)")
                            
                            archivo[personaCambiarInfo][posicionCamperCambiar]["numeroIdentificacion"]=identificacionCambiar #despues de haber pedido el nuevo numero de identificacion solo remplaza el que ya estaba por el nuevo

                            confiInfor=input("¿Quieres cambiar algo mas? si/no\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")

                        elif opcCambioCamper==3:

                            nombreCambiar=input("Ingresa los nuevos nombres\n")

                            archivo[personaCambiarInfo][posicionCamperCambiar]["nombres"]=nombreCambiar #se preguntan los nuevos nombres y remplaza al que ya esta  

                            confiInfor=input("¿Quieres cambiar algo mas? si/no\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")

                        elif opcCambioCamper==4:

                            apellidoCambiar=input("Ingresa los nuevos apellidos\n")

                            archivo[personaCambiarInfo][posicionCamperCambiar]["apellidos"]=apellidoCambiar #se preguntan los nuevos apellidos y remplaza al que ya esta  

                            confiInfor=input("¿Quieres cambiar algo mas? si/no\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")

                        elif opcCambioCamper==5:

                            direccionCambiar=input("Ingresa la nueva direccion\n")

                            archivo[personaCambiarInfo][posicionCamperCambiar]["direccion"]=direccionCambiar #se pregunta la nueva direccion y remplaza al que ya esta  

                            confiInfor=input("¿Quieres cambiar algo mas? si/no\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")

                        elif opcCambioCamper==6:

                            acudienteCambiar=input("Ingresa los nuevos nombres y apellidos del acudiente\n")

                            archivo[personaCambiarInfo][posicionCamperCambiar]["acudiente"]=acudienteCambiar #se preguntan los nuevos nombres y apellidos del acudiente y remplaza al que ya esta  

                            confiInfor=input("¿Quieres cambiar algo mas? si/no\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")

                        elif opcCambioCamper==7:

                            #esta es la manera en la que se puede hacer repetir un error 
                            bol27=True
                            while bol27==True:
                                try:
                                    telefonoCambiar=int(input("Ingresa el nuevo numero de telefono movil\n"))
                                    bol27=False
                                except ValueError:
                                    print("Ingresa un numero de telefono movil valido (Solo numeros)")
                            
                            archivo[personaCambiarInfo][posicionCamperCambiar]["telefonoCelular"]=telefonoCambiar #despues de haber pedido el nuevo telefono movil solo remplaza el que ya estaba por el nuevo

                            confiInfor=input("¿Quieres cambiar algo mas? si/no\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")
                        
                        elif opcCambioCamper==8:

                            #esta es la manera en la que se puede hacer repetir un error 
                            bol28=True
                            while bol28==True:
                                try:
                                    telefonoFijoCambiar=int(input("Ingresa el nuevo numero de telefono fijo\n"))
                                    bol28=False
                                except ValueError:
                                    print("Ingresa un numero de telefono fijo valido (Solo numeros)")
                            
                            archivo[personaCambiarInfo][posicionCamperCambiar]["telefonoFijo"]=telefonoFijoCambiar #despues de haber pedido el nuevo numero de identificacion solo remplaza el que ya estaba por el nuevo

                            confiInfor=input("¿Quieres cambiar algo mas? si/no\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")

                        elif opcCambioCamper==9:
                            
                            print("-----Tipos de estado-----")
                            for a in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeEstados"])):
                                print(archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeEstados"][a])
                            
                            estadoCambiar=input("¿Cual es el nuevo estado?\n")

                            while estadoCambiar not in archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeEstados"]:
                                estadoCambiar=input("Ingrese un estado valido (Tienes que escribirlo como aparece en los tipos de estado)\n")

                            archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=estadoCambiar

                            if estadoCambiar=="Cursando":

                                print("Como el estado del estudiante ahora es cursando tienes que llenar la siguiente informacion:")

                                agregarFechaInicio=input("Ingrese una fecha de inicio (DD-MM-AAAA)\n")
                                archivo[personaCambiarInfo][posicionCamperCambiar]["fechaInicio"]=agregarFechaInicio

                                system("clear")
                                agregarFechaCierre=input("Ingrese una fecha de cierre (DD-MM-AAAA)\n")
                                archivo[personaCambiarInfo][posicionCamperCambiar]["fechaCierre"]=agregarFechaCierre

                                system("clear")
                                agregarGrupo=input("Ingrese el grupo al que va a pertenecer el Camper\n")
                                archivo[personaCambiarInfo][posicionCamperCambiar]["grupo"]=agregarGrupo

                                system("clear")
                                print("-----Tipos de Rutas-----")
                                for y in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeRutas"])):#se muestran todos los tipos de rutas que hay 
                                    print(archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeRutas"][y])
                                
                                rutaAgregar=input("Ingresa una ruta\n")

                                while rutaAgregar not in archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeRutas"]:
                                    rutaAgregar=input("Ingresa una ruta valida (Tienes que escribirlo como aparece en los tipos de rutas)\n")

                                archivo[personaCambiarInfo][posicionCamperCambiar]["ruta"]=rutaAgregar

                                system("clear")
                                archivo[personaCambiarInfo][posicionCamperCambiar]["moduloActual"]=1#se pone que el modulo actual es igual a 1 ya que como apenas esta empezando empieza en el modulo 1


                                print("-----Materias del modulo 3-----")#se muestran las materias que hay para el modulo 3
                                for i in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM3"])):
                                    print(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM3"][i])
                                
                                modulo3Agregar1=input("Ingresa las 1 materia que quieres agregar\n")
                                while modulo3Agregar1 not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM3"]:
                                    modulo3Agregar1=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")
                                
                                archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][2].append(modulo3Agregar1)
                                
                                modulo3Agregar2=input("Ingresa las 1 materia que quieres agregar\n")
                                while modulo3Agregar2 not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM3"]:
                                    modulo3Agregar2=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")

                                archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][2].append(modulo3Agregar2)

                                system("clear")

                                print("-----Materias del modulo 4-----")#se muestran las materias que hay para el modulo 3
                                for i in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM4"])):
                                    print(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM4"][i])
                                
                                modulo4Agregar1=input("Ingresa las 1 materia que quieres agregar\n")
                                while modulo4Agregar1 not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM4"]:
                                    modulo4Agregar1=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")
                                
                                archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][3].append(modulo4Agregar1)
                                
                                modulo4Agregar2=input("Ingresa las 1 materia que quieres agregar\n")
                                while modulo4Agregar2 not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM4"]:
                                    modulo4Agregar2=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")

                                archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][3].append(modulo4Agregar2)


                                system("clear")

                                print("-----Materias del modulo 5-----")#se muestran las materias que hay para el modulo 3
                                for i in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM5"])):
                                    print(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM5"][i])
                                
                                modulo5Agregar1=input("Ingresa las 1 materia que quieres agregar\n")
                                while modulo5Agregar1 not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM5"]:
                                    modulo5Agregar1=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")
                                
                                archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][4].append(modulo5Agregar1)
                                
                                modulo5Agregar2=input("Ingresa las 1 materia que quieres agregar\n")
                                while modulo5Agregar2 not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM5"]:
                                    modulo5Agregar2=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")

                                archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][4].append(modulo5Agregar2)

                                system("clear")

                                trainerHay=[]
                                print("-----Trainers-----")
                                for z in range(len(archivo["Trainers"])):
                                    print(archivo["Trainers"][z]["nombres"])
                                    if archivo["Trainers"][z]["nombres"] not in trainerHay:
                                        trainerHay.append(archivo["Trainers"][z]["nombres"])

                                trainerAgregar=input("Ingresa el trainer\n")
                                while trainerAgregar not in trainerHay:
                                    trainerAgregar=input("Ingresa un trainer valido (Tienes que escribirlo como aparece en Trainers)\n")

                            
                            confiInfor=input("¿Quieres cambiar algo mas? si/no\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")
                        
                        if opcCambioCamper==10:
                            if archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="cursando":
                                fechaCambio=input("¿Cual es la nueva fecha de inicio? (DD-MM-AAAA)\n")

                                archivo[personaCambiarInfo][posicionCamperCambiar]["fechaInicio"]=fechaCambio
                            else:
                                print("Este camper se encuentra en estado",archivo[personaCambiarInfo][posicionCamperCambiar]["estado"], "por lo tanto no tiene fecha de inicio")


                menuCoordinador()
                try:
                    opcMenuCoordinador=int(input("Ingresa tu opcion\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 7 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                except ValueError:
                    opcMenuCoordinador=int(input("Ingresa una opcion valida (Numero)\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 7 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla

            elif opcMenuCoordinador==3:


                menuCoordinador()
                try:
                    opcMenuCoordinador=int(input("Ingresa tu opcion\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 7 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                except ValueError:
                    opcMenuCoordinador=int(input("Ingresa una opcion valida (Numero)\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 7 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla

            elif opcMenuCoordinador==4:


                menuCoordinador()
                try:
                    opcMenuCoordinador=int(input("Ingresa tu opcion\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 7 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                except ValueError:
                    opcMenuCoordinador=int(input("Ingresa una opcion valida (Numero)\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 7 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla


            elif opcMenuCoordinador==5:


                menuCoordinador()
                try:
                    opcMenuCoordinador=int(input("Ingresa tu opcion\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 7 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                except ValueError:
                    opcMenuCoordinador=int(input("Ingresa una opcion valida (Numero)\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 7 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla

            elif opcMenuCoordinador==6:


                menuCoordinador()
                try:
                    opcMenuCoordinador=int(input("Ingresa tu opcion\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 7 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
                except ValueError:
                    opcMenuCoordinador=int(input("Ingresa una opcion valida (Numero)\n"))
                    while opcMenuCoordinador<1 or opcMenuCoordinador>7:
                            opcMenuCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))#se usa un bucle while para que cada vez que ingresen un numero mayor a 7 o menor a 1(que son las opciones validas) le diga que por favor ingrese una opcion de las que aparecen en pantalla
            
            elif opcMenuCoordinador==7:

                system("clear")
                print ("Gracias por usar el programa")

                bol1=False

    if x==0:
        user=input("No se encontro el usuario ingreselo nuevamente\n")



json_archivo=json.dumps(archivo)
with open("./Campusland.json","w") as files:
    files.write(json_archivo)
#Desarrollado por Luis Henao c.c. 1093904929 y Zully Ortiz c.c.1092528097
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
                    confirmacion="si"
                    while confirmacion=="si":
                        #Le mostrara el camper el submenu de la opcion uno 
                        menuCamperOpc1()
                        #El camper ingresara la opcion que desea observar 
                        
                        bol13=True
                        while bol13 == True:
                            try:
                                newOpc1=int(input("Ingrese una opcion del menu anterior:\n"))
                                while newOpc1<1 or newOpc1>5:
                                    newOpc1=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))
                                bol13=False
                            except ValueError:
                                print("Ingresa una opcion valida (Numero)\n")
                        system("clear")
                                                        
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
                            
                            confirmacion=input("Si quieres ver otro reporte escribe: si, de lo contrario preciona enter\n")
                            system("clear")

                        elif newOpc1==2:
                            if archivo["Campers"][i]["estado"]=="Aprobado" or archivo["Campers"][i]["estado"]=="Cursando": 
                                # Si en las posiciones del camper se encuentra el estado aprobado o cursando se le mstrata al camper.   
                                print("Tu riesgo es:",archivo["Campers"][i]["riesgo"])#Se le mostrara al camper el riesgos que se encuentra
                            else:#Si el camper no se encuentra en aprobado o cursando se le mostrara en que estado se encuentra y se le aclarará que no tienes riesgo por lo mismo.
                                print("Tu estado es:",archivo["Campers"][i]["estado"],"por lo tanto no tienes riesgo")

                            confirmacion=input("Si quieres ver otro reporte escribe: si, de lo contrario preciona enter\n")
                            system("clear")

                        #Si la opcion elegida es tres se hara:
                        elif newOpc1==3:
                            print("Tu ruta es:",archivo["Campers"][i]["ruta"])#Se le mostara la ruta en el que se encuentra el camper

                            confirmacion=input("Si quieres ver otro reporte escribe: si, de lo contrario preciona enter\n")
                            system("clear")
                        #Si la opcion elegida del camper es cuatro se hara: 
                        elif newOpc1==4:
                            print("Tu trainer es:",archivo["Campers"][i]["trainer"])#Se le mostrara el trainer del camper

                            confirmacion=input("Si quieres ver otro reporte escribe: si, de lo contrario preciona enter\n")
                            system("clear")
                        #Si la opcion elegida es cinco se hara:
                        elif newOpc1==5:
                            print("El modulo que te encuentras actualmente es:",archivo["Campers"][i]["moduloActual"],archivo["Campers"][i]["numeroModulo"][archivo["Campers"][i]["moduloActual"]-1])#SSe mostrara el modulo que se encuentra actualmente el camper

                            confirmacion=input("Si quieres ver otro reporte escribe: si, de lo contrario preciona enter\n")
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
                    
                    bol14=True
                    while bol14==True:
                        try:
                            numOpc=int(input("Ingrese una de las opciones del menu anterior\n"))#El ingresara la opcione que desee realizar del menu anterior 
                            while numOpc<1 or numOpc>3:
                                numOpc=int(input("Ingrese una opcion de la que aparece en la pantalla.\n"))
                            bol14=False
                        except ValueError:
                            print("Ingresa una opcion valida (Numero)\n")
                    system("clear")
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
                                print("Ingrese un telefono movil valido (solo numeros)\n")#el camper ingresara el nuevo telefono movil

                        archivo["Campers"][i]["telefonoCelular"]=newPhone#Ingresara en las posiciones del camper y ingresara donde esta el telefono movil y asi se guardara el cambio del nuevo dato ingresado.

                    elif numOpc==3:#Si la opcion elegida es tres se hara:
                        bol8=True#este boleano es para que el valor a ingresar a pantalla sea numero si no es numero se volvera a repetir el bucle y no le permitira seguir.
                        while bol8==True:
                            try:
                                newFijo=int(input("Ingrese el nuevo telefono fijo\n"))#el camper ingresara el nuevo telefono fijo
                                bol8=False
                            except ValueError:
                                print("Ingrese un telefono fijo valido(solo numeros)\n")#Si el camper ingresa alguna letra se le notificara y se le recordara que solo se acepta numero y se volvera a repetir 

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
                    print("La ruta de entrenamiento es",archivo["Trainers"][q]["ruta"])
                    
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
                    bol15=True
                    while bol15==True:
                        try:
                            newOpc=int(input("Ingrese unas de las opciones del menu anterior:\n"))#Ingresara una opcion del submenu anterior
                            while newOpc<1 or newOpc>3:
                                newOpc=int(input("Ingrese una opcion de las que aparecen en la pantalla:\n"))
                            bol15=False
                        except ValueError:
                            print("Ingrese una opcion valida(Número)\n")
                    system("clear")

                    
                    if newOpc==1: #Si la opcion es uno se hara:
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
                                print("Ingrese un telefono movil valido(solo numeros)\n")
                        archivo["Trainers"][q]["telefonoCelular"]=newPhone1#En las posiciones del trainer en la posicion del telefono celular se guardara el dato que ingreso en trainer
                    #Si la opcion elegida es tres se hara: 
                    elif newOpc==3:
                        bol11=True#este booleano es por que el dato a ingresar debe ser entero por ende si el trainer ingresa una letra no se le aceptara y se le volvera a repetir el valor a ingresar hasta que no lo ingrese bien el bucle no parará.
                        while bol11==True:
                            try:
                                newFijo1=int(input("Ingrese el nuevo telefono fijo:\n"))#El trainer ingresara el nuevo telefono fijo
                                bol11=False
                            except ValueError:
                                print("Ingrese un telefono fijo valido (solo numeros)\n")
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
                print("-----",personaCambiar,"-----")
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
                if personaCambiarInfo=="Campers":

                    print("-----Campers-----")
                    for r in range(len(archivo[personaCambiarInfo])):#este for se usa solo para que mire todas las personas que hay en el tipo de usuario quiere el cambiar (ejemplo: Campers)
                        print("------------------")
                        print("Nombre:",archivo[personaCambiarInfo][r]["nombres"]) #siguiendo con el ejemplo le muestra todos los nombres que hay en Campers ya que recorre cada uno con el bucle for
                        print("ID:",archivo[personaCambiarInfo][r]["id"])#siguiendo con el ejemplo le muestra todos los id que hay en Campers ya que recorre cada uno con el bucle for
                        print("------------------\n")

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
                        print("Datos por cambiar\n1. ID\n2. Numero de Identificacion\n3. Nombres\n4. Apellidos\n5. Direccion\n6. Acudiente\n7. Telefono Celular\n8. Telefono fijo\n9. Estado\n\nLa siguiente informacion solo es valida para usuarios que ya estan cursando\n\n10. Fecha de inicio\n11. Fecha de cierre\n12. grupo\n13. Modulo actual\n14. Modulos\n15. Trainer\n16. Ruta\n17. Volver al menu anterior ")

                        #esta es la manera en la que se puede hacer repetir un error 
                        bol24=True
                        while bol24==True:
                            try:

                                opcCambioCamper=int(input("¿Que dato quieres cambiar?:\n"))
                                while opcCambioCamper<1 or opcCambioCamper>17:#este while es para que ingrese una opcion de las que hay en pantalla 
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

                            confiInfor=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
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

                            confiInfor=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")

                        elif opcCambioCamper==3:

                            nombreCambiar=input("Ingresa los nuevos nombres\n")

                            archivo[personaCambiarInfo][posicionCamperCambiar]["nombres"]=nombreCambiar #se preguntan los nuevos nombres y remplaza al que ya esta  

                            confiInfor=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")

                        elif opcCambioCamper==4:

                            apellidoCambiar=input("Ingresa los nuevos apellidos\n")

                            archivo[personaCambiarInfo][posicionCamperCambiar]["apellidos"]=apellidoCambiar #se preguntan los nuevos apellidos y remplaza al que ya esta  

                            confiInfor=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")

                        elif opcCambioCamper==5:

                            direccionCambiar=input("Ingresa la nueva direccion\n")

                            archivo[personaCambiarInfo][posicionCamperCambiar]["direccion"]=direccionCambiar #se pregunta la nueva direccion y remplaza al que ya esta  

                            confiInfor=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")

                        elif opcCambioCamper==6:

                            acudienteCambiar=input("Ingresa los nuevos nombres y apellidos del acudiente\n")

                            archivo[personaCambiarInfo][posicionCamperCambiar]["acudiente"]=acudienteCambiar #se preguntan los nuevos nombres y apellidos del acudiente y remplaza al que ya esta  

                            confiInfor=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
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

                            confiInfor=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
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

                            confiInfor=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")

                        elif opcCambioCamper==9:
                            
                            print("-----Tipos de estado-----")
                            for a in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeEstados"])):#se muestran los tipos de estado con unbucle for
                                print(archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeEstados"][a])
                            
                            estadoCambiar=input("¿Cual es el nuevo estado?\n")#se pregunta cual es el nuevo estado y se guarda en la variable estadoCambiar

                            while estadoCambiar not in archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeEstados"]: #mientras que el estado ingresado por el usuario no este en los tipos de estados le pedira que ingrese un estado valido 
                                estadoCambiar=input("Ingrese un estado valido (Tienes que escribirlo como aparece en los tipos de estado)\n")

                            archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=estadoCambiar# Como ya se sabe cual es el nuevo estado que quiere solo se remplaza el que ya estaba por el que ingreso el usuario

                            if estadoCambiar=="Aprobado":#si el usuario puso de nuevo estado aprovado se tienen que llenar otra informacion ya que ahora pertenece a campusland

                                print("Como el estado del estudiante ahora es Aprobado tienes que llenar la siguiente informacion:")

                                agregarFechaInicio=input("Ingrese una fecha de inicio (DD-MM-AAAA)\n")#se pide y se agrega la fecha de inicio
                                archivo[personaCambiarInfo][posicionCamperCambiar]["fechaInicio"]=agregarFechaInicio

                                system("clear")
                                agregarFechaCierre=input("Ingrese una fecha de cierre (DD-MM-AAAA)\n")#se pide y se agrega la fecha de cierre
                                archivo[personaCambiarInfo][posicionCamperCambiar]["fechaCierre"]=agregarFechaCierre

                                system("clear")
                                agregarGrupo=input("Ingrese el grupo al que va a pertenecer el Camper\n")#Se pregunta el grupo al que va a pertenecer y se agrega 
                                archivo[personaCambiarInfo][posicionCamperCambiar]["grupo"]=agregarGrupo

                                system("clear")
                                print("-----Tipos de Rutas-----")
                                for y in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeRutas"])):#se muestran todos los tipos de rutas que hay 
                                    print(archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeRutas"][y])
                                
                                rutaAgregar=input("Ingresa una ruta\n")#se pide la tura a agregar

                                while rutaAgregar not in archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeRutas"]:
                                    #mientras que la ruta que agregue no este en tiposDeRutas 
                                    rutaAgregar=input("Ingresa una ruta valida (Tienes que escribirlo como aparece en los tipos de rutas)\n")

                                archivo[personaCambiarInfo][posicionCamperCambiar]["ruta"]=rutaAgregar#despues de haber dicho la ruta que quiere se agrega a ruta

                                system("clear")
                                archivo[personaCambiarInfo][posicionCamperCambiar]["moduloActual"]=1#se pone que el modulo actual es igual a 1 ya que como apenas esta empezando empieza en el modulo 1

                                #solo los modulos 3, 4 y 5 se pueden escoger las materias por lo tanto son las unicas que se piden 

                                print("-----Materias del modulo 3-----")#se muestran las materias que hay para el modulo 3
                                for i in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM3"])):
                                    print(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM3"][i])
                                
                                #como se pueden agregar 2 materias se piden solo 2
                                modulo3Agregar1=input("Ingresa las 1 materia que quieres agregar\n")#se pide la primera materia del modulo tres 

                                while modulo3Agregar1 not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM3"]:# mientras la materia ingresada no se encuentre en materiasM3 se le pedire que ingrese una materia valida  
                                    modulo3Agregar1=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")
                                
                                archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][2].append(modulo3Agregar1)
                                
                                modulo3Agregar2=input("Ingresa las 2 materia que quieres agregar\n")#se pide la segunda materia del modulo tres 
                                while modulo3Agregar2 not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM3"]:# mientras la materia ingresada no se encuentre en materiasM3 se le pedire que ingrese una materia valida  
                                    modulo3Agregar2=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")

                                archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][2].append(modulo3Agregar2)

                                system("clear")

                                #como se pueden agregar 2 materias se piden solo 2
                                print("-----Materias del modulo 4-----")#se muestran las materias que hay para el modulo 4
                                for i in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM4"])):
                                    print(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM4"][i])
                                
                                modulo4Agregar1=input("Ingresa las 1 materia que quieres agregar\n")#se pide la primera materia del modulo 4
                                while modulo4Agregar1 not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM4"]:# mientras la materia ingresada no se encuentre en materiasM3 se le pedire que ingrese una materia valida  
                                    modulo4Agregar1=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")
                                
                                archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][3].append(modulo4Agregar1)
                                
                                modulo4Agregar2=input("Ingresa las 2 materia que quieres agregar\n")#se pide la segunda materia del modulo 4
                                while modulo4Agregar2 not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM4"]:# mientras la materia ingresada no se encuentre en materiasM3 se le pedire que ingrese una materia valida  
                                    modulo4Agregar2=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")

                                archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][3].append(modulo4Agregar2)


                                system("clear")

                                #como se pueden agregar 2 materias se piden solo 2
                                print("-----Materias del modulo 5-----")#se muestran las materias que hay para el modulo 5
                                for i in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM5"])):
                                    print(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM5"][i])
                                
                                modulo5Agregar1=input("Ingresa las 1 materia que quieres agregar\n")#se pide la primera materia del modulo 5
                                while modulo5Agregar1 not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM5"]:# mientras la materia ingresada no se encuentre en materiasM3 se le pedire que ingrese una materia valida  
                                    modulo5Agregar1=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")
                                
                                archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][4].append(modulo5Agregar1)
                                
                                modulo5Agregar2=input("Ingresa las 2 materia que quieres agregar\n")#se pide la segunda materia del modulo 5
                                while modulo5Agregar2 not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM5"]:# mientras la materia ingresada no se encuentre en materiasM3 se le pedire que ingrese una materia valida  
                                    modulo5Agregar2=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")

                                archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][4].append(modulo5Agregar2)

                                system("clear")

                                trainerHay=[]#en esta lista se guardaran los nombres de los trainers que hay
                                print("-----Trainers-----")
                                for z in range(len(archivo["Trainers"])):#con este bucle for se muestran los nombres de los trainers que hay 
                                    print(archivo["Trainers"][z]["nombres"])
                                    if archivo["Trainers"][z]["nombres"] not in trainerHay:#si el nombre del trainer no esta en la lista trainerHay se agrega y si esta solo lo ignora 
                                        trainerHay.append(archivo["Trainers"][z]["nombres"])

                                trainerAgregar=input("Ingresa el trainer\n")
                                while trainerAgregar not in trainerHay:
                                    trainerAgregar=input("Ingresa un trainer valido (Tienes que escribirlo como aparece en Trainers)\n")

                                archivo[personaCambiarInfo][posicionCamperCambiar]["trainer"]=trainerAgregar
                            
                            elif estadoCambiar=="Cursando" and archivo[personaCambiarInfo][posicionCamperCambiar]["fechaInicio"]=="":#si el estado ingresado es Cursando y en la fecha de inicio no hay nada se tienen que llenar unos datos (se mira si la fecha de inicio esta vacia por si el estado pasa de estado Incrito directamente a Aprobado(esto solo es un ejemplo))

                                #si el usuario puso de nuevo estado aprovado se tienen que llenar otra informacion ya que ahora pertenece a campusland

                                print("Como el estado del estudiante ahora es Cursando tienes que llenar la siguiente informacion:")

                                agregarFechaInicio=input("Ingrese una fecha de inicio (DD-MM-AAAA)\n")#se pide y se agrega la fecha de inicio
                                archivo[personaCambiarInfo][posicionCamperCambiar]["fechaInicio"]=agregarFechaInicio

                                system("clear")
                                agregarFechaCierre=input("Ingrese una fecha de cierre (DD-MM-AAAA)\n")#se pide y se agrega la fecha de cierre
                                archivo[personaCambiarInfo][posicionCamperCambiar]["fechaCierre"]=agregarFechaCierre

                                system("clear")
                                agregarGrupo=input("Ingrese el grupo al que va a pertenecer el Camper\n")#Se pregunta el grupo al que va a pertenecer y se agrega 
                                archivo[personaCambiarInfo][posicionCamperCambiar]["grupo"]=agregarGrupo

                                system("clear")
                                print("-----Tipos de Rutas-----")
                                for y in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeRutas"])):#se muestran todos los tipos de rutas que hay 
                                    print(archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeRutas"][y])
                                
                                rutaAgregar=input("Ingresa una ruta\n")#se pide la tura a agregar

                                while rutaAgregar not in archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeRutas"]:
                                    #mientras que la ruta que agregue no este en tiposDeRutas 
                                    rutaAgregar=input("Ingresa una ruta valida (Tienes que escribirlo como aparece en los tipos de rutas)\n")

                                archivo[personaCambiarInfo][posicionCamperCambiar]["ruta"]=rutaAgregar#despues de haber dicho la ruta que quiere se agrega a ruta

                                system("clear")
                                archivo[personaCambiarInfo][posicionCamperCambiar]["moduloActual"]=1#se pone que el modulo actual es igual a 1 ya que como apenas esta empezando empieza en el modulo 1

                                #solo los modulos 3, 4 y 5 se pueden escoger las materias por lo tanto son las unicas que se piden 

                                print("-----Materias del modulo 3-----")#se muestran las materias que hay para el modulo 3
                                for i in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM3"])):
                                    print(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM3"][i])
                                
                                #como se pueden agregar 2 materias se piden solo 2
                                modulo3Agregar1=input("Ingresa las 1 materia que quieres agregar\n")#se pide la primera materia del modulo tres 

                                while modulo3Agregar1 not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM3"]:# mientras la materia ingresada no se encuentre en materiasM3 se le pedire que ingrese una materia valida  
                                    modulo3Agregar1=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")
                                
                                archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][2].append(modulo3Agregar1)
                                
                                modulo3Agregar2=input("Ingresa las 2 materia que quieres agregar\n")#se pide la segunda materia del modulo tres 
                                while modulo3Agregar2 not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM3"]:# mientras la materia ingresada no se encuentre en materiasM3 se le pedire que ingrese una materia valida  
                                    modulo3Agregar2=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")

                                archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][2].append(modulo3Agregar2)

                                system("clear")

                                #como se pueden agregar 2 materias se piden solo 2
                                print("-----Materias del modulo 4-----")#se muestran las materias que hay para el modulo 4
                                for i in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM4"])):
                                    print(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM4"][i])
                                
                                modulo4Agregar1=input("Ingresa las 1 materia que quieres agregar\n")#se pide la primera materia del modulo 4
                                while modulo4Agregar1 not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM4"]:# mientras la materia ingresada no se encuentre en materiasM3 se le pedire que ingrese una materia valida  
                                    modulo4Agregar1=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")
                                
                                archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][3].append(modulo4Agregar1)
                                
                                modulo4Agregar2=input("Ingresa las 2 materia que quieres agregar\n")#se pide la segunda materia del modulo 4
                                while modulo4Agregar2 not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM4"]:# mientras la materia ingresada no se encuentre en materiasM3 se le pedire que ingrese una materia valida  
                                    modulo4Agregar2=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")

                                archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][3].append(modulo4Agregar2)


                                system("clear")

                                #como se pueden agregar 2 materias se piden solo 2
                                print("-----Materias del modulo 5-----")#se muestran las materias que hay para el modulo 5
                                for i in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM5"])):
                                    print(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM5"][i])
                                
                                modulo5Agregar1=input("Ingresa las 1 materia que quieres agregar\n")#se pide la primera materia del modulo 5
                                while modulo5Agregar1 not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM5"]:# mientras la materia ingresada no se encuentre en materiasM3 se le pedire que ingrese una materia valida  
                                    modulo5Agregar1=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")
                                
                                archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][4].append(modulo5Agregar1)
                                
                                modulo5Agregar2=input("Ingresa las 2 materia que quieres agregar\n")#se pide la segunda materia del modulo 5
                                while modulo5Agregar2 not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM5"]:# mientras la materia ingresada no se encuentre en materiasM3 se le pedire que ingrese una materia valida  
                                    modulo5Agregar2=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")

                                archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][4].append(modulo5Agregar2)


                                
                                system("clear")

                                trainerHay=[]#en esta lista se guardaran los nombres de los trainers que hay
                                print("-----Trainers-----")
                                for z in range(len(archivo["Trainers"])):#con este bucle for se muestran los nombres de los trainers que hay 
                                    print(archivo["Trainers"][z]["nombres"])
                                    if archivo["Trainers"][z]["nombres"] not in trainerHay:#si el nombre del trainer no esta en la lista trainerHay se agrega y si esta solo lo ignora 
                                        trainerHay.append(archivo["Trainers"][z]["nombres"])

                                trainerAgregar=input("Ingresa el trainer\n")
                                while trainerAgregar not in trainerHay:
                                    trainerAgregar=input("Ingresa un trainer valido (Tienes que escribirlo como aparece en Trainers)\n")
                                
                                archivo[personaCambiarInfo][posicionCamperCambiar]["trainer"]=trainerAgregar

                            
                            confiInfor=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")
                        
                        elif opcCambioCamper==10:
                            if archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Aprobado":
                                fechaCambio=input("¿Cual es la nueva fecha de inicio? (DD-MM-AAAA)\n")

                                archivo[personaCambiarInfo][posicionCamperCambiar]["fechaInicio"]=fechaCambio
                            
                            elif archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Cursando":

                                fechaCambio=input("¿Cual es la nueva fecha de inicio? (DD-MM-AAAA)\n")

                                archivo[personaCambiarInfo][posicionCamperCambiar]["fechaInicio"]=fechaCambio
                            
                        
                            else:
                                print("Este camper se encuentra en estado",archivo[personaCambiarInfo][posicionCamperCambiar]["estado"], "por lo tanto no tiene fecha de inicio")

                            confiInfor=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")
                        
                        elif opcCambioCamper==11:

                            if archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Aprobado":
                                fechaCierreCambio=input("¿Cual es la nueva fecha de cierre? (DD-MM-AAAA)\n")

                                archivo[personaCambiarInfo][posicionCamperCambiar]["fechaCierre"]=fechaCierreCambio
                            
                            elif archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Cursando":

                                fechaCierreCambio=input("¿Cual es la nueva fecha de cierre? (DD-MM-AAAA)\n")

                                archivo[personaCambiarInfo][posicionCamperCambiar]["fechaCierre"]=fechaCierreCambio
                            
                        
                            else:
                                print("Este camper se encuentra en estado",archivo[personaCambiarInfo][posicionCamperCambiar]["estado"], "por lo tanto no tiene fecha de inicio")


                            confiInfor=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")


                        elif opcCambioCamper==12:
                            if archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Aprobado":

                                grupoCambiar=input("¿Cual es el nuevo grupo?\n")
                                archivo[personaCambiarInfo][posicionCamperCambiar]["grupo"]=grupoCambiar
                            
                            elif archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Cursando":

                                grupoCambiar=input("¿Cual es el nuevo grupo?\n")
                                archivo[personaCambiarInfo][posicionCamperCambiar]["grupo"]=grupoCambiar
                            
                            else:
                                print("Este camper se encuentra en estado",archivo[personaCambiarInfo][posicionCamperCambiar]["estado"], "por lo tanto no tiene grupo")


                            confiInfor=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")


                        elif opcCambioCamper==13:

                            if archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Aprobado":
                                print("----Modulos-----")
                                for s in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["numeroModulo"])):#se muestran los modulos que hay 
                                    print(s+1,archivo[personaCambiarInfo][posicionCamperCambiar]["numeroModulo"][s])

                                #esta es la manera para pedir un entreo y en caso de error se pueda repetir 
                                bol29=True
                                while bol29==True:
                                    try:
                                        moduloActualCambiar=int(input("¿Cual es el nuevo modulo actual? (Ingrese el numero del modulo)\n"))
                                        while moduloActualCambiar<1 or moduloActualCambiar>5:
                                            moduloActualCambiar=int(input("Ingresa un modulo valido (Entre 1 y 5 que son los que apareren en pantalla)\n"))
                                        bol29=False
                                    
                                    except ValueError:
                                        print("Ingresa un modulo valido (Numero)")
                                
                                archivo[personaCambiarInfo][posicionCamperCambiar]["moduloActual"]=moduloActualCambiar#despues de haber pedido el nuevo modulo actual se reemplaza por el que ya estaba
                            
                            elif archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Cursando":

                                print("----Modulos-----")
                                for s in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["numeroModulo"])):#se muestran los modulos que hay 
                                    print(s+1,archivo[personaCambiarInfo][posicionCamperCambiar]["numeroModulo"][s])

                                #esta es la manera para pedir un entreo y en caso de error se pueda repetir 
                                bol29=True
                                while bol29==True:
                                    try:
                                        moduloActualCambiar=int(input("¿Cual es el nuevo modulo actual? (Ingrese el numero del modulo)\n"))
                                        while moduloActualCambiar<1 or moduloActualCambiar>5:
                                            moduloActualCambiar=int(input("Ingresa un modulo valido (Entre 1 y 5 que son los que apareren en pantalla)\n"))
                                        bol29=False
                                    
                                    except ValueError:
                                        print("Ingresa un modulo valido (Numero)")
                                
                                archivo[personaCambiarInfo][posicionCamperCambiar]["moduloActual"]=moduloActualCambiar#despues de haber pedido el nuevo modulo actual se reemplaza por el que ya estaba

                            else:
                                print("Este camper se encuentra en estado",archivo[personaCambiarInfo][posicionCamperCambiar]["estado"], "por lo tanto no tiene modulo actual")

                            

                            confiInfor=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")
                        

                        elif opcCambioCamper==14:

                            if archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Aprobado":
                                print("----Modulos que se pueden cambiar-----")
                                for s in range(2,len(archivo[personaCambiarInfo][posicionCamperCambiar]["numeroModulo"])):#se muestran los modulos que hay 
                                    print(s+1,archivo[personaCambiarInfo][posicionCamperCambiar]["numeroModulo"][s])
                                
                                bol30=True
                                while bol30==True:
                                    try:
                                        moduloCambiar=int(input("¿En que modulo quieres cambiar materias? (Ingresa el numero)\n"))
                                        while moduloCambiar<3 or moduloCambiar>5:
                                            moduloCambiar=int(input("Ingresa un modulo de los que aparecen en pantalla\n")) 
                                        bol30=False
                                    
                                    except ValueError:
                                        print("Ingresa un modulo valido (Numero)")
                                
                                if moduloCambiar==3:
                                    print("-----Materias del modulo 3-----")
                                    for h in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM3"])):
                                        print(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM3"][h])
                                    materiaModulo3Cambiar=input("Ingresa la primera nueva materia del 3 modulo\n")
                                    while materiaModulo3Cambiar not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM3"]:
                                        materiaModulo3Cambiar=input("Ingresa una materia valida (Tienes que escribirla como aparece en pantalla)\n")

                                    archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][2]=[]#aca vaciamos la lista para poder añadir las nuevas materias
                                    archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][2].append(materiaModulo3Cambiar)

                                    materiaModulo3Cambiar=input("Ingresa la segunda nueva materia del 3 modulo\n")
                                    while materiaModulo3Cambiar not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM3"]:
                                        materiaModulo3Cambiar=input("Ingresa una materia valida (Tienes que escribirla como aparece en pantalla)\n")
                                    
                                    archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][2].append(materiaModulo3Cambiar)
                                
                                elif moduloCambiar==4:
                                    print("-----Materias del modulo 4-----")
                                    for h in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM4"])):

                                        print(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM4"][h])

                                    materiaModulo4Cambiar=input("Ingresa la primera nueva materia del 4 modulo\n")
                                    while materiaModulo4Cambiar not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM4"]:
                                        materiaModulo4Cambiar=input("Ingresa una materia valida (Tienes que escribirla como aparece en pantalla)\n")

                                    archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][3]=[]#aca vaciamos la lista para poder añadir las nuevas materias
                                    archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][3].append(materiaModulo4Cambiar)

                                    materiaModulo4Cambiar=input("Ingresa la segunda nueva materia del 4 modulo\n")
                                    while materiaModulo4Cambiar not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM4"]:
                                        materiaModulo4Cambiar=input("Ingresa una materia valida (Tienes que escribirla como aparece en pantalla)\n")
                                    
                                    archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][3].append(materiaModulo4Cambiar)
                                
                                elif moduloCambiar==5:
                                    print("-----Materias del modulo 5-----")

                                    for h in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM5"])):
                                        print(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM5"][h])

                                    materiaModulo5Cambiar=input("Ingresa la primera nueva materia del 5 modulo\n")
                                    while materiaModulo5Cambiar not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM5"]:
                                        materiaModulo5Cambiar=input("Ingresa una materia valida (Tienes que escribirla como aparece en pantalla)\n")

                                    archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][4]=[]#aca vaciamos la lista para poder añadir las nuevas materias
                                    archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][4].append(materiaModulo5Cambiar)

                                    materiaModulo5Cambiar=input("Ingresa la segunda nueva materia del 5 modulo\n")
                                    while materiaModulo5Cambiar not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM5"]:
                                        materiaModulo5Cambiar=input("Ingresa una materia valida (Tienes que escribirla como aparece en pantalla)\n")
                                    
                                    archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][4].append(materiaModulo5Cambiar)

                            
                            
                            elif archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Cursando":

                                print("----Modulos que se pueden cambiar-----")
                                for s in range(2,len(archivo[personaCambiarInfo][posicionCamperCambiar]["numeroModulo"])):#se muestran los modulos que hay 
                                    print(s+1,archivo[personaCambiarInfo][posicionCamperCambiar]["numeroModulo"][s])
                                
                                bol30=True
                                while bol30==True:
                                    try:
                                        moduloCambiar=int(input("¿En que modulo quieres cambiar materias? (Ingresa el numero)\n"))
                                        while moduloCambiar<3 or moduloCambiar>5:
                                            moduloCambiar=int(input("Ingresa un modulo de los que aparecen en pantalla\n")) 
                                        bol30=False
                                    
                                    except ValueError:
                                        print("Ingresa un modulo valido (Numero)")
                                
                                if moduloCambiar==3:
                                    print("-----Materias del modulo 3-----")
                                    for h in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM3"])):
                                        print(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM3"][h])
                                    materiaModulo3Cambiar=input("Ingresa la primera nueva materia del 3 modulo\n")
                                    while materiaModulo3Cambiar not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM3"]:
                                        materiaModulo3Cambiar=input("Ingresa una materia valida (Tienes que escribirla como aparece en pantalla)\n")

                                    archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][2]=[]#aca vaciamos la lista para poder añadir las nuevas materias
                                    archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][2].append(materiaModulo3Cambiar)

                                    materiaModulo3Cambiar=input("Ingresa la segunda nueva materia del 3 modulo\n")
                                    while materiaModulo3Cambiar not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM3"]:
                                        materiaModulo3Cambiar=input("Ingresa una materia valida (Tienes que escribirla como aparece en pantalla)\n")
                                    
                                    archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][2].append(materiaModulo3Cambiar)
                                
                                elif moduloCambiar==4:
                                    print("-----Materias del modulo 4-----")
                                    for h in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM4"])):

                                        print(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM4"][h])

                                    materiaModulo4Cambiar=input("Ingresa la primera nueva materia del 4 modulo\n")
                                    while materiaModulo4Cambiar not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM4"]:
                                        materiaModulo4Cambiar=input("Ingresa una materia valida (Tienes que escribirla como aparece en pantalla)\n")

                                    archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][3]=[]#aca vaciamos la lista para poder añadir las nuevas materias
                                    archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][3].append(materiaModulo4Cambiar)

                                    materiaModulo4Cambiar=input("Ingresa la segunda nueva materia del 4 modulo\n")
                                    while materiaModulo4Cambiar not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM4"]:
                                        materiaModulo4Cambiar=input("Ingresa una materia valida (Tienes que escribirla como aparece en pantalla)\n")
                                    
                                    archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][3].append(materiaModulo4Cambiar)
                                
                                elif moduloCambiar==5:
                                    print("-----Materias del modulo 5-----")

                                    for h in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM5"])):
                                        print(archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM5"][h])

                                    materiaModulo5Cambiar=input("Ingresa la primera nueva materia del 5 modulo\n")
                                    while materiaModulo5Cambiar not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM5"]:
                                        materiaModulo5Cambiar=input("Ingresa una materia valida (Tienes que escribirla como aparece en pantalla)\n")

                                    archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][4]=[]#aca vaciamos la lista para poder añadir las nuevas materias
                                    archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][4].append(materiaModulo5Cambiar)

                                    materiaModulo5Cambiar=input("Ingresa la segunda nueva materia del 5 modulo\n")
                                    while materiaModulo5Cambiar not in archivo[personaCambiarInfo][posicionCamperCambiar]["materiasM5"]:
                                        materiaModulo5Cambiar=input("Ingresa una materia valida (Tienes que escribirla como aparece en pantalla)\n")
                                    
                                    archivo[personaCambiarInfo][posicionCamperCambiar]["modulos"][4].append(materiaModulo5Cambiar)
                                
                            
                            else:
                                print("Este camper se encuentra en estado",archivo[personaCambiarInfo][posicionCamperCambiar]["estado"], "por lo tanto no tiene modulo actual")
                            
                            confiInfor=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")
                        
                        if opcCambioCamper==15:
                            
                            if archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Aprobado":
                                trainerHayCambiar=[]
                                print("-----Trainers-----")
                                for p in range(len(archivo["Trainers"])):#se muestran los nombres de los trainers y se agregan a la lista trainerHayCambiar
                                    print(archivo["Trainers"][p]["nombres"])
                                    if archivo["Trainers"][p]["nombres"] not in trainerHayCambiar:
                                        trainerHayCambiar.append(archivo["Trainers"][p]["nombres"])
                                
                                trainerCambiar=input("¿Cual es el nuevo trainer?\n")#se pregunta cual sera el nuevo trainer 

                                while trainerCambiar not in trainerHayCambiar:#mientras el nuevo trainer no este en la lista trainerHayCambiar se le pedira que ingrese un trainer valido
                                    trainerCambiar=input("Ingrese un trainer valido (Tiene que escribirlo como aparece en pantalla)\n")
                                
                                archivo[personaCambiarInfo][posicionCamperCambiar]["trainer"]=trainerCambiar#despues de saber cual es el nuevo trainer remplaza al que ya estaba
                            
                            elif archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Cursando":

                                trainerHayCambiar=[]
                                print("-----Trainers-----")
                                for p in range(len(archivo["Trainers"])):#se muestran los nombres de los trainers y se agregan a la lista trainerHayCambiar
                                    print(archivo["Trainers"][p]["nombres"])
                                    if archivo["Trainers"][p]["nombres"] not in trainerHayCambiar:
                                        trainerHayCambiar.append(archivo["Trainers"][p]["nombres"])
                                
                                trainerCambiar=input("¿Cual es el nuevo trainer?\n")#se pregunta cual sera el nuevo trainer 

                                while trainerCambiar not in trainerHayCambiar:#mientras el nuevo trainer no este en la lista trainerHayCambiar se le pedira que ingrese un trainer valido
                                    trainerCambiar=input("Ingrese un trainer valido (Tiene que escribirlo como aparece en pantalla)\n")
                                
                                archivo[personaCambiarInfo][posicionCamperCambiar]["trainer"]=trainerCambiar#despues de saber cual es el nuevo trainer remplaza al que ya estaba


                            else:
                                print("Este camper se encuentra en estado",archivo[personaCambiarInfo][posicionCamperCambiar]["estado"], "por lo tanto no tiene Trainer")
                            
                            confiInfor=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")
                        
                        if opcCambioCamper==16:

                            if archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Aprobado":
                                
                                for g in range(len( archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeRutas"])):
                                    print(archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeRutas"][g])
                                
                                rutaCambiar=input("¿Cual es la nueva ruta?\n")
                                while rutaCambiar not in archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeRutas"]:
                                    rutaCambiar=input("Ingrese un ruta valida (Tienes que ecribirla como aparece en pantalla)\n")


                                archivo[personaCambiarInfo][posicionCamperCambiar]["ruta"]=rutaCambiar


                            elif archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Cursando":

                                for g in range(len( archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeRutas"])):
                                    print(archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeRutas"][g])
                                
                                rutaCambiar=input("¿Cual es la nueva ruta?\n")
                                while rutaCambiar not in archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeRutas"]:
                                    rutaCambiar=input("Ingrese un ruta valida (Tienes que ecribirla como aparece en pantalla)\n")


                                archivo[personaCambiarInfo][posicionCamperCambiar]["ruta"]=rutaCambiar

                            
                            else:
                                print("Este camper se encuentra en estado",archivo[personaCambiarInfo][posicionCamperCambiar]["estado"], "por lo tanto no tiene Trainer")
                            
                            confiInfor=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")
                        
                        if opcCambioCamper==17:
                            system("clear")
                            confiInfor="no"

                if personaCambiarInfo=="Trainers":#si el usuario al que se le quiere cambiar la informacion es Trainers se hace lo siguiente
                    idTrainer=[]#en esta lista se guardaran todos los id de los trainer para saber si el id que ingrese esta en los trainers
                    print("-----Trainers-----")
                    for x in range(len(archivo["Trainers"])):
                        print("----------------------")
                        print("Nombre:",archivo["Trainers"][x]["nombres"])#se muestran los nombres de los trainers y el id 
                        print("ID:",archivo["Trainers"][x]["id"])        
                        print("----------------------")
                        if archivo["Trainers"][x]["id"] not in idTrainer:#mirando todas las pociciones de los trainers en el id si ese id no esta en idTrainer se agrega para asi tener todos los id que hay en trainers
                            idTrainer.append(archivo["Trainers"][x]["id"])

                    bol31=True
                    while bol31==True:
                        try:#se usa este try porque el id que se pide se pide en entero entonces en caso de que ingresen una letra le pueda mostrar un error 
                            idTrainerCambiar=int(input("Ingresa el ID del trainer a cambiar\n"))#se pide el id del trainer que quiere cambiar 
                            while idTrainerCambiar not in idTrainer:#mientras que el id de trainer no este en idTrainer se dice que id no encontrado y se pide que ingrese uno valido
                                idTrainerCambiar=int(input("ID no encontrado por favor escribe uno valido\n"))
                            bol31=False
                        except ValueError:
                            print("Por favor ingresa un ID valido (Solo numeros)")
                    
                    for b in range(len(archivo["Trainers"])):#depues de ver que el id si esta en los trainers se usa este bucle for para saber la posicion del trainer con ese id 
                        if idTrainerCambiar==archivo["Trainers"][b]["id"]:
                            posicionTrainerCambiar=b
                    
                    system("clear")
                        
                    

                    confiInforTrainer="si"
                    while confiInforTrainer=="si":

                        print("-----Informacion que se puede cambiar-----\n1. ID\n2. Numero de identificacion\n3. Nombres\n4. Apellidos\n5. Direccion\n6. Telefono Celular\n7. Telefono Fijo\n8. Ruta\n9. Volver al menu anterior ")
                    
                        bol32=True
                        while bol32==True:
                            try:
                                opcCambioTrainer=int(input("Ingresa tu opcion\n"))
                                while opcCambioTrainer<1 or opcCambioTrainer>9:
                                    opcCambioTrainer=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))
                                bol32=False
                            except ValueError:
                                print("Ingresa un opcion valida (Numero)")
                        
                        if opcCambioTrainer==1:

                            bol33=True
                            while bol33==True:
                                
                                try:
                                    idCambioTrainer=int(input("Ingresa el nuevo ID\n"))
                                    bol33=False
                                except ValueError:
                                    print("Ingresa un ID valido (Solo numeros)")
                            
                            archivo[personaCambiarInfo][posicionTrainerCambiar]["id"]=idCambioTrainer
                                
                            confiInforTrainer=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")
                            system("clear")
                        
                        elif opcCambioTrainer==2:

                            bol34=True
                            while bol34==True:
                                try:
                                    nidCambioTrainer=int(input("Ingresa el nuevo Numero de identificacion\n"))
                                    bol34=False
                                except ValueError:
                                    print("Ingresa un numero de identificadion valido (Solo numeros)")

                            archivo[personaCambiarInfo][posicionTrainerCambiar]["numeroIdentificacion"]= nidCambioTrainer

                            confiInforTrainer=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")
                            system("clear")
                        
                        elif opcCambioTrainer==3:

                            nombreCambioTrainer= input("Ingresa los nuevos nombres\n")

                            archivo[personaCambiarInfo][posicionTrainerCambiar]["nombres"]=nombreCambioTrainer

                            confiInforTrainer=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")
                            system("clear")
                        
                        elif opcCambioTrainer==4:

                            apellidoCambioTrainer=input("Ingresa los nuevos apellidos\n")

                            archivo[personaCambiarInfo][posicionTrainerCambiar]["apellidos"]=apellidoCambioTrainer

                            confiInforTrainer=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")
                            system("clear")
                        
                        elif opcCambioTrainer==5:

                            direccionCambioTrainer=input("Ingresa la nueva direccion\n")

                            archivo[personaCambiarInfo][posicionTrainerCambiar]["direccion"]=direccionCambioTrainer

                            confiInforTrainer=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")
                            system("clear")
                        
                        elif opcCambioTrainer==6:
                            
                            bol35=True
                            while bol35==True:
                                try:
                                    TelefonoCelularTrainerCambiar=int(input("Ingresa el nuevo numero de telefono celular\n"))
                                    bol35=False
                                except ValueError:
                                    print("Ingresa un numero de telefono valido (Solo numeros)")
                                
                            archivo[personaCambiarInfo][posicionTrainerCambiar]["telefonoCelular"]=TelefonoCelularTrainerCambiar

                            confiInforTrainer=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")
                            system("clear")

                        elif opcCambioTrainer==7:
                            
                            bol35=True
                            while bol35==True:
                                try:
                                    TelefonoFijoTrainerCambiar=int(input("Ingresa el nuevo numero de telefono fijo\n"))
                                    bol35=False
                                except ValueError:
                                    print("Ingresa un numero de telefono valido (Solo numeros)")
                                
                            archivo[personaCambiarInfo][posicionTrainerCambiar]["telefonoFijo"]=TelefonoFijoTrainerCambiar

                            confiInforTrainer=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")
                            system("clear")

                        elif opcCambioTrainer==8:

                            print("-----Tipos de rutas-----")
                            for p in range(len(archivo[personaCambiarInfo][posicionTrainerCambiar]["tiposDeRutas"])):
                                print(archivo[personaCambiarInfo][posicionTrainerCambiar]["tiposDeRutas"][p])

                            rutaTrainerCambiar=input("Ingrese la nueva ruta\n")

                            while rutaTrainerCambiar not in archivo[personaCambiarInfo][posicionTrainerCambiar]["tiposDeRutas"]:
                                
                                rutaTrainerCambiar=input("Ingrese una ruta valida (Tienes que escibirla como aparece en pantalla)\n")

                            archivo[personaCambiarInfo][posicionTrainerCambiar]["ruta"]=rutaTrainerCambiar

                            confiInforTrainer=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")
                            system("clear")
                        
                        elif opcCambioTrainer==9:
                            system("clear")

                            confiInforTrainer="no"

                if personaCambiarInfo=="Coordinador":

                    confiInforCoordinador="si"
                    while confiInforCoordinador=="si":

                        print("-----Informacion que se puede cambiar-----\n1. ID\n2. Numero de identificacion\n3. Nombres\n4. Apellidos\n5. Direccion\n6. Telefono Celular\n7. Telefono Fijo\n8. Volver al menu anterior ")


                        bol36=True
                        while bol36==True:
                            try:
                                opcCambioCoordinador=int(input("Ingresa tu opcion\n"))
                                while opcCambioCoordinador<1 or opcCambioCoordinador>8:
                                    opcCambioCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))
                                bol36=False
                            except ValueError:
                                print("Ingrese una opcion valida (Numero)")
                        
                        if opcCambioCoordinador==1:

                            bol37=True
                            while bol37==True:
                                try:
                                    idCambioCoordinador=int(input("Ingresa el nuevo ID\n"))
                                    bol37=False
                                except ValueError:
                                    print("Ingresa un ID valido (Solo numeros)")
                                
                            archivo["Coordinador"][0]["id"]=idCambioCoordinador

                            confiInforCoordinador=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")
                            system("clear")
                        
                        elif opcCambioCoordinador==2:

                            bol38=True
                            while bol38==True:
                                try:
                                    identificacionCambioCoordinador=int(input("Ingresa el nuevo numero de identificacion\n"))
                                    bol38=False
                                except ValueError:
                                    print("Ingresa un numero de identificaion valido (Solo numeros)")
                                
                            archivo["Coordinador"][0]["numeroIdentificacion"]=identificacionCambioCoordinador

                            confiInforCoordinador=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")
                            system("clear")

                        elif opcCambioCoordinador==3:

                            nombreCambioCoordinador=input("Ingresa los nuevos nombres del coordinador\n")

                            archivo["Coordinador"][0]["nombres"]=nombreCambioCoordinador

                            confiInforCoordinador=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")
                            system("clear")

                        elif opcCambioCoordinador==4:

                            apellidoCambioCoordinador=input("Ingresa los nuevos apellidos del coordinador\n")

                            archivo["Coordinador"][0]["apellidos"]=apellidoCambioCoordinador

                            confiInforCoordinador=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")
                            system("clear")
                        
                        elif opcCambioCoordinador==5:

                            direccionCambioCoordinador=input("Ingresa la nueva direccion\n")

                            archivo["Coordinador"][0]["direccion"]=direccionCambioCoordinador

                            confiInforCoordinador=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")
                            system("clear")

                        elif opcCambioCoordinador==6:

                            bol39=True
                            while bol39==True:
                                try:
                                    celularCambioCoordinador=int(input("Ingresa el nuevo numero de telefono celular\n"))
                                    bol39=False
                                except ValueError:
                                    print("Ingresa un numero de telefono valido (Solo numeros)")
                                
                            archivo["Coordinador"][0]["telefonoCelular"]=celularCambioCoordinador

                            confiInforCoordinador=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")
                            system("clear")
                        
                        elif opcCambioCoordinador==7:

                            bol40=True
                            while bol40==True:
                                try:
                                    fijoCambioCoordinador=int(input("Ingresa el nuevo numero de telefono fijo\n"))
                                    bol40=False
                                except ValueError:
                                    print("Ingresa un numero de telefono valido (Solo numeros)")
                                
                            archivo["Coordinador"][0]["telefonoFijo"]=fijoCambioCoordinador

                            confiInforCoordinador=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")
                            system("clear")

                        elif opcCambioCoordinador==8:

                            confiInforCoordinador=""
                            system("clear")
                            
                             
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

                system("clear")
                
                idCamperNota=[]
                print("-----Campers-----")#se muestran los campers con sus id y guarda los id en la lista idCAmperNota
                for f in range(len(archivo["Campers"])):
                    print("----------------------------")
                    print("Nombre",archivo["Campers"][f]["nombres"])
                    print("ID",archivo["Campers"][f]["id"])
                    print("----------------------------")
                    if archivo["Campers"][f]["id"] not in idCamperNota:
                        idCamperNota.append(archivo["Campers"][f]["id"])


                bol41=True
                while bol41==True:
                    try:
                        idNotaFiltro=int(input("Ingresa el ID del camper al que le quieres agregar la nota\n"))
                        while idNotaFiltro not in idCamperNota:
                            idNotaFiltro=int(input("ID no encontrado por favor ingresa uno valido\n"))
                        bol41=False
                    except ValueError:
                        print("Ingresa un ID valido (Solo numeros)")
                
                for j in range(len(archivo["Campers"])):
                    if idNotaFiltro==archivo["Campers"][j]["id"]:
                        posicionCamperNota=j

                
                confiAgregarNota="si"
                while confiAgregarNota=="si":
                    print("-----Modulos-----")
                    for g in range(len(archivo["Campers"][posicionCamperNota]["numeroModulo"])):
                        print(g+1,archivo["Campers"][posicionCamperNota]["numeroModulo"][g])

                    bol42=True
                    while bol42==True:
                        try:
                            moduloAgregarNota=int(input("Ingrese el modulo al que le quiere agregar la nota del filtro (Ingrese el numero)\n"))
                            while moduloAgregarNota<1 or moduloAgregarNota>5:
                                moduloAgregarNota=int(input("Ingrese un modulo de los que aparecen en pantalla\n"))
                            bol42=False
                        except ValueError:
                            print("Ingrese el numero del modulo")

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
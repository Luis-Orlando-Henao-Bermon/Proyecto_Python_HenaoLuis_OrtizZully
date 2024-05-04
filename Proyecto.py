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
          4). Salir. 
    --------------------------------------------------------
""")

def menuTrainer():
    print("///////////////////////////////////////////////////\n----------- BIENVENIDO", archivo["Trainers"][q]["nombres"],"""--------------------
          
          1). Cambiar usuario y contraseña
          2). Ruta de entrenamiento.
          3). Cambiar información.
          4). Salir.
          
    ---------------------------------------------------
    ///////////////////////////////////////////////////
""")

def menuTrainerOpc3():
    print("""
    ----------------- Cambiar información ---------------
          1). Cambiar dirección.
          2). Cambiar telefono movil.
          3). Cambiar telefono fijo 
          4). Salir
    -----------------------------------------------------
""")

def menuCoordinador():
    print("//////////////////////////////////////////////////////////////////////\n    ---------------- Bienvenido",archivo["Coordinador"][0]["nombres"],"""----------------------------
          1). Cambiar usuarios y contraseñas de todo el sistema educativo.
          2). Cambiar informacion de todo el sistema educativo.
          3). Agregar nota de examen de aprobación.
          4). Agregar nota de filtro. 
          5). Consultar cuales campers se encuentra en riesgo alto.
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
          7). Volver al menu anterior 
    ----------------------------------------------------------------------------------------------------
""")
    

with open("./Campusland.json", encoding="utf-8") as file:#con esto se abre el archivo de campusland.json que es donde esta toda la informacion
    archivo=json.load(file)

user=input("Ingrese su usuario:\n")#se pide que ingrese el usuario
system("clear")
x=0#esto es para saber si hay alguien con ese usuario ya que si hay alguien con ese usuario x se volvera 1 y se terminara el bucle de while 

while x==0:#si no hay nadie con el usuario ingresado x seguira siendo 0 por lo tanto se repetira el bucle while (antes de repetir el bucle se pide que se ingrese de nuevo el usuario para poder ver si el ingresado nuevamente esta o no )
    for i in range(len(archivo["Campers"])):#se usa un bucle for para recorra cada una  de las pociciones de los campers

        if user==archivo["Campers"][i]["user"]["login"]:#se miran todas las pociciones de los campers y si el usuario (login) alguno de ellos coinciden con el ingresado x pasa a valer 1 y se rompe el bucle de while 
        
            x+=1
            passwordCamper=input("Ingresa su contraseña:\n")#despues de saber cual es el camper con ese usuario se le pide la contraseña 
            system("clear")

            while passwordCamper != archivo["Campers"][i]["user"]["contraseña"]:#se usa un bucle while porque mientras que la contraseña ingresada no este en archivo["Campers"][i]["user"]["contraseña"] (que es la direcion en donde esta la contraseña en el archivo) se repetira el bucle que lo que hace es volver a pedirle la contraseña 
                passwordCamper=input("Contraseña incorrecta ingresela otra vez\n")
            system("clear")
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
                    confirmacion="si"#Creamos un booleano donde sea si se hara
                    while confirmacion=="si":
                        #Le mostrara el camper el submenu de la opcion uno 
                        menuCamperOpc1()

                        bol13=True
                        while bol13 == True:
                            try:#si el usuario ingresa una letra en las opciones se le indidara que debe ser numero y se le repetira el proceso hasta que lo ingrese bien, y si ingresa un numero que no esta en el menu se le dira que solo se le permitira las opciones que aparece en la pantalla
                                newOpc1=int(input("Ingrese una opcion del menu anterior:\n"))#El camper ingresara la opcion que desea observar 
                                while newOpc1<1 or newOpc1>5:
                                    newOpc1=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))
                                bol13=False
                            except ValueError:
                                print("Ingresa una opcion valida (Numero)\n")
                        system("clear")
                                                        
                        #Si la opcion elegida es uno se mostrara 
                        if newOpc1==1:#toda la informacion que tiene el camper, llamar desde json cada informacion del camper para que se muestre de una forma ordenada en la pantalla
                            print("--- Hola",archivo["Campers"][i]["nombres"],"estos son tus datos: -----------\n")
                            print("    Numero de identificaion:",archivo["Campers"][i]["numeroIdentificacion"])
                            print("    Nombres:",archivo["Campers"][i]["nombres"])
                            print("    Apellidos:",archivo["Campers"][i]["apellidos"])
                            print("    Direccion:",archivo["Campers"][i]["direccion"])
                            print("    Acudiente:",archivo["Campers"][i]["acudiente"])
                            print("    Telefono celular:",archivo["Campers"][i]["telefonoCelular"])
                            print("    Telefono fijo:",archivo["Campers"][i]["telefonoFijo"])
                            print("------------------------------------------------------")
                            
                            confirmacion=input("Si quieres ver otro reporte escribe: si, de lo contrario preciona enter\n")
                            system("clear")#este es el booleano de la linea 117, dodne se le preguntara al camper si desea ver otra opcion del menu del reporte si la respuesta es si, se le repetira el proceso, y si da enter le mostrara el menu principal del camper 

                        elif newOpc1==2:#Si la opcion elegida es dos se hara:

                        #si en el archivo del camper el estado es aprobado o esta cursado se le mostrara el riesgo que se encuentra
                            mod=archivo["Campers"][i]["moduloActual"]
                            mod=mod-1
                            if archivo["Campers"][i]["estado"]=="Aprobado" or archivo["Campers"][i]["estado"]=="Cursando": 
                                # Si en las posiciones del camper se encuentra el estado aprobado o cursando se le mstrata al camper.   
                                print("Tu riesgo es:",archivo["Campers"][i]["riesgo"][mod],"\n")
                                #Se le mostrara al camper el riesgos que se encuentra
                            else:#Si el camper no se encuentra en aprobado o cursando se le mostrara en que estado se encuentra y se le aclarará que no tienes riesgo por lo mismo.
                                print("Tu estado es:",archivo["Campers"][i]["estado"],"por lo tanto no tienes riesgo""\n")
                            
                            confirmacion=input("Si quieres ver otro reporte escribe: si, de lo contrario preciona enter\n")
                            system("clear")#este es el booleano de la linea 117, dodne se le preguntara al camper si desea ver otra opcion del menu del reporte si la respuesta es si, se le repetira el proceso, y si da enter le mostrara el menu principal del camper 

                        #Si la opcion elegida es tres se hara:
                        elif newOpc1==3:
                            print("Tu ruta es:",archivo["Campers"][i]["ruta"],"\n")#Se le mostara la ruta en el que se encuentra el camper

                            confirmacion=input("Si quieres ver otro reporte escribe: si, de lo contrario preciona enter\n")
                            system("clear")#este es el booleano de la linea 117, dodne se le preguntara al camper si desea ver otra opcion del menu del reporte si la respuesta es si, se le repetira el proceso, y si da enter le mostrara el menu principal del camper 
                        #Si la opcion elegida del camper es cuatro se hara: 
                        elif newOpc1==4:
                            print("Tu trainer es:",archivo["Campers"][i]["trainer"],"\n") #Se le mostrara el trainer del camper

                            confirmacion=input("Si quieres ver otro reporte escribe: si, de lo contrario preciona enter\n")
                            system("clear")#este es el booleano de la linea 117, dodne se le preguntara al camper si desea ver otra opcion del menu del reporte si la respuesta es si, se le repetira el proceso, y si da enter le mostrara el menu principal del camper 
                        #Si la opcion elegida es cinco se hara:
                        elif newOpc1==5:
                            #Se le muestra el modulo que se encurntra siguiendo la ruta archivo["Campers"][i]["moduloActual"], y despues se le mostrara el nombre del modulo  archivo["Campers"][i]["numeroModulo"][archivo["Campers"][i]["moduloActual"]-1], como los modulos se enumeran de 0 a 4, le restamos 1 para que enumere desde uno hasta cinco 
                            print("El modulo que te encuentras actualmente es:",archivo["Campers"][i]["moduloActual"],archivo["Campers"][i]["numeroModulo"][archivo["Campers"][i]["moduloActual"]-1],"\n")#SSe mostrara el modulo que se encuentra actualmente el camper

                            confirmacion=input("Si quieres ver otro reporte escribe: si, de lo contrario preciona enter\n")
                            system("clear")#este es el booleano de la linea 117, dodne se le preguntara al camper si desea ver otra opcion del menu del reporte si la respuesta es si, se le repetira el proceso, y si da enter le mostrara el menu principal del camper 


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
                    system("clear")

                    newPass1=input("¿Ingrese la nueva contraseña?\n")#Se le preguntara al camper cual va a ser el nuevo usuario
                    archivo["Campers"][i]["user"]["contraseña"]=newPass1#ingresara las posiciones del camper donde esta el user y mira la contraseña del camper y lo cambia por el nuevo que ingreso.
                    system("clear")

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
                    confirmacion3="si"
                    while confirmacion3=="si":

                        menuCamperOpc3()#Se llamara la funcion del menu camper opcion tres donde se le mostrara las opciones disponibles del menu.

                        bol14=True
                        while bol14==True:
                            try:
                                numOpc3=int(input("Ingrese una de las opciones del menu anterior\n"))#El ingresara la opcione que desee realizar del menu anterior 
                                while numOpc3<1 or numOpc3>3:

                                    numOpc3=int(input("Ingrese una opcion de la que aparece en la pantalla.\n"))

                                bol14=False
                            except ValueError:
                                print("Ingresa una opcion valida (Numero)\n")
                        system("clear")
                        if numOpc3==1:#Si la opcion del menu es uno se hara:
                            newAdress=input("Ingrese la nueva direccion\n")#el camper ingresara la nueva direccion 
                            archivo["Campers"][i]["direccion"]=newAdress#Ingresara en las posiciones del camper y ingresara  a la direccion y asi se guardara el cambio de la nueva direccion 
                            print("")
                            confirmacion=input("Si deseas cambiar otra información escribe: si, de lo contrario preciona enter\n")
                            system("clear")

                        elif numOpc3==2:#Si la opcion del menu es dos se hara:
                            bol7=True#este boleano es para que el valor a ingresar a pantalla sea numero si no es numero se volvera a repetir el bucle y no le permitira seguir.
                            while bol7==True:
                                try:
                                    newPhone=int(input("Ingrese el nuevo telefono movil\n"))#el camper ingresara el nuevo telefono movil 
                                    bol7=False
                                except ValueError:   
                                    print("Ingrese un telefono movil valido (solo numeros)\n")#el camper ingresara el nuevo telefono movil
                                    print("")
                                confirmacion=input("Si deseas cambiar otra información escribe: si, de lo contrario preciona enter\n")
                            system("clear")

                            archivo["Campers"][i]["telefonoCelular"]=newPhone#Ingresara en las posiciones del camper y ingresara donde esta el telefono movil y asi se guardara el cambio del nuevo dato ingresado.

                        elif numOpc3==3:#Si la opcion elegida es tres se hara:
                            bol8=True#este boleano es para que el valor a ingresar a pantalla sea numero si no es numero se volvera a repetir el bucle y no le permitira seguir.
                            while bol8==True:
                                try:
                                    newFijo=int(input("Ingrese el nuevo telefono fijo\n"))#el camper ingresara el nuevo telefono fijo
                                    bol8=False
                                except ValueError:
                                    print("Ingrese un telefono fijo valido(solo numeros)\n")#Si el camper ingresa alguna letra se le notificara y se le recordara que solo se acepta numero y se volvera a repetir 
                                    print("")
                                confirmacion=input("Si deseas cambiar otra información escribe: si, de lo contrario preciona enter\n")
                            system("clear")

                            archivo["Campers"][i]["telefonoFijo"]=newFijo#Ingresara en las posiciones del camper y ingresara donde se encuentra telefono fijo y asi se guardara el nuevo dato ingresado. 

                        elif numOpc3==4:

                         system("clear")
                         confirmacion3="no"


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
                    print("")
                    campers=False
                    

    for q in range(len(archivo["Trainers"])):#se usa un bucle for para recorra cada una  de las pociciones de los trainers

        if user == archivo["Trainers"][q]["user"]["login"]:#se miran todas las pociciones de los trainers y si el usuario (login) alguno de ellos coinciden con el ingresado x pasa a valer 1 y se rompe el bucle de while

            x+=1
            passwordTrainer=input("Ingresa la contraseña\n")#despues de saber cual es el Trainer con ese usuario se le pide la contraseña 
            system("clear")
            
            while passwordTrainer != archivo["Trainers"][q]["user"]["contraseña"]:#se usa un bucle while porque mientras que la contraseña ingresada no este en ["Trainers"][q]["user"]["contraseña"] (que es la direcion en donde esta la contraseña en el archivo) se repetira el bucle que lo que hace es volver a pedirle la contraseña 
                passwordTrainer=input("Contraseña incorrecta ingresela otra vez\n")
            system("clear")

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
                    system("clear")
                    archivo["Trainers"][q]["user"]["login"]=newUser2 #en el archivo se posicionara donde estan los trainer e ingresara a user login(usuario) y se guardara el nuevo usuario que ingreso el trainer
                    newPass2=input("¿Cual es la nueva contraseña?:\n")#El trainer ingresara la nueva contraseña
                    archivo["Trainers"][q]["user"]["contraseña"]=newPass2#en el archivo se posicionara donde se encuantre los traines e ingresara a user contraseña y se guardara la nueva contraseña que ingreso el trainer 
                    system("clear")

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

                    print("La ruta de entrenamiento es",archivo["Trainers"][q]["ruta"],"\n")
                    
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
                    confirmacion1="si"
                    while confirmacion1 == "si":
                        #se le mostara el submenu de la opcion 3 al trainer 
                        menuTrainerOpc3()
                        bol15=True
                        while bol15==True:
                            try:
                                newOpc=int(input("Ingrese unas de las opciones del menu anterior:\n"))#Ingresara una opcion del submenu anterior
                                while newOpc<1 or newOpc>4:
                                    newOpc=int(input("Ingrese una opcion de las que aparecen en la pantalla:\n"))
                                bol15=False
                            except ValueError:
                                print("Ingrese una opcion valida(Número)\n")
                        system("clear")

                        
                        if newOpc==1: #Si la opcion es uno se hara:
                            newAdress1=input("Ingrese la nueva dirección:\n")#El trainer ingresara la direccion nueva 
                            archivo["Trainers"][q]["direccion"]=newAdress1#en las pociciones del trainer en la posicion de direccion se le cambiara a la direccion nueva ingresada por el mismo.
                        #si la opcion elegida es dos se hara:
                            confirmacion1=input("Si deseas cambiar otra información escribe: si, de lo contrario preciona enter\n")
                            system("clear")

                            
                        elif newOpc==2:
                            bol10=True#este booleano es por que el dato a ingresar debe ser entero por ende si el trainer ingresa una letra no se le aceptara y se le volvera a repetir el valor a ingresar hasta que no lo ingrese bien el bucle no parará.
                            while bol10==True:
                                try:
                                    newPhone1=int(input("Ingrese el nuevo telefono movil:\n"))#El trainer ingresara el nuevo telefono movil
                                    bol10=False#
                                except ValueError:
                                    print("Ingrese un telefono movil valido(solo numeros)\n")
                            archivo["Trainers"][q]["telefonoCelular"]=newPhone1#En las posiciones del trainer en la posicion del telefono celular se guardara el dato que ingreso en trainer
                            #Si la opcion elegida es tres se hara: 
                            confirmacion1=input("Si deseas cambiar otra información escribe: si, de lo contrario preciona enter\n")
                            system("clear")

                            
                        elif newOpc==3:
                            bol11=True#este booleano es por que el dato a ingresar debe ser entero por ende si el trainer ingresa una letra no se le aceptara y se le volvera a repetir el valor a ingresar hasta que no lo ingrese bien el bucle no parará.
                            while bol11==True:
                                try:
                                    newFijo1=int(input("Ingrese el nuevo telefono fijo:\n"))#El trainer ingresara el nuevo telefono fijo
                                    bol11=False
                                except ValueError:
                                    print("Ingrese un telefono fijo valido (solo numeros)\n")
                            archivo["Trainers"][q]["telefonoFijo"]=newFijo1#En las posiciones del trainer en la posicion del telefono fijo se guardara el dato que ingreso en trainer
                            confirmacion1=input("Si deseas cambiar otra información escribe: si, de lo contrario preciona enter\n")
                            system("clear")

                        
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

                        elif newOpc==4:
                            confirmacion1=""
                    
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
                        print("Datos por cambiar\n1. ID\n2. Numero de Identificacion\n3. Nombres\n4. Apellidos\n5. Direccion\n6. Acudiente\n7. Telefono Celular\n8. Telefono fijo\n9. Estado\n\nLa siguiente informacion solo es valida para usuarios que ya estan cursando\n\n10. Fecha de inicio\n11. Fecha de cierre\n12. grupo\n13. Modulo actual\n14. Volver al menu anterior ")

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
                            system("clear")
                            
                            print("-----Tipos de estado-----")
                            for a in range(len(archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeEstados"])):#se muestran los tipos de estado con unbucle for
                                print(archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeEstados"][a])
                            
                            estadoCambiar=input("¿Cual es el nuevo estado?\n")#se pregunta cual es el nuevo estado y se guarda en la variable estadoCambiar

                            while estadoCambiar not in archivo[personaCambiarInfo][posicionCamperCambiar]["tiposDeEstados"]: #mientras que el estado ingresado por el usuario no este en los tipos de estados le pedira que ingrese un estado valido 
                                estadoCambiar=input("Ingrese un estado valido (Tienes que escribirlo como aparece en los tipos de estado)\n")

                            archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=estadoCambiar# Como ya se sabe cual es el nuevo estado que quiere solo se remplaza el que ya estaba por el que ingreso el usuario

                            if estadoCambiar=="Aprobado" and archivo[personaCambiarInfo][posicionCamperCambiar]["fechaInicio"]=="" or estadoCambiar=="Cursando" and archivo[personaCambiarInfo][posicionCamperCambiar]["fechaInicio"]=="":#si el usuario puso de nuevo estado aprovado se tienen que llenar otra informacion ya que ahora pertenece a campusland

                                print("Como el estado del estudiante ahora es Aprobado tienes que llenar la siguiente informacion:")

                                agregarFechaInicio=input("Ingrese una fecha de inicio (DD-MM-AAAA)\n")#se pide y se agrega la fecha de inicio
                                archivo[personaCambiarInfo][posicionCamperCambiar]["fechaInicio"]=agregarFechaInicio

                                system("clear")
                                agregarFechaCierre=input("Ingrese una fecha de cierre (DD-MM-AAAA)\n")#se pide y se agrega la fecha de cierre
                                archivo[personaCambiarInfo][posicionCamperCambiar]["fechaCierre"]=agregarFechaCierre

                                system("clear")
                                archivo[personaCambiarInfo][posicionCamperCambiar]["moduloActual"]=1#se pone que el modulo actual es igual a 1 ya que como apenas esta empezando empieza en el modulo 1

                                system("clear")

                                grupos=[]
                                for q in range(len(archivo["Coordinador"][1]["rutas"])):#con este bucle for se muestran todas las rutas que hay 
                                    print("-----------------------------------")
                                    print("Ruta:",archivo["Coordinador"][1]["rutas"][q])
                                    for t in range(len(archivo["Coordinador"][1]["tiposDeRutas"][q]["grupos"])):#despues de que el bucle anterior haya mosstrado la primera tuta este bucle muestra los salones que hay en esa ruta 
                                        print("-----Grupos-----")
                                        print(archivo["Coordinador"][1]["tiposDeRutas"][q]["grupos"][t])
                                        if archivo["Coordinador"][1]["tiposDeRutas"][q]["grupos"][t] not in grupos:#este if mira si el grupo esta en la lista grupos si no esta lo añade ahi 
                                            grupos.append(archivo["Coordinador"][1]["tiposDeRutas"][q]["grupos"][t])
                                    
                                
                                grupoCambiar=input("Ingrese un grupo (Escogelo dependiendo de la ruta que Quieras)\n")
                                
                                while grupoCambiar not in grupos:#mienta que el grupo ingresado no este en la lista gupos le va apedir que ingrese otro grupo
                                    grupoCambiar=input("Grupo no encontrado ingresa un grupo de los que hay en pantalla \n")

                                estudiantesG=0#este es un contador para mirar cuantos estudiantes tienen el mismo grupo
                                for y in range(len(archivo["Campers"])):
                                    if grupoCambiar==archivo["Campers"][y]["grupo"]:#si el estudiante tiene el mismo grupo al ingresado suma uno al contador
                                        estudiantesG=estudiantesG+1

                                while estudiantesG==1:
                                    grupoCambiar=input("Grupo con limites de estudiantes por favor ingresa otro\n")

                                    while grupoCambiar not in grupos:#mienta que el grupo ingresado no este en la lista gupos le va apedir que ingrese otro grupo
                                        grupoCambiar=input("Ingresa un grupo de los que hay en pantalla \n")

                                    estudiantesG=0
                                    for y in range(len(archivo["Campers"])):#este es un contador para mirar cuantos estudiantes tienen el mismo grupo
                                        if grupoCambiar==archivo["Campers"][y]["grupo"]:#si el estudiante tiene el mismo grupo al ingresado suma uno al contador
                                            estudiantesG=estudiantesG+1


                                archivo[personaCambiarInfo][posicionCamperCambiar]["grupo"]=grupoCambiar #despues de saber cual es el grupo simplemente lo agrega al grupo del estudiante

                                for u in range(len(archivo["Coordinador"][1]["rutas"])):#este es un for para mirar todas las rutas 
                                    if grupoCambiar in archivo["Coordinador"][1]["tiposDeRutas"][u]["grupos"]:#si una ruta tiene el grupo ingresado le va a poner esa ruta al camper 
                                        archivo[personaCambiarInfo][posicionCamperCambiar]["ruta"]=archivo["Coordinador"][1]["rutas"][u]

                            confiInfor=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")
                        
                        elif opcCambioCamper==10:
                            if archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Aprobado" or archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Cursando":
                                fechaCambio=input("¿Cual es la nueva fecha de inicio? (DD-MM-AAAA)\n")

                                archivo[personaCambiarInfo][posicionCamperCambiar]["fechaInicio"]=fechaCambio
                                            
                            else:
                                print("Este camper se encuentra en estado",archivo[personaCambiarInfo][posicionCamperCambiar]["estado"], "por lo tanto no tiene fecha de inicio")

                            confiInfor=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")
                        
                        elif opcCambioCamper==11:

                            if archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Aprobado" or archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Cursando":
                                fechaCierreCambio=input("¿Cual es la nueva fecha de cierre? (DD-MM-AAAA)\n")

                                archivo[personaCambiarInfo][posicionCamperCambiar]["fechaCierre"]=fechaCierreCambio
                            
                            else:
                                print("Este camper se encuentra en estado",archivo[personaCambiarInfo][posicionCamperCambiar]["estado"], "por lo tanto no tiene fecha de inicio")


                            confiInfor=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")


                        elif opcCambioCamper==12:
                            if archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Aprobado" or archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Cursando":
                                
                                
                                system("clear")

                                grupos=[]
                                for q in range(len(archivo["Coordinador"][1]["rutas"])):#con este bucle for se muestran todas las rutas que hay 
                                    print("-----------------------------------")
                                    print("Ruta:",archivo["Coordinador"][1]["rutas"][q])
                                    for t in range(len(archivo["Coordinador"][1]["tiposDeRutas"][q]["grupos"])):#despues de que el bucle anterior haya mosstrado la primera tuta este bucle muestra los salones que hay en esa ruta 
                                        print("-----Grupos-----")
                                        print(archivo["Coordinador"][1]["tiposDeRutas"][q]["grupos"][t])
                                        if archivo["Coordinador"][1]["tiposDeRutas"][q]["grupos"][t] not in grupos:#este if mira si el grupo esta en la lista grupos si no esta lo añade ahi 
                                            grupos.append(archivo["Coordinador"][1]["tiposDeRutas"][q]["grupos"][t])
                                    
                                
                                grupoCambiar=input("Ingrese un grupo (Escogelo dependiendo de la ruta que Quieras)\n")
                                
                                while grupoCambiar not in grupos:#mienta que el grupo ingresado no este en la lista gupos le va apedir que ingrese otro grupo
                                    grupoCambiar=input("Grupo no encontrado ingresa un grupo de los que hay en pantalla \n")

                                estudiantesG=0#este es un contador para mirar cuantos estudiantes tienen el mismo grupo
                                for y in range(len(archivo["Campers"])):
                                    if grupoCambiar==archivo["Campers"][y]["grupo"]:#si el estudiante tiene el mismo grupo al ingresado suma uno al contador
                                        estudiantesG=estudiantesG+1

                                while estudiantesG==33:#mientras que el contadopr de estudiantes en un grupo sea 33 (es la cantidad maxima de estudiantes) le va a decir que el grupo esta lleno y que tiene que ingresar otro
                                    grupoCambiar=input("Grupo con limites de estudiantes por favor ingresa otro\n")

                                    while grupoCambiar not in grupos:#mienta que el grupo ingresado no este en la lista gupos le va apedir que ingrese otro grupo
                                        grupoCambiar=input("Ingresa un grupo de los que hay en pantalla \n")

                                    estudiantesG=0
                                    for y in range(len(archivo["Campers"])):#este es un contador para mirar cuantos estudiantes tienen el mismo grupo
                                        if grupoCambiar==archivo["Campers"][y]["grupo"]:#si el estudiante tiene el mismo grupo al ingresado suma uno al contador
                                            estudiantesG=estudiantesG+1


                                archivo[personaCambiarInfo][posicionCamperCambiar]["grupo"]=grupoCambiar #despues de saber cual es el grupo simplemente lo agrega al grupo del estudiante

                                for u in range(len(archivo["Coordinador"][1]["rutas"])):#este es un for para mirar todas las rutas 
                                    if grupoCambiar in archivo["Coordinador"][1]["tiposDeRutas"][u]["grupos"]:#si una ruta tiene el grupo ingresado le va a poner esa ruta al camper 
                                        archivo[personaCambiarInfo][posicionCamperCambiar]["ruta"]=archivo["Coordinador"][1]["rutas"][u]

                            else:
                                print("Este camper se encuentra en estado",archivo[personaCambiarInfo][posicionCamperCambiar]["estado"], "por lo tanto no tiene grupo")


                            confiInfor=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#se pregunta si quiere cambiar algo mas y si dice que si se mostrara el menu anterior ya que mientras que confiInfor sea si se repetira el bucle while que contiene el menu de opciones de cambio
                            system("clear")


                        elif opcCambioCamper==13:

                            if archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Aprobado" or archivo[personaCambiarInfo][posicionCamperCambiar]["estado"]=="Cursando":
                                print("----Modulos-----")
                                for s in range(len(archivo["Coordinador"][1]["numeroModulo"])):#se muestran los modulos que hay 
                                    print(s+1,archivo["Coordinador"][1]["numeroModulo"][s])

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
                        
                        if opcCambioCamper==14:
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
                    while confiInforTrainer=="si":#este bucle se usa para preguntar si quiere cambiar algo mas si escribe si se repite el bucle y si preciona enter se sale del bucle y vuelve al menu anterior
                        #se muestra la informacion que se puede cambiar 
                        print("-----Informacion que se puede cambiar-----\n1. ID\n2. Numero de identificacion\n3. Nombres\n4. Apellidos\n5. Direccion\n6. Telefono Celular\n7. Telefono Fijo\n8. Ruta\n9. Volver al menu anterior ")
                    
                        bol32=True
                        while bol32==True:
                            try:
                                opcCambioTrainer=int(input("Ingresa tu opcion\n")) #se pide la opcion y si la opcion no esta entre las que aparecen en pantalla le mada error
                                while opcCambioTrainer<1 or opcCambioTrainer>9:
                                    opcCambioTrainer=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))
                                bol32=False
                            except ValueError:
                                print("Ingresa un opcion valida (Numero)")
                        
                        if opcCambioTrainer==1:
                            #si escoge la opcion 1 le pide el nuevo id y lo remplaza por el que ya estaba
                            bol33=True
                            while bol33==True:
                                
                                try:
                                    idCambioTrainer=int(input("Ingresa el nuevo ID\n"))
                                    bol33=False
                                except ValueError:
                                    print("Ingresa un ID valido (Solo numeros)")
                            
                            archivo[personaCambiarInfo][posicionTrainerCambiar]["id"]=idCambioTrainer
                                
                            confiInforTrainer=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#aca es donde se pregunta si quiere cambiar algo mas para saber si se repite el bucle o no
                            system("clear")
                        
                        elif opcCambioTrainer==2:
                            #si escoge la opcion 2 le pide el nuevo numero de identificacion y lo remplaza por el que ya estaba
                            bol34=True
                            while bol34==True:
                                try:
                                    nidCambioTrainer=int(input("Ingresa el nuevo Numero de identificacion\n"))
                                    bol34=False
                                except ValueError:
                                    print("Ingresa un numero de identificadion valido (Solo numeros)")

                            archivo[personaCambiarInfo][posicionTrainerCambiar]["numeroIdentificacion"]= nidCambioTrainer

                            confiInforTrainer=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#aca es donde se pregunta si quiere cambiar algo mas para saber si se repite el bucle o no
                            system("clear")
                        
                        elif opcCambioTrainer==3:
                            #si escoge la opcion 3 le pide los nuevos nombres y los remplaza por el que ya estaba

                            nombreCambioTrainer= input("Ingresa los nuevos nombres\n")

                            archivo[personaCambiarInfo][posicionTrainerCambiar]["nombres"]=nombreCambioTrainer

                            confiInforTrainer=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#aca es donde se pregunta si quiere cambiar algo mas para saber si se repite el bucle o no
                            system("clear")
                        
                        elif opcCambioTrainer==4:

                            #si escoge la opcion 4 le pide los nuevos apellidos y los remplaza por el que ya estaba
                            apellidoCambioTrainer=input("Ingresa los nuevos apellidos\n")

                            archivo[personaCambiarInfo][posicionTrainerCambiar]["apellidos"]=apellidoCambioTrainer

                            confiInforTrainer=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#aca es donde se pregunta si quiere cambiar algo mas para saber si se repite el bucle o no
                            system("clear")
                        
                        elif opcCambioTrainer==5:
                            
                            #si escoge la opcion 5 le pide la nueva direccion y la remplaza por la que ya estaba

                            direccionCambioTrainer=input("Ingresa la nueva direccion\n")

                            archivo[personaCambiarInfo][posicionTrainerCambiar]["direccion"]=direccionCambioTrainer

                            confiInforTrainer=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#aca es donde se pregunta si quiere cambiar algo mas para saber si se repite el bucle o no
                            system("clear")
                        
                        elif opcCambioTrainer==6:
                            
                            #si escoge la opcion 6 le pide el nuevo numero de telefono y lo remplaza por el que ya estaba

                            bol35=True
                            while bol35==True:
                                try:
                                    TelefonoCelularTrainerCambiar=int(input("Ingresa el nuevo numero de telefono celular\n"))
                                    bol35=False
                                except ValueError:
                                    print("Ingresa un numero de telefono valido (Solo numeros)")
                                
                            archivo[personaCambiarInfo][posicionTrainerCambiar]["telefonoCelular"]=TelefonoCelularTrainerCambiar

                            confiInforTrainer=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#aca es donde se pregunta si quiere cambiar algo mas para saber si se repite el bucle o no
                            system("clear")

                        elif opcCambioTrainer==7:
                            
                            #si escoge la opcion 7 le pide el nuevo numero de telefono fijo y lo remplaza por el que ya estaba

                            bol35=True
                            while bol35==True:
                                try:
                                    TelefonoFijoTrainerCambiar=int(input("Ingresa el nuevo numero de telefono fijo\n"))
                                    bol35=False
                                except ValueError:
                                    print("Ingresa un numero de telefono valido (Solo numeros)")
                                
                            archivo[personaCambiarInfo][posicionTrainerCambiar]["telefonoFijo"]=TelefonoFijoTrainerCambiar

                            confiInforTrainer=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#aca es donde se pregunta si quiere cambiar algo mas para saber si se repite el bucle o no
                            system("clear")

                        elif opcCambioTrainer==8:

                            #si escoge la opcion 8 le pide la nueva ruta y lo remplaza por el que ya estaba

                            print("-----Tipos de rutas-----")
                            for p in range(len(archivo["Coordinador"][1]["rutas"])):
                                print(archivo["Coordinador"][1]["rutas"][p])

                            rutaTrainerCambiar=input("Ingrese la nueva ruta\n")

                            while rutaTrainerCambiar not in archivo["Coordinador"][1]["rutas"]:
                                
                                rutaTrainerCambiar=input("Ingrese una ruta valida (Tienes que escibirla como aparece en pantalla)\n")

                            archivo[personaCambiarInfo][posicionTrainerCambiar]["ruta"]=rutaTrainerCambiar

                            for o in range(len(archivo["Coordinador"][1]["rutas"])):#despues de reemplazar la ruta se usa este bucle para saber la pocicion de la ruta que se escogio
                                if rutaTrainerCambiar==archivo["Coordinador"][1]["rutas"][o]:
                                    posicionRutaTrainer=o

                            print("-----Grupos de esta ruta-----")
                            gruposRuta=[]#en esta lista se guardaran los grupos que hay para esta ruta
                            for t in range(len(archivo["Coordinador"][1]["tiposDeRutas"][posicionRutaTrainer]["grupos"])):
                                print(archivo["Coordinador"][1]["tiposDeRutas"][posicionRutaTrainer]["grupos"][t])
                                if archivo["Coordinador"][1]["tiposDeRutas"][posicionRutaTrainer]["grupos"][t] not in gruposRuta:
                                    gruposRuta.append(archivo["Coordinador"][1]["tiposDeRutas"][posicionRutaTrainer]["grupos"][t])

                            grupoAgregar=input("Escoja un grupo\n")

                            while grupoAgregar not in gruposRuta:
                                grupoAgregar=input("Escoja un grupo de los que hay en pantalla (tienes que escribirlo como esta ahi)\n")
                            
                            for y in range(len(archivo["Campers"])):#se usa un bucle while para mirar todos los campers y los campers que tengan ese grupo se le agrega ese trainer 

                                if grupoAgregar==archivo["Campers"][y]["grupo"]:
                                    archivo["Campers"][y]["trainer"]=archivo[personaCambiarInfo][posicionTrainerCambiar]["nombres"]


                            
                            confiInforTrainer=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")#aca es donde se pregunta si quiere cambiar algo mas para saber si se repite el bucle o no
                            system("clear")
                        
                        elif opcCambioTrainer==9:
                            #si escoge el punto 9 confiInforTrainer es igual a "" y con esto se edevuelve al menu anterior 
                            system("clear")

                            confiInforTrainer=""

                if personaCambiarInfo=="Coordinador":
                    #como solo hay un solo coordinador directamente se le pregunta que quiere cambiar de esa informacion

                    confiInforCoordinador="si"
                    while confiInforCoordinador=="si":#este while se usa para saber si quiere cambiar mas cosas de los datos y si quiere hacerlo se repite este bucle 

                        print("-----Informacion que se puede cambiar-----\n1. ID\n2. Numero de identificacion\n3. Nombres\n4. Apellidos\n5. Direccion\n6. Telefono Celular\n7. Telefono Fijo\n8. Volver al menu anterior ")#se muestran las opciones que puede modificar


                        bol36=True
                        while bol36==True:
                            try:
                                opcCambioCoordinador=int(input("Ingresa tu opcion\n"))#se pide la opcion que quiiere cambiar
                                while opcCambioCoordinador<1 or opcCambioCoordinador>8:#mientras que la opcion que quiere cambiar no este entre las que hay en pantalla le pedira que ingrese una opcion valida 
                                    opcCambioCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))
                                bol36=False
                            except ValueError:
                                print("Ingrese una opcion valida (Numero)")
                        
                        if opcCambioCoordinador==1:

                            #si escoge la opcion 1 le pide el nuevo id y lo remplaza por el que ya estaba

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

                            #si escoge la opcion 2 le pide el nuevo numero de identificacion y lo remplaza por el que ya estaba

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

                            #si escoge la opcion 3 le pide los nuevos nombres y los remplaza por el que ya estaba

                            nombreCambioCoordinador=input("Ingresa los nuevos nombres del coordinador\n")

                            archivo["Coordinador"][0]["nombres"]=nombreCambioCoordinador

                            confiInforCoordinador=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")
                            system("clear")

                        elif opcCambioCoordinador==4:

                            #si escoge la opcion 4 le pide los nuevos apellidos y lo remplaza por el que ya estaba

                            apellidoCambioCoordinador=input("Ingresa los nuevos apellidos del coordinador\n")

                            archivo["Coordinador"][0]["apellidos"]=apellidoCambioCoordinador

                            confiInforCoordinador=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")
                            system("clear")
                        
                        elif opcCambioCoordinador==5:

                            #si escoge la opcion 5 le pide la nueva direccion y lo remplaza por la que ya estaba

                            direccionCambioCoordinador=input("Ingresa la nueva direccion\n")

                            archivo["Coordinador"][0]["direccion"]=direccionCambioCoordinador

                            confiInforCoordinador=input("Si quieres cambiar algo mas escribe: si, de lo contraio preciona enter\n")
                            system("clear")

                        elif opcCambioCoordinador==6:

                            #si escoge la opcion 6 le pide el nuevo numero de telefono movil y lo remplaza por el que ya estaba

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

                            #si escoge la opcion 7 le pide el nuevo numero de telefono fijo y lo remplaza por el que ya estaba

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

                            #si escoge la opcion 8 confiInforCoordinador se vuelve igual a "" y se cierra el ciclo

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
                Iden=int(input("Ingrese identificacion\n"))
                for i in range(0,len(archivo["Campers"])):
                    if Iden==archivo["Campers"][i]["numeroIdentificacion"]:
                        if archivo["Campers"][i]["estado"]=="Inscrito":
                            Nota=int(input("Ingrese la nota del estudiante\n"))
                            archivo["Campers"][i]["NotaI"]=Nota
                        else:
                            archivo["Campers"][i]["estado"]=="Cursando"
                            print("No tienes nota de inscripcion por que estas",archivo["Campers"][i]["estado"],"\n")

                input("")

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
                        idNotaFiltro=int(input("Ingresa el ID del camper al que le quieres agregar la nota\n"))#se pide el id del camper al que se le quiere agregar la nota y si el camper no esta en la lista idCamperNota le pida que ingrese uno valido
                        while idNotaFiltro not in idCamperNota:
                            idNotaFiltro=int(input("ID no encontrado por favor ingresa uno valido\n"))
                        bol41=False
                    except ValueError:
                        print("Ingresa un ID valido (Solo numeros)")
                
                for j in range(len(archivo["Campers"])):#este bucle for se usa para saber la pocicion del camper que tiene el id ingresado
                    if idNotaFiltro==archivo["Campers"][j]["id"]:
                        posicionCamperNota=j
                
                system("clear")

                
                confiAgregarNota="si"
                while confiAgregarNota=="si":
                    print("-----Modulos-----")#se muestran los modulos que hay (esa informacion la tiene cada uno de los campers)
                    for g in range(len(archivo["Campers"][posicionCamperNota]["numeroModulo"])):
                        print(g+1,archivo["Campers"][posicionCamperNota]["numeroModulo"][g])

                    bol42=True
                    while bol42==True:
                        try:
                            moduloAgregarNota=int(input("Ingrese el modulo al que le quiere agregar la nota del filtro (Ingrese el numero)\n"))#se pide el modulo en el cual quiere agregar nota de filtro y si dice una nota diferente a las que hay en pantalla le pide que ingrese una valida
                            while moduloAgregarNota<1 or moduloAgregarNota>5:
                                moduloAgregarNota=int(input("Ingrese un modulo de los que aparecen en pantalla\n"))
                            bol42=False
                        except ValueError:
                            print("Ingrese el numero del modulo")

                    
                    #dependiendo de la opcion que escoja se le pide la nota eorica y la practica luego se saca el promedio de esas 2 y esa es la nota que se agrega a cada modulo (cada camper tiene un lugar para cada nota)

                    if moduloAgregarNota==1:
                        system("clear")
                        
                        bol43=True
                        while bol43==True:
                            
                            try:
                                notaTeoricaM1=int(input("Ingrese la nota del filtro teorico\n"))
                                while notaTeoricaM1<0 or notaTeoricaM1>100:
                                    notaTeoricaM1=int(input("Ingrese una nota valida (Entre 0 y 100)\n"))
                                bol43=False
                            except ValueError:
                                print("Ingresa una nota valida (Numero)")
                        
                        system("clear")
                        
                        bol44=True
                        while bol44==True:
                            
                            try:
                                notaPracticaM1=int(input("Ingrese la nota del filtro practico\n"))
                                while notaPracticaM1<0 or notaPracticaM1>100:
                                    notaPracticaM1=int(input("Ingrese una nota valida (Entre 0 y 100)\n"))
                                bol44=False
                            except ValueError:
                                print("Ingresa una nota valida (Numero)")
                        
                        
                        notaFiltroM1=(notaPracticaM1+notaTeoricaM1)/2

                        if notaFiltroM1<60:
                            riesgoM1="Alto"
                        
                        elif notaFiltroM1>60:
                            riesgoM1="Bajo"


                        archivo["Campers"][posicionCamperNota]["riesgo"][0]=riesgoM1#aca se agrega el riesgo de este modulo
                        
                        archivo["Campers"][posicionCamperNota]["notaFiltro"][0]=notaFiltroM1

                        confiAgregarNota=input("Si quieres agregar otra nota de filtro escribe: si, de lo contrario preciona enter\n")
                        system("clear")

                    elif moduloAgregarNota==2:
                        system("clear")
                        
                        bol43=True
                        while bol43==True:
                            
                            try:
                                notaTeoricaM2=int(input("Ingrese la nota del filtro teorico\n"))
                                while notaTeoricaM2<0 or notaTeoricaM2>100:
                                    notaTeoricaM2=int(input("Ingrese una nota valida (Entre 0 y 100)\n"))
                                bol43=False
                            except ValueError:
                                print("Ingresa una nota valida (Numero)")
                        
                        system("clear")
                        
                        bol44=True
                        while bol44==True:
                            
                            try:
                                notaPracticaM2=int(input("Ingrese la nota del filtro practico\n"))
                                while notaPracticaM2<0 or notaPracticaM2>100:
                                    notaPracticaM2=int(input("Ingrese una nota valida (Entre 0 y 100)\n"))
                                bol44=False
                            except ValueError:
                                print("Ingresa una nota valida (Numero)")
                        
                        
                        notaFiltroM2=(notaPracticaM2+notaTeoricaM2)/2

                        if notaFiltroM2<60:
                            riesgoM2="Alto"
                        
                        elif notaFiltroM2>60:
                            riesgoM2="Bajo"


                        archivo["Campers"][posicionCamperNota]["riesgo"][1]=riesgoM2#aca se agrega el riesgo de este modulo
                        
                        
                        archivo["Campers"][posicionCamperNota]["notaFiltro"][1]=notaFiltroM2

                        confiAgregarNota=input("Si quieres agregar otra nota de filtro escribe: si, de lo contrario preciona enter\n")
                        system("clear")

                    elif moduloAgregarNota==3:
                        system("clear")
                        
                        bol43=True
                        while bol43==True:
                            
                            try:
                                notaTeoricaM3=int(input("Ingrese la nota del filtro teorico\n"))
                                while notaTeoricaM3<0 or notaTeoricaM3>100:
                                    notaTeoricaM3=int(input("Ingrese una nota valida (Entre 0 y 100)\n"))
                                bol43=False
                            except ValueError:
                                print("Ingresa una nota valida (Numero)")
                        
                        system("clear")
                        
                        bol44=True
                        while bol44==True:
                            
                            try:
                                notaPracticaM3=int(input("Ingrese la nota del filtro practico\n"))
                                while notaPracticaM3<0 or notaPracticaM3>100:
                                    notaPracticaM3=int(input("Ingrese una nota valida (Entre 0 y 100)\n"))
                                bol44=False
                            except ValueError:
                                print("Ingresa una nota valida (Numero)")
                        
                        
                        notaFiltroM3=(notaPracticaM3+notaTeoricaM3)/2

                        if notaFiltroM3<60:
                            riesgoM3="Alto"
                        
                        elif notaFiltroM3>60:
                            riesgoM3="Bajo"


                        archivo["Campers"][posicionCamperNota]["riesgo"][2]=riesgoM3#aca se agrega el riesgo de este modulo
                        
                        
                        archivo["Campers"][posicionCamperNota]["notaFiltro"][2]=notaFiltroM3

                        confiAgregarNota=input("Si quieres agregar otra nota de filtro escribe: si, de lo contrario preciona enter\n")
                        system("clear")

                    elif moduloAgregarNota==4:
                        system("clear")
                        
                        bol43=True
                        while bol43==True:
                            
                            try:
                                notaTeoricaM4=int(input("Ingrese la nota del filtro teorico\n"))
                                while notaTeoricaM4<0 or notaTeoricaM4>100:
                                    notaTeoricaM4=int(input("Ingrese una nota valida (Entre 0 y 100)\n"))
                                bol43=False
                            except ValueError:
                                print("Ingresa una nota valida (Numero)")
                        
                        system("clear")
                        
                        bol44=True
                        while bol44==True:
                            
                            try:
                                notaPracticaM4=int(input("Ingrese la nota del filtro practico\n"))
                                while notaPracticaM4<0 or notaPracticaM4>100:
                                    notaPracticaM4=int(input("Ingrese una nota valida (Entre 0 y 100)\n"))
                                bol44=False
                            except ValueError:
                                print("Ingresa una nota valida (Numero)")
                        
                        
                        notaFiltroM4=(notaPracticaM4+notaTeoricaM4)/2

                        if notaFiltroM4<60:
                            riesgoM4="Alto"
                        
                        elif notaFiltroM4>60:
                            riesgoM4="Bajo"


                        archivo["Campers"][posicionCamperNota]["riesgo"][3]=riesgoM4#aca se agrega el riesgo de este modulo
                        
                        
                        archivo["Campers"][posicionCamperNota]["notaFiltro"][3]=notaFiltroM4

                        confiAgregarNota=input("Si quieres agregar otra nota de filtro escribe: si, de lo contrario preciona enter\n")
                        system("clear")
                    
                    elif moduloAgregarNota==5:
                        system("clear")
                        
                        bol43=True
                        while bol43==True:
                            
                            try:
                                notaTeoricaM5=int(input("Ingrese la nota del filtro teorico\n"))
                                while notaTeoricaM5<0 or notaTeoricaM5>100:
                                    notaTeoricaM5=int(input("Ingrese una nota valida (Entre 0 y 100)\n"))
                                bol43=False
                            except ValueError:
                                print("Ingresa una nota valida (Numero)")
                        
                        system("clear")
                        
                        bol44=True
                        while bol44==True:
                            
                            try:
                                notaPracticaM5=int(input("Ingrese la nota del filtro practico\n"))
                                while notaPracticaM5<0 or notaPracticaM5>100:
                                    notaPracticaM5=int(input("Ingrese una nota valida (Entre 0 y 100)\n"))
                                bol44=False
                            except ValueError:
                                print("Ingresa una nota valida (Numero)")
                        
                        
                        notaFiltroM5=(notaPracticaM5+notaTeoricaM5)/2

                        if notaFiltroM5<60:
                            riesgoM5="Alto"
                        
                        elif notaFiltroM5>60:
                            riesgoM5="Bajo"


                        archivo["Campers"][posicionCamperNota]["riesgo"][4]=riesgoM5#aca se agrega el riesgo de este modulo
                        
                        
                        archivo["Campers"][posicionCamperNota]["notaFiltro"][4]=notaFiltroM5

                        confiAgregarNota=input("Si quieres agregar otra nota de filtro escribe: si, de lo contrario preciona enter\n")
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


            elif opcMenuCoordinador==5:
                
                for i in range(0,len(archivo["Campers"])):
                    if archivo["Campers"][i]["riesgo"]=="Alto":
                        print("Los riegos altos son",archivo["Campers"][i]["riesgo"],"\n")



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

                system("clear")
                    
                confiRepoCoordi="si"
                while confiRepoCoordi=="si":

                    menuCoordinadorOpc6()

                    bol45=True
                    while bol45 ==True:
                        try:
                            opcReporteCoordinador=int(input("Ingresa tu opcion\n"))
                            while opcReporteCoordinador<1 or opcReporteCoordinador>7:
                                opcReporteCoordinador=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))
                            bol45=False
                        except ValueError:
                            print("Ingresa una opcion valida (Numero)")

                    
                    if opcReporteCoordinador==1:

                        system("clear")

                        print("-----Campers en estado inscrito-----")

                        for j in range(len(archivo["Campers"])):

                            if archivo["Campers"][j]["estado"]=="Inscrito":
                                print("Estudiante:", archivo["Campers"][j]["nombres"])
                                print("ID:", archivo["Campers"][j]["id"])
                                
                            

                        confiRepoCoordi=input("Si quieres ver otro reporte escribe: si, de lo contrario presiona enter\n")
                        system("clear")

                    elif opcReporteCoordinador==2:
                        
                        system("clear")
                        print("-----Modulos-----")
                        for m in range(len(archivo["Campers"][0]["numeroModulo"])):#como todos los campers tiene la informacion de los modulos simplemente se escoge un estudiante y se usa el for para que muestre los modulos 
                            print(m+1,archivo["Campers"][0]["numeroModulo"][m])

                        bol46=True
                        while bol46==True:
                            try:
                                moduloRendimiento=int(input("Ingresa el numero del modulo actual\n"))
                                while moduloRendimiento<1 or moduloRendimiento>5:
                                    moduloRendimiento=int(input("Ingresa un modulo de los que aparecen en pantalla\n"))

                                bol46=False
                            except ValueError:
                                print("Ingresa un modulo valido (Numero)")

                            
                        system("clear")
                            
                        print("-----Campers que aprobaron-----")
                        cont1=0
                        for t in range(len(archivo["Campers"])):

                            if archivo["Campers"][t]["notaFiltro"][moduloRendimiento-1]>60.0:
                                print("------------------------------")
                                print("Estudiante:", archivo["Campers"][t]["nombres"])
                                print("ID:", archivo["Campers"][t]["id"])
                                print("------------------------------")
                                cont1=cont1+1
                            
                        if cont1==0:
                            print("\nNingun camper aprobo este modulo\n")




                        confiRepoCoordi=input("Si quieres ver otro reporte escribe: si, de lo contrario presiona enter\n")
                        system("clear")


                    elif opcReporteCoordinador==3:

                        system("clear")

                        print("-----Trainers-----")

                        for i in range(len(archivo["Trainers"])):
                            print("---------------------------")
                            print("Nombres",archivo["Trainers"][i]["nombres"])
                            print("ID",archivo["Trainers"][i]["id"])
                            print("---------------------------")

                        confiRepoCoordi=input("Si quieres ver otro reporte escribe: si, de lo contrario presiona enter\n")
                        system("clear")


                    elif opcReporteCoordinador==4:

                        system("clear")
                        print("-----Modulos-----")
                        for m in range(len(archivo["Campers"][0]["numeroModulo"])):#como todos los campers tiene la informacion de los modulos simplemente se escoge un estudiante y se usa el for para que muestre los modulos 
                            print(m+1,archivo["Campers"][0]["numeroModulo"][m])

                        bol46=True
                        while bol46==True:
                            try:
                                moduloRendimiento=int(input("Ingresa el numero del modulo actual\n"))
                                while moduloRendimiento<1 or moduloRendimiento>5:
                                    moduloRendimiento=int(input("Ingresa un modulo de los que aparecen en pantalla\n"))

                                bol46=False
                            except ValueError:
                                print("Ingresa un modulo valido (Numero)")
                            
                        system("clear")
                            
                        print("-----Campers que tienen bajo rendimiento-----")
                        cont=0
                        for t in range(len(archivo["Campers"])):

                            if archivo["Campers"][t]["notaFiltro"][moduloRendimiento-1]<60.0:
                                print("------------------------------")
                                print("Estudiante:", archivo["Campers"][t]["nombres"])
                                print("ID:", archivo["Campers"][t]["id"])
                                print("------------------------------")
                                cont=cont+1
                            
                        if cont==0:
                            print("\nNo hay campers con bajo rendimiento\n")




                        confiRepoCoordi=input("Si quieres ver otro reporte escribe: si, de lo contrario presiona enter\n")
                        system("clear")
                        
                    elif opcReporteCoordinador==6: 

                        system("clear")

                        print("\n///////////////////Modulo 1///////////////////\n")
                        print("-----Estudiantes que aprobaron-----")
                        contm1=0
                        for g in range(len(archivo["Campers"])):

                            if archivo["Campers"][g]["notaFiltro"][0]>60.0:
                                print("-------------------------")
                                print("Nombres:", archivo["Campers"][g]["nombres"])
                                print("ID:", archivo["Campers"][g]["id"])
                                print("-------------------------")
                                contm1=contm1+1
                            
                        if contm1==0:
                        
                            print("\nNingun estudiante aprobo este modulo\n")

                        print("-----Estudiantes que reprobaron-----")
                        contm1=0
                        for q in range(len(archivo["Campers"])):
                            if archivo["Campers"][q]["notaFiltro"][0]<60.0:
                                print("-------------------------")
                                print("Nombres:", archivo["Campers"][q]["nombres"])
                                print("ID:", archivo["Campers"][q]["id"])
                                print("-------------------------")
                                contm1=contm1+1
                            
                        if contm1==0:
                            print("\nNingun estudiante reprobo este modulo\n")

                        #############################################################

                        print("\n///////////////////Modulo 2///////////////////\n")
                        print("-----Estudiantes que aprobaron-----")
                        contm1=0
                        for w in range(len(archivo["Campers"])):
                            if archivo["Campers"][w]["notaFiltro"][1]>60.0:
                                print("-------------------------")
                                print("Nombres:", archivo["Campers"][w]["nombres"])
                                print("ID:", archivo["Campers"][w]["id"])
                                print("-------------------------")
                                contm1=contm1+1
                            
                        if contm1==0:
                            print("\nNingun estudiante aprobo este modulo\n")

                        print("-----Estudiantes que reprobaron-----")
                        contm1=0
                        for e in range(len(archivo["Campers"])):
                            if archivo["Campers"][e]["notaFiltro"][1]<60.0:
                                print("-------------------------")
                                print("Nombres:", archivo["Campers"][e]["nombres"])
                                print("ID:", archivo["Campers"][e]["id"])
                                print("-------------------------")
                                contm1=contm1+1
                            
                        if contm1==0:
                            print("\nNingun estudiante reprobo este modulo\n")

                        #############################################################

                        print("\n///////////////////Modulo 3///////////////////\n")
                        print("-----Estudiantes que aprobaron-----")
                        contm1=0
                        for w in range(len(archivo["Campers"])):
                            if archivo["Campers"][w]["notaFiltro"][2]>60.0:
                                print("-------------------------")
                                print("Nombres:", archivo["Campers"][w]["nombres"])
                                print("ID:", archivo["Campers"][w]["id"])
                                print("-------------------------")
                                contm1=contm1+1
                            
                        if contm1==0:
                            print("\nNingun estudiante aprobo este modulo\n")

                        print("-----Estudiantes que reprobaron-----")
                        contm1=0
                        for e in range(len(archivo["Campers"])):
                            if archivo["Campers"][e]["notaFiltro"][2]<60.0:
                                print("-------------------------")
                                print("Nombres:", archivo["Campers"][e]["nombres"])
                                print("ID:", archivo["Campers"][e]["id"])
                                print("-------------------------")
                                contm1=contm1+1
                            
                        if contm1==0:
                            print("\nNingun estudiante reprobo este modulo\n")

                        #############################################################

                        print("\n///////////////////Modulo 4///////////////////\n")
                        print("-----Estudiantes que aprobaron-----")
                        contm1=0
                        for w in range(len(archivo["Campers"])):
                            if archivo["Campers"][w]["notaFiltro"][3]>60.0:
                                print("-------------------------")
                                print("Nombres:", archivo["Campers"][w]["nombres"])
                                print("ID:", archivo["Campers"][w]["id"])
                                print("-------------------------")
                                contm1=contm1+1
                            
                        if contm1==0:
                            print("\nNingun estudiante aprobo este modulo\n")

                        print("-----Estudiantes que reprobaron-----")
                        contm1=0
                        for e in range(len(archivo["Campers"])):
                            if archivo["Campers"][e]["notaFiltro"][3]<60.0:
                                print("-------------------------")
                                print("Nombres:", archivo["Campers"][e]["nombres"])
                                print("ID:", archivo["Campers"][e]["id"])
                                print("-------------------------")
                                contm1=contm1+1
                            
                        if contm1==0:
                            print("\nNingun estudiante reprobo este modulo\n")

                        #############################################################

                        print("\n///////////////////Modulo 5///////////////////\n")
                        print("-----Estudiantes que aprobaron-----")
                        contm1=0
                        for w in range(len(archivo["Campers"])):
                            if archivo["Campers"][w]["notaFiltro"][4]>60.0:
                                print("-------------------------")
                                print("Nombres:", archivo["Campers"][w]["nombres"])
                                print("ID:", archivo["Campers"][w]["id"])
                                print("-------------------------")
                                contm1=contm1+1
                            
                        if contm1==0:
                            print("\nNingun estudiante aprobo este modulo\n")

                        print("-----Estudiantes que reprobaron-----")
                        contm1=0
                        for e in range(len(archivo["Campers"])):
                            if archivo["Campers"][e]["notaFiltro"][4]<60.0:
                                print("-------------------------")
                                print("Nombres:", archivo["Campers"][e]["nombres"])
                                print("ID:", archivo["Campers"][e]["id"])
                                print("-------------------------")
                                contm1=contm1+1
                            
                        if contm1==0:
                            print("\nNingun estudiante reprobo este modulo\n")

                        confiRepoCoordi=input("Si quieres ver otro reporte escribe: si, de lo contrario presiona enter\n")
                        system("clear")

                    elif opcReporteCoordinador==7:

                        
                         

                        confiRepoCoordi=""        
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
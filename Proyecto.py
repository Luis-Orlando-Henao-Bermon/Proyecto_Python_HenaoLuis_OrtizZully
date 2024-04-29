import json 

with open("./Campusland.json", encoding="utf-8") as file:#con esto se abre el archivo de campusland.json que es donde esta toda la informacion
    archivo=json.load(file)

user=input("Ingrese el usuario\n")#se pide que ingrese el usuario

x=0#esto es para saber si hay alguien con ese usuario ya que si hay alguien con ese usuario x se volvera 1 y se terminara el bucle de while 

while x==0:#si no hay nadie con el usuario ingresado x seguira siendo 0 por lo tanto se repetira el bucle while (antes de repetir el bucle se pide que se ingrese de nuevo el usuario para poder ver si el ingresado nuevamente esta o no )
    for i in range(len(archivo["Campers"])):#se usa un bucle for para recorra cada una  de las pociciones de los campers

        if user in archivo["Campers"][i]["user"]["login"]:#se miran todas las pociciones de los campers y si el usuario (login) alguno de ellos coinciden con el ingresado x pasa a valer 1 y se rompe el bucle de while 

            x+=1
            passwordCamper=input("Ingresa la contraseña\n")#despues de saber cual es el camper con ese usuario se le pide la contraseña 

            while passwordCamper not in archivo["Campers"][i]["user"]["contraseña"]:#se usa un bucle while porque mientras que la contraseña ingresada no este en archivo["Campers"][i]["user"]["contraseña"] (que es la direcion en donde esta la contraseña en el archivo) se repetira el bucle que lo que hace es volver a pedirle la contraseña 
                passwordCamper=input("Contraseña incorrecta ingresela otra vez\n")
            
            print("Bienvenido",archivo["Campers"][i]["nombres"] )    

    for q in range(len(archivo["Trainers"])):#se usa un bucle for para recorra cada una  de las pociciones de los trainers
        if user in archivo["Trainers"][q]["user"]["login"]:

            x+=1
            passwordTrainer=input("Ingresa la contraseña\n")
            
            while passwordTrainer not in archivo["Trainers"][q]["user"]["contraseña"]:
                passwordTrainer=input("Contraseña incorrecta ingresela otra vez\n")

            print("Bienvenido",archivo["Trainers"][q]["nombres"])
            
            

    if user in archivo["Coordinador"]["user"]["login"]:#como se sabe que solo hay un coordinador mira si en coordinador esta ese usuario ingresado 

        x+=1
        passwordCoordinador=input("Ingresa la contraseña\n")

        while passwordCoordinador not in archivo["Coordinador"]["user"]["contraseña"]:
            passwordCoordinador=input("Contraseña incorrecta ingresela otra vez\n")
        
        print("Bienvenido",archivo["Coordinador"]["nombres"])

    if x==0:
        user=input("No se encontro el usuario ingreselo nuevamente\n")



json_archivo=json.dumps(archivo)
with open("./Campusland.json","w") as files:
    files.write(json_archivo)
#Desarrollado por Luis Henao c.c. 1093904929 y Zully Ortiz c.c.1092528097
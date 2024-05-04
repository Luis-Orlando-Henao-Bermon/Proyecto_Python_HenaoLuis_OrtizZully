"""

                    print("-----Materias del modulo 3-----")#se muestran las materias que hay para el modulo 3
                    for i in range(len(archivo["Coordinador"][1]["materiasM3"])):
                        print(archivo[""Coordinador""][1]["materiasM3"][i])

                    #como se pueden agregar 2 materias se piden solo 2
                    modulo3Agregar1=input("Ingresa las 1 materia que quieres agregar\n")#se pide la primera materia del modulo tres 

                    while modulo3Agregar1 not in archivo["Coordinador"][1]["materiasM3"]:# mientras la materia ingresada no se encuentre en materiasM3 se le pedire que ingrese una materia valida  
                        modulo3Agregar1=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")

                    archivo["Coordinador"][1]["tiposDeRutas][len(archivo["Coordinador"][1]["rutas")-1]["modulos"][2].append(modulo3Agregar1)

                    modulo3Agregar2=input("Ingresa las 2 materia que quieres agregar\n")#se pide la segunda materia del modulo tres 
                    while modulo3Agregar2 not in archivo["Coordinador"][1]["materiasM3"]:# mientras la materia ingresada no se encuentre en materiasM3 se le pedire que ingrese una materia valida  
                        modulo3Agregar2=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")

                    archivo["Coordinador"][1]["tiposDeRutas][len(archivo["Coordinador"][1]["rutas")-1]["modulos"][2].append(modulo3Agregar2)

                    system("clear")

                    #como se pueden agregar 2 materias se piden solo 2
                    print("-----Materias del modulo 4-----")#se muestran las materias que hay para el modulo 4
                    for i in range(len(archivo["Coordinador"][1]["materiasM4"])):
                        print(archivo["Coordinador"][1]["materiasM4"][i])

                    modulo4Agregar1=input("Ingresa las 1 materia que quieres agregar\n")#se pide la primera materia del modulo 4
                    while modulo4Agregar1 not in archivo["Coordinador"][1]["materiasM4"]:# mientras la materia ingresada no se encuentre en materiasM3 se le pedire que ingrese una materia valida  
                        modulo4Agregar1=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")

                    archivo["Coordinador"][1]["tiposDeRutas][len(archivo["Coordinador"][1]["rutas")-1]["modulos"][3].append(modulo4Agregar1)

                    modulo4Agregar2=input("Ingresa las 2 materia que quieres agregar\n")#se pide la segunda materia del modulo 4
                    while modulo4Agregar2 not in archivo["Coordinador"][1]["materiasM4"]:# mientras la materia ingresada no se encuentre en materiasM3 se le pedire que ingrese una materia valida  
                        modulo4Agregar2=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")

                    archivo["Coordinador"][1]["tiposDeRutas][len(archivo["Coordinador"][1]["rutas")-1]["modulos"][3].append(modulo4Agregar2)


                    system("clear")

                    #como se pueden agregar 2 materias se piden solo 2
                    print("-----Materias del modulo 5-----")#se muestran las materias que hay para el modulo 5
                    for i in range(len(archivo["Coordinador"][1]["materiasM5"])):
                        print(archivo["Coordinador"][1]["materiasM5"][i])

                    modulo5Agregar1=input("Ingresa las 1 materia que quieres agregar\n")#se pide la primera materia del modulo 5
                    while modulo5Agregar1 not in archivo["Coordinador"][1]["materiasM5"]:# mientras la materia ingresada no se encuentre en materiasM3 se le pedire que ingrese una materia valida  
                        modulo5Agregar1=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")

                    archivo["Coordinador"][1]["tiposDeRutas][len(archivo["Coordinador"][1]["rutas")-1]["modulos"][4].append(modulo5Agregar1)

                    modulo5Agregar2=input("Ingresa las 2 materia que quieres agregar\n")#se pide la segunda materia del modulo 5
                    while modulo5Agregar2 not in archivo["Coordinador"][1]["materiasM5"]:# mientras la materia ingresada no se encuentre en materiasM3 se le pedire que ingrese una materia valida  
                        modulo5Agregar2=input("Ingresa una materia valida (Tienes que escribirla como aparece en Materias del modulo 3)\n")

                    archivo["Coordinador"][1]["tiposDeRutas][len(archivo["Coordinador"][1]["rutas")-1]["modulos"][4].append(modulo5Agregar2)


"""



{
    "nombreRuta": "",
    "grupos": [
        ""
    ],
    "modulos": [
        [
            "Introduccion a la algoritmo",
            "Pseint",
            "Python"
        ],
        [
            "HTML",
            "CSS",
            "Bootstrap"
        ],
        [],
        [],
        []
    ]
}
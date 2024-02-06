carreras = []
seguir = True

while(seguir):
    try:
        print("------------ Menu ---------------")
        print("1. Agregar carrera")
        print("2. Mostrar carrera")
        print("3. Actualizar carrera")
        print("4. Eliminar carrera")
        print("5. Menu clases")
        print("6. Salir")
        opcion = int(input("Seleccione una opcion: "))
    except:
        print("Opcion no valida.")
    else:
        match(opcion):
            case 1:
                carrera = {}
                nombre_carrera = input("Ingrese el nombre de la carrera: ")
                carrera['carrera'] = nombre_carrera
                carreras.append(carrera)
                print("Carrera agregada correctamente.")
            case 2:
                print("Lista de carreras: ")
                for carrera in carreras:
                    print(f"Nombre: " + carrera['carrera'])
            case 3:
                nombre_carrera = input("Ingrese el nombre de la carrera: ")
                nuevo_nombre = input("Ingrese el nuevo nombre de la carrera: ")

                for carrera in carreras:
                    if carrera['carrera'] == nombre_carrera:
                        carrera['carrera'] = nuevo_nombre
                        print("Carrera actualizada correctamente.")
            case 4:
                nombre_eliminar = input("Nombre de la carrera que desea eliminar: ")

                encontrado = False
                indice = 0
                for carrera in carreras:
                    if carrera['carrera'] == nombre_eliminar:
                        encontrado = True
                        break
                    else:
                        indice += 1
                if encontrado:
                    carreras.remove(carreras[indice])
                else:
                    print("Carrera no encontrada.")
            case 5:
                seguir_clase = True
                while(seguir_clase):
                    try:
                        print("1. Agregar clases")
                        print("2. Mostrar clases")
                        print("3. Actualizar clases")
                        print("4. Eliminar clases")
                        print("5. Salir")
                        opcion_clase = int(input("Seleccione una opcion: "))
                    except:
                        print("Opcion no valida.")
                    else:
                        match(opcion_clase):
                            case 1:
                                nombre_carrera = input("Ingrese el nombre de la carrera para agregar clases: ")
                                
                                for carrera in carreras:
                                    if carrera['carrera'] == nombre_carrera:
                                        nombre_clase = input("Ingrese el nombre de la clase: ")
                                        if 'clases' not in carrera:
                                            carrera['clases'] = []
                                        carrera['clases'].append(nombre_clase)
                                    print("Clase agregada correctamente.")
                                    break
                            case 2:
                                nombre_carrera = input("Ingrese el nombre de la carrera: ")

                                for carrera in carreras:
                                    if carrera['carrera'] == nombre_carrera:
                                        if carrera['clases']:
                                            print("Clases: ")
                                            for clase in carrera['clases']:
                                                print(f" - {clase}")
                                        else:
                                            print("No hay clases registradas.")
                                        break
                                else:
                                    print("No encontrado.")
                            case 3:
                                nombre_carrera = input("Ingrese el nombre de la carrera: ")
                                nombre_clase = input("Ingrese el nombre de la clase")
                                nuevo_nombre = input("Ingrese el nuevo nombre de la clase: ")

                                for carrera in carreras:
                                    if carrera['carrera'] == nombre_carrera:
                                        for i, clase in enumerate(carrera['clases']):
                                            if clase == nombre_clase:
                                                carrera['clases'][i] = nuevo_nombre
                                                print("Carrera modificada correctamente.")
                                                break
                                        else:
                                            print("Clase no encontrado.")
                                        break
                                else:
                                    print("Carrera no encontrada.")
                            case 4:
                                nombre_carrera = input("Ingrese el nombre de la carrera: ")
                                nombre_eliminar = input("Ingrese el nombre de la clase que desea eliminar: ")

                                for carrera in carreras:
                                    if carrera['carrera'] == nombre_carrera:                #for carrera in carreras:                                                                             
                                        for i, clase in enumerate(carrera['clases']):       #   if carrera['carrera'] == nombre_carrera:                                                                              
                                            if clase == nombre_eliminar:                    #       if nombre_eliminar in carrera['clases']:                                                                           
                                                carrera['clases'].pop(i)                    #           carrera['clases'].remove(nombre_eliminar)                                                                       
                                                print("Clase borrada correctamente.")       #           print("Clase eliminada correctamente.")                                                                       
                                                break                                       #        else:                                                        
                                        else:                                               #             print("Clase no encontrada")                                                                                                           
                                            print("Clase no encontrada.")                   #        break
                                        break
                                else:
                                    print("Carrera no encontrada.")
                            case 5:
                                print("Hasta la proxima.")
                                seguir_clase = False
            case 6:
                print("Saliendo....")
                seguir = False
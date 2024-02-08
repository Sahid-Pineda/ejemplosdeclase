carreras = []

def agregar_carrera():
    carrera = {}
    carrera['carrera'] = input("Ingrese el nombre de la carrera: ")
    carreras.append(carrera)
    print("Carrera agregada correctamente.")
  
def agregar_clase():
    nombre_carrera = input("Ingrese el nombre de la carrera: ")
    for carrera in carreras:
        if carrera['carrera'] == nombre_carrera:
            nombre_clase = input("Ingrese el nombre de la clase: ")
            if 'clases' not in carrera:
                carrera['clases'] = []
            carrera['clases'].append(nombre_clase)

def mostrar():
    nombre_carrera = input("Ingrese el nombre de la carrera: ")
    for carrera in carreras:
        print(f"Carrera: {carrera['carrera']}")
        if carrera['carrera'] == nombre_carrera:
            for clase in carrera['clases']:
                print(f"-Clases de la carrera  {nombre_carrera}: {clase}")

def menu():
    try:
        tipo_menu = int(input("\n1.Carrera\n2.Clase\nTipo de menu: "))
        if tipo_menu == 1:
            tipo_menu = "Carrera"
        elif tipo_menu == 2:
            tipo_menu = "Clase"

        print(f"\n---------Menu {tipo_menu} ------------")
        print(f"1. Agregar {tipo_menu}")
        print(f"2. Mostrar {tipo_menu}")
        print(f"3. Actualizar {tipo_menu}")
        print(f"4. Eliminar {tipo_menu}")
        print("5. Salir")
        opcion = int(input("Seleccione una opcion: "))
    except:
        print("Opcion no valida.")
    else:
        match opcion:
            case 1:
                if tipo_menu == "Carrera":
                    agregar_carrera()
                elif tipo_menu == "Clase":
                    agregar_clase()
            case 2:
                mostrar()
            case 5:
                seguir = False
            case default:
                print("Opcion no valida.")

seguir = True

while(seguir):
    menu()
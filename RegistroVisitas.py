class Persona:
    # - ID: int
    # - nombre1: string
    # - nombre2: string
    # - apellido1: string
    # - apellido2: string
    # - direccion: string

    def __init__(self, id, nombre1, nombre2, apellido1, apellido2, direccion):
        self.__id = id
        self.__nombre1 = nombre1
        self.__nombre2 = nombre2
        self.__apellido1 = apellido1
        self.__apellido2 = apellido2
        self.__direccion = direccion
        self._tipo = ""

    #Setters
    def setId(self, id):
        self.__id = id
    
    def setNombre1(self, nombre1):
        self.__nombre1 = nombre1

    def setNombre2(self, nombre2):
        self.__nombre2 = nombre2

    def setApellido1(self, apellido1):
        self.__apellido1 = apellido1

    def setApellido2(self, apellido2):
        self.__apellido2 = apellido2

    def setDireccion(self, direccion):
        self.__direccion = direccion

    #Getters
    def getId(self):
        return self.__id
    
    def getNombre1(self):
        return self.__nombre1
    
    def getNombre2(self):
        return self.__nombre2
    
    def getApellido1(self):
        return self.__apellido1
    
    def getApellido2(self):
        return self.__apellido2
    
    def getDireccion(self):
        return self.__direccion
    
    def __str__(self):
        return f"\nTipo: {self._tipo}\nIdentidad: {self.getId()}\nNombre Completo: {self.getNombre1()} {self.getNombre2()} {self.getApellido1()} {self.getApellido2()}\nDirección: {self.getDireccion()}"

class Empleados(Persona):
    # - Numero de Empleado: int

    def __init__(self, id, nombre1, nombre2, apellido1, apellido2, direccion, nEmpleado):
        super().__init__(id, nombre1, nombre2, apellido1, apellido2, direccion)
        self.__nEmpleado = nEmpleado

    #Setters
    def setNEmpleado(self, nEmpleado):
        self.__nEmpleado = nEmpleado

    #Getters
    def getNEmpleado(self):
        return self.__nEmpleado
    
    def __str__(self):
        return super().__str__() + f"\nNo. Empleado: {self.getNEmpleado()}"
    
class Maestro(Empleados):
    # - Facultad: string
    # - Especializacion: string

    def __init__(self, id, nombre1, nombre2, apellido1, apellido2, direccion, nEmpleado, facultad, especializacion):
        super().__init__(id, nombre1, nombre2, apellido1, apellido2, direccion, nEmpleado)
        self.__facultad = facultad
        self.__especializacion = especializacion
        self._tipo = "Maestro"

    #Setters
    def setFacultad(self, facultad):
        self.__facultad = facultad

    def setEspecializacion(self, especializacion):
        self.__especializacion = especializacion

    #Getters
    def getFacultad(self):
        return self.__facultad
    
    def getEspecializacion(self):
        return self.__especializacion
    
    def __str__(self):
        return Empleados.__str__(self) + f"\nFacultad: {self.getFacultad()}\nEspecialización: {self.getEspecializacion()}"
    
class Administrativo(Empleados):
    # - Area: string
    # - Campo: string

    def __init__(self, id = 123, nombre1 = '', nombre2= '', apellido1 = '', apellido2= '', direccion = '', nEmpleado = 456, area = '', campo= ''):
        super().__init__(id, nombre1, nombre2, apellido1, apellido2, direccion, nEmpleado)
        self.__area = area
        self.__campo = campo
        self._tipo = "Administrativo"

    #Setters
    def setArea(self, area):
        self.__area = area

    def setCampo(self, campo):
        self.__campo = campo

    #Getters
    def getArea(self):
        return self.__area
    
    def getCampo(self):
        return self.__campo
    
    def __str__(self):
        return Empleados.__str__(self) + f"\nÁrea: {self.getArea()}\nCampo: {self.getCampo()}"
    
class Alumno(Persona):
    # - Carrera: string
    # - Horario: string
    # - Numero de Cuenta: int

    def __init__(self, id, nombre1, nombre2, apellido1, apellido2, direccion, carrera, horario, nCuenta):
        super().__init__(id, nombre1, nombre2, apellido1, apellido2, direccion)
        self.__carrera = carrera
        self.__horario = horario
        self.__nCuenta = nCuenta
        self._tipo = "Alumno"

    #Setters
    def setCarrera(self, carrera):
        self.__carrera = carrera

    def setHorario(self, horario):
        self.__horario = horario

    def setNCuenta(self, nCuenta):
        self.__nCuenta = nCuenta

    #Getters
    def getCarrera(self):
        return self.__carrera
    
    def getHorario(self):
        return self.__horario
    
    def getNCuenta(self):
        return self.__nCuenta
    
    def __str__(self):
        return super().__str__() + f"\nCarrera: {self.getCarrera()}\nHorario: {self.getHorario()}\nNo. de Cuenta: {self.getNCuenta()}"
    
class Visitas(Persona):
    # - Razon Visita: string
    # - Edificio: string

    def __init__(self, id, nombre1, nombre2, apellido1, apellido2, direccion, razonVisita, edificio):
        super().__init__(id, nombre1, nombre2, apellido1, apellido2, direccion)
        self.__razonVisita = razonVisita
        self.__edificio = edificio
        self._tipo = "Visita"

    #Setters
    def setRazonVisita(self, razonVisita):
        self.__razonVisita = razonVisita

    def setEdificio(self, edificio):
        self.__edificio = edificio

    #Getters
    def getRazonVisita(self):
        return self.__razonVisita
    
    def getEdificio(self):
        return self.__edificio
    
    def __str__(self):
        return super().__str__() + f"\nRazón de Visita: {self.getRazonVisita()}\nEdificio: {self.getEdificio()}"
    
class Jefe(Maestro, Administrativo):
    # - Fecha de Inicio: string
    # - Fecha Fin: string
    # - Jefe: boolean
    def __init__(self, id, nombre1, nombre2, apellido1, apellido2, direccion, nEmpleado, facultad, especializacion, fechaInicio, fechaFin, jefe):
        Maestro.__init__(self, id, nombre1, nombre2, apellido1, apellido2, direccion, nEmpleado, facultad, especializacion)
        Administrativo.__init__(self, id, nombre1, nombre2, apellido1, apellido2, direccion, nEmpleado)
        self.__fechaInicio = fechaInicio
        self.__fechaFin = fechaFin
        self.__jefe = bool(jefe)
        self._tipo = "Jefe"

    #Setters
    def setFechaInicio(self, fechaInicio):
        self.__fechaInicio = fechaInicio

    def setFechaFin(self, fechaFin):
        self.__fechaFin = fechaFin

    def setJefe(self, jefe):
        self.__jefe = jefe

    #Getters
    def getFechaInicio(self):
        return self.__fechaInicio
    
    def getFechaFin(self):
        return self.__fechaFin
    
    def getJefe(self):
        return self.__jefe
    
    def __str__(self):
        return Maestro.__str__(self) + f"\nFecha de Inicio: {self.getFechaInicio()}\nFecha Fin: {self.getFechaFin()}\nJefe: {self.getJefe()}"
    
class Registro:
    def __init__(self):
        self.__visitas = []

    def Agregar(self, tipo):
        print("\n\tREGISTRANDO INFORMACIÓN")
        id = int(input("Ingrese su número de Identidad: "))
        nombre1 = input("Ingrese su primer nombre: ")
        nombre2 = input("Ingrese su segundo nombre: ")
        apellido1 = input("Ingrese su primer apellido: ")
        apellido2 = input("Ingrese su segundo apellido: ")
        direccion = input("Ingrese su dirección: ")

        if tipo == 1: # Agregando Empleado
            nEmpleado = int(input("Ingrese su número de Empleado: "))
            rol = int(input("\n1. Si es Maestro\n2. Si es Administrativo\n3. Si es Jefe\nSeleccione una opción: "))
            if rol == 1:
                facultad = input("\nIngrese su Facultad: ")
                especializacion = input("Ingrese su Especialización: ")
                nuevo_maestro = Maestro(id, nombre1, nombre2, apellido1, apellido2, direccion, nEmpleado, facultad, especializacion)
                self.__visitas.append(nuevo_maestro)
            elif rol == 2:
                area = input("\nIngrese su área: ")
                campo = input("Ingrese su campo: ")
                nuevo_administrativo = Administrativo(id, nombre1, nombre2, apellido1, apellido2, direccion, nEmpleado, area, campo)
                self.__visitas.append(nuevo_administrativo)
            elif rol == 3:
                facultad = input("\nIngrese su Facultad: ")
                especializacion = input("Ingrese su Especialización: ")
                # areaBoss = input("Ingrese su área: ")
                # campoBoss = input("Ingrese su campo: ")
                fechaInicio = input("Ingrese su Fecha de inicio en el cargo: ")
                fechaFin = input("Ingrese su Fecha Fin en el cargo: ")
                identificarCargo = input("Si es Jefe escriba 'j', si es Coordinador escriba 'c': ")
                jefe = identificarCargo.lower() == 'j'
                nuevo_jefe = Jefe(id, nombre1, nombre2, apellido1, apellido2, direccion, nEmpleado, facultad, especializacion, fechaInicio, fechaFin, jefe)
                self.__visitas.append(nuevo_jefe)
        elif tipo == 2: #Agregando Alumno
            carrera = input("Ingrese el nombre de la carrera: ")
            horario = input("Ingrese horario: ")
            nCuenta = input("Ingrese su No. de Cuenta: ")
            nuevo_alumno = Alumno(id, nombre1, nombre2, apellido1, apellido2, direccion, carrera, horario, nCuenta)
            self.__visitas.append(nuevo_alumno)
        elif tipo == 3: #Agregando Visita
            razonVisita = input("Ingrese razón de visita: ")
            edificio = input("Ingrese el edificio al que se dirige: ")
            nueva_visita = Visitas(id, nombre1, nombre2, apellido1, apellido2, direccion, razonVisita, edificio)
            self.__visitas.append(nueva_visita)
        else:
            print("Opcion no válida.")
        print("Registrado correctamente.")

    def Mostar(self):
        print("\nINFORMACION DEL REGISTRO DE INGRESO")
        for visita in self.__visitas:
            print(visita)

    def Modificar(self):
        pass

    def Eliminar(self):
        pass

visitas = Registro()

seguir = True

while(seguir):
    try:
        print("\n------ Menu ------")
        print("1. Registrar Visitante")
        print("2. Mostrar Visitantes")
        print("3. Actualizar Información Visitantes")
        print("4. Eliminar Visitante")
        print("5. Salir")
        opcion = int(input("Seleccione una opción: "))
    except:
        print("Opcion no valida")
    else:
        match opcion:
            case 1:
                tipo = int(input("\n1. Empleado\n2. Alumno\n3. Visitante\nSeleccione una opción: "))
                visitas.Agregar(tipo)
            case 2:
                visitas.Mostar()
            case 3:
                pass
            case 4:
                pass
            case 5:
                print("Saliendo...")
                seguir = False
            case default:
                print("Opción no válida")
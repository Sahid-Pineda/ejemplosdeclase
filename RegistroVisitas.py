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
    
class Maestro(Empleados):
    # - Facultad: string
    # - Especializacion: string

    def __init__(self, id, nombre1, nombre2, apellido1, apellido2, direccion, nEmpleado, facultad, especializacion):
        super().__init__(id, nombre1, nombre2, apellido1, apellido2, direccion, nEmpleado)
        self.__facultad = facultad
        self.__especializacion = especializacion

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
    
class Administrativo(Empleados):
    # - Area: string
    # - Campo: boolean

    def __init__(self, id, nombre1, nombre2, apellido1, apellido2, direccion, nEmpleado, area, campo = False):
        super().__init__(id, nombre1, nombre2, apellido1, apellido2, direccion, nEmpleado)
        self.__area = area
        self.__campo = campo

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
    
class Alumno(Persona):
    # - Carrera: string
    # - Horario: string
    # - Numero de Cuenta: int

    def __init__(self, id, nombre1, nombre2, apellido1, apellido2, direccion, carrera, horario, nCuenta):
        super().__init__(id, nombre1, nombre2, apellido1, apellido2, direccion)
        self.__carrera = carrera
        self.__horario = horario
        self.__nCuenta = nCuenta

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
    
class Visitas(Persona):
    # - Razon Visita: string
    # - Edificio: string

    def __init__(self, id, nombre1, nombre2, apellido1, apellido2, direccion, razonVisita, edificio):
        super().__init__(id, nombre1, nombre2, apellido1, apellido2, direccion)
        self.__razonVisita = razonVisita
        self.__edificio = edificio

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
    
class Jefe(Maestro, Administrativo):
    # - Fecha de Inicio: string
    # - Fecha Fin: string
    # - Jefe: boolean

    def __init__(self, id, nombre1, nombre2, apellido1, apellido2, direccion, nEmpleado, facultad, especializacion, fechaInicio, fechaFin, jefe = False):
        super().__init__(id, nombre1, nombre2, apellido1, apellido2, direccion, nEmpleado, facultad, especializacion)
        self.__fechaInicio = fechaInicio
        self.__fechaFin = fechaFin
        self.__jefe = jefe

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


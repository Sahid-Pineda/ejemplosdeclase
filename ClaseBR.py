class Cuarto:
    #Numero de Ventanas
    #Medidas
    def __init__(self, numeroVentanas, medidas):
        self.__numeroVentanas = numeroVentanas
        self.__medidas = medidas

    #Setters
    def setNumeroVentanas(self, numeroVentanas):
        self.__numeroVentanas = numeroVentanas

    def setMedidas(self, medidas):
        self.__medidas = medidas    
    
    #Getters
    def getNumeroVentanas(self):
        return self.__numeroVentanas

    def getMedidas(self):
        return self.__medidas 

class Sala:
    #Chimenea
    #Descripción
    def __init__(self, chimenea, descripcion):
        self.__chimenea = chimenea
        self.__descripcion = descripcion

    #Setters    
    def setChimenea(self, chimenea):
        self.__chimenea = chimenea
    
    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    #Getters
    def getChimenea(self):
        return self.__chimenea
    
    def getDescripcion(self):
        return self.__descripcion
    
class Lavatrasto:
    #Depositos
    #Agua-Caliente
    def __init__(self, depositos, aguaCaliente):
        self.__depositos = depositos
        self.__aguaCaliente = aguaCaliente
    
    #Setters
    def setDepositos(self, depositos):
        self.__depositos = depositos

    def setAguaCaliente(self, aguaCaliente):
        self.__aguaCaliente = aguaCaliente

    #Getters
    def getDepositos(self):
        return self.__depositos
    
    def getAguaCaliente(self):
        return self.__aguaCaliente

class Patio:
    #Área de Socialización
    #Medidas
    #Descripción
    def __init__(self, areaSocializacion, medidas, descripcion):
        self.__areaSocializacion = areaSocializacion
        self.__medidas = medidas
        self.__descripcion = descripcion

    #Setters
    def setAreaSocializacion(self, areaSocializacion):
        self.__areaSocializacion = areaSocializacion
    
    def setMedidas(self, medidas):
        self.__medidas = medidas
    
    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    #Getters
    def getAreaSocializacion(self):
        return self.__areaSocializacion
    
    def getMedidas(self):
        return self.__medidas
    
    def getDescripcion(self):
        return self.__descripcion

class Estado:
    # Nombre
    # Fecha
    def __init__(self, nombre, fecha):
        self.__nombre = nombre
        self.__fecha = fecha

    #Setters
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def setFecha(self, fecha):
        self.__fecha = fecha
    
    #Getters
    def getNombre(self):
        return self.__nombre

    def getFecha(self):
        return self.__fecha
class Casa:
    #Direccion
    #Descripcion
    def __init__(self, direccion, descripcionCasa):
        self.__direccion = direccion
        self.__descripcionCasa = descripcionCasa
        self.cuartos = []
        self.salas = []
        self.cocinas = []
        self.patios = []
        self.estados = []

    #Setters
    def setDireccion(self, direccion):
        self.__direccion = direccion
    
    def setDescripcion(self, descripcionCasa):
        self.__descripcionCasa = descripcionCasa

    #Getters
    def getDireccion(self):
        return self.__direccion
    
    def getDescripcion(self):
        return self.__descripcionCasa

class Cocina:
    #Electrodomésticos Incluidos
    #Medidas
    #Material Desayunador
    def __init__(self, electrodomesticos, medidas, materialDesayunador) -> None:
        self.__electrodomesticos = electrodomesticos
        self.__medidas = medidas
        self.__materialDesayunador = materialDesayunador
        self.lavatrastos = []

    #Setters
    def setElectrodomesticos(self, electrodomesticos):
        self.__electrodomesticos = electrodomesticos

    def setMedidas(self, medidas):
        self.__medidas = medidas

    def setMaterialDesayunador(self, materialDesayunador):
        self.__materialDesayunador = materialDesayunador
    
    #Getters
    def getEletrodomesticos(self):
        return self.__electrodomesticos
    
    def getMedidas(self):
        return self.__medidas
    
    def getMaterialDesayunador(self):
        return self.__materialDesayunador
    
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
    #Descripción Sala
    def __init__(self, chimenea, descripcionSala):
        self.__chimenea = chimenea
        self.__descripcionSala = descripcionSala

    #Setters    
    def setChimenea(self, chimenea):
        self.__chimenea = chimenea
    
    def setDescripcionSala(self, descripcionSala):
        self.__descripcionSala = descripcionSala

    #Getters
    def getChimenea(self):
        return self.__chimenea
    
    def getDescripcion(self):
        return self.__descripcionSala
    
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
    def __init__(self, areaSocializacion, medidas, descripcionPatio):
        self.__areaSocializacion = areaSocializacion
        self.__medidas = medidas
        self.__descripcionPatio = descripcionPatio

    #Setters
    def setAreaSocializacion(self, areaSocializacion):
        self.__areaSocializacion = areaSocializacion
    
    def setMedidas(self, medidas):
        self.__medidas = medidas
    
    def setDescripcion(self, descripcionPatio):
        self.__descripcionPatio = descripcionPatio

    #Getters
    def getAreaSocializacion(self):
        return self.__areaSocializacion
    
    def getMedidas(self):
        return self.__medidas
    
    def getDescripcion(self):
        return self.__descripcionPatio

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
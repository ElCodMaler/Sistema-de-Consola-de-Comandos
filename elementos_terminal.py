import datetime
#La clase fichero
class Fichero:
    #constructor del fichero
    def __init__(self,id=0 , nombre="", extencion="", peso=0, datos=""):
        #si no existe el valor del ID de la clase fichero, entonces se le asigna, de lo contrario no puede cambiar el ID
        if(self.id == None):
            self.id = id
            self.fechaCreada = self.fecha()
        self.nombre = nombre
        self.peso = peso
        self.extencion = extencion
        self.fechaModificada = self.fecha()
        self.datos = datos
    #metodo fecha, donde se usa la clase datatime para retornar la fecha y hora actuales
    def fecha(self):
        fechaActual = datetime.datetime.now()
        return fechaActual
#La clase carpeta
class Carpeta:
    #constructor de la carpeta
    def __init__(self,id=0 , nombre="", listaFicheros = [], listaCarpetas = [], pesoTotal=0):
        #si no existe el valor del ID de la clase fichero, entonces se le asigna, de lo contrario no puede cambiar el ID
        if(self.id == None):
            self.id = id
            self.fechaCreada = datetime.datetime.now()
        self.nombre = nombre
        self.listaFicheros = listaFicheros
        self.listaCarpetas = listaCarpetas
        self.pesoTotal = pesoTotal
#clase unidad
class Unidad:
    #constructor de la unidad
    def __init__(self,id=0 , nombre="C:", capacidadTotal = 400, espacioDisponible = 400, listaCarpetas = [], tipo = "HDD"):
        #si no existe el valor del ID de la clase fichero, entonces se le asigna, de lo contrario no puede cambiar el ID
        if(self.id == None):
            self.id = id
            self.fechaCreada = datetime.datetime.now()
        self.nombre = nombre
        self.capacidadTotal = capacidadTotal
        self.espacioDisponible = espacioDisponible
        self.listaCarpetas = listaCarpetas
        self.tipo = tipo
class Persona:

    def __init__(self, nombre = '', apellido = '', fechaNacimiento = '') -> None:
        self.__Nombre       = nombre
        self.__Apellido     = apellido
        self.__FNacimiento  = fechaNacimiento

    def getNombre(self):

        return self.__Nombre

    def setNombre(self, nombre):

        self.__Nombre = nombre

    def getApellido(self):

        return self.__Apellido

    def setApellido(self, apellido):

        self.__Apellido = apellido

    def getFNacimiento(self):

        return self.__FNacimiento

    def setFNacimiento(self, fechaNacimiento):

        self.__FNacimiento = fechaNacimiento


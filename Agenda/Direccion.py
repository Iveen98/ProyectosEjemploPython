class Direccion:

    def __init__(self, calle = '', piso = '', ciudad = '', codigoPostal = '') -> None:
        self.__Calle        = calle
        self.__Piso         = piso
        self.__Ciudad       = ciudad
        self.__CodigoPostal = codigoPostal

    def getCalle(self):

        return self.__Calle

    def setCalle(self, calle):

        self.__Calle = calle

    def getPiso(self):

        return self.__Piso

    def setPiso(self, piso):

        self.__Piso = piso

    def getCiudad(self):

        return self.__Ciudad

    def setCiudad(self, ciudad):

        self.__Ciudad = ciudad

    def getCodigoPostal(self):

        return self.__CodigoPostal

    def setCodigoPostal(self, codigoPostal):

        self.__CodigoPostal = codigoPostal


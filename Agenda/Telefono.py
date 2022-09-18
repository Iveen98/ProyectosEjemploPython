class Telefono:

    def __init__(self, tMovil = '', tTrabajo = '', tFijo = '') -> None:
        self.__TMovil   = tMovil
        self.__TTrabajo = tTrabajo
        self.__TFijo    = tFijo

    def getTMovil(self):

        return self.__TMovil

    def setTMovil(self, tMovil):

        self.__TMovil = tMovil

    def getTTrabajo(self):

        return self.__TTrabajo

    def setTTrabajo(self, tTrabajo):

        self.__TTrabajo = tTrabajo

    def getTFijo(self):

        return self.__TFijo

    def setTFijo(self, tFijo):

        self.__TFijo = tFijo

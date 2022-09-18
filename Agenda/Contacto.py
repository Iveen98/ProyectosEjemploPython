from Direccion import Direccion
from Persona import Persona
from Telefono import Telefono

class Contacto(Direccion,Persona,Telefono):

    def __init__(self, email = "") -> None:
        self.__Email   = email

    def getEmail(self):

        return self.__Email

    def setEmail(self, email):

        self.__Email = email        

    def mostrarContacto(self):

        devolver = "Nombre : " + self.getNombre() + " \n "
        devolver = devolver + "Apellido : " + self.getApellido() + " \n "
        devolver = devolver + "Fecha Nacimiento : " + self.getFNacimiento() + " \n "
        devolver = devolver + "Correo : " + self.getEmail() + " \n "
        devolver = devolver + "Calle : " + self.getCalle() + " \n "
        devolver = devolver + "Piso : " + self.getPiso() + " \n "
        devolver = devolver + "Ciudad : " + self.getCiudad() + " \n "
        devolver = devolver + "CodigoPostal : " + self.getCodigoPostal() + " \n "
        devolver = devolver + "Telofono Movil : " + self.getTMovil() + " \n "
        devolver = devolver + "Telefono Trabajo  : " + self.getTTrabajo() + " \n "
        devolver = devolver + "Telefono Fijo  : " + self.getTFijo()

        return devolver
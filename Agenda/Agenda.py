from Contacto import Contacto
from io import BufferedReader, BufferedWriter
import os

class Agenda:

    def __init__(self, listaContacto = [], path = os.getcwd() + "\\agenda.txt") -> None:
        self.__ListaContacto    = listaContacto
        self.__Path             = path

    def getListaContacto(self):

        return self.__ListaContacto

    def setListaContacto(self, listaContacto):

        self.__ListaContacto = listaContacto

    def getPath(self):

        return self.__Path

    def setPath(self, path):

        self.__Path = path

    def cargarContacto(self):

        if (os.path.exists(self.__Path)):

            f  : BufferedReader = open(self.__Path, "r")

            lineas = f.readlines()

            for linea in lineas :

                self.__crearContactoFichero(linea)

            f.close()

    def __crearContactoFichero(self, linea):

        datos = linea.split(";")

        #Correo,Calle,Piso,Ciudad,CodigoPostal,Nombre,Apellido,FellaNacimiento,TMovil,TTrabajo,TFijo
        contacto : Contacto = Contacto()

        contacto.setEmail(datos[0])
        contacto.setCalle(datos[1])
        contacto.setPiso(datos[2])
        contacto.setCiudad(datos[3])
        contacto.setCodigoPostal(datos[4])
        contacto.setNombre(datos[5])
        contacto.setApellido(datos[6])
        contacto.setFNacimiento(datos[7])
        contacto.setTMovil(datos[8])
        contacto.setTTrabajo(datos[9])
        contacto.setTFijo(datos[10])

        self.__ListaContacto.append(contacto)
    
    def crearContacto(self):

        correo      = input("Correo Electronico : ")
        calle       = input("Calle : ")
        piso        = input("Piso : ")
        ciudad      = input("Ciudad : ")
        cPostal     = input("Codigo Postal : ")
        nombre      = input("Nombre : ")
        apellido    = input("Apellido : ")
        fNacimiento = input("Fecha Nacimiento : ")
        tMovil      = input("Telefono Movil : ")
        tTrabajo    = input("Telefono Trabajo : ")
        tFijo       = input("Telefono Fijo : ")

        contacto : Contacto = Contacto(correo)
        contacto.setCalle(calle)
        contacto.setPiso(piso)
        contacto.setCiudad(ciudad)
        contacto.setCodigoPostal(cPostal)
        contacto.setNombre(nombre)
        contacto.setApellido(apellido)
        contacto.setFNacimiento(fNacimiento)
        contacto.setTMovil(tMovil)
        contacto.setTTrabajo(tTrabajo)
        contacto.setTFijo(tFijo)

        self.__ListaContacto.append(contacto)

    def guardarContactos(self):

        # Crear Fichero
        try: 
        
            f : BufferedWriter = open(self.__Path,"w+")

        except FileExistsError:

            print("ya esta creado")

        else:

            for contacto in self.__ListaContacto :

                contacto : Contacto = contacto

                linea  = contacto.getEmail() + ";" + contacto.getCalle() + ";" + contacto.getPiso() + ";" + contacto.getCiudad() + ";" + contacto.getCodigoPostal() + ";" + contacto.getNombre() + ";" + contacto.getApellido() + ";" + contacto.getFNacimiento() + ";" + contacto.getTMovil() + ";" + contacto.getTTrabajo() + ";" + contacto.getTFijo()

                f.write(linea)

            f.flush()

            f.close()

    def mostrarAgenda(self):

        for contacto in self.__ListaContacto :

            contacto : Contacto = contacto

            print("----------------CONTACTO--------------")

            print(contacto.mostrarContacto())

            print("--------------------------------------")

    def buscarContactoPorNombre(self, nombre):

        for contacto in self.__ListaContacto : 

            if (contacto.getNombre().lower() == nombre.lower()):

                print("----------------CONTACTO--------------")

                print(contacto.mostrarContacto())

                print("--------------------------------------")

    def borrarContactoPorNombre(self, nombre):

        posicion = 0
        salir = False

        while (posicion < len(self.__ListaContacto) and not(salir)):

            contacto : Contacto = self.__ListaContacto[posicion]

            if (contacto.getNombre().lower() == nombre.lower()):

                salir = True
                print("Contacto a Borrar : " , nombre)
                self.__ListaContacto.pop(posicion)

            posicion += 1

        if (not(salir)): 

            print("Contacto no encontrado")

    def buscarContactoPorNumero(self, telefono):

        for contacto in self.__ListaContacto : 

            if (contacto.getTMovil().lower() == telefono.lower()):

                print("----------------CONTACTO--------------")

                print(contacto.mostrarContacto())

                print("--------------------------------------")

    def borrarContactoPorNumero(self, telefono):

        posicion = 0
        salir = False

        while (posicion < len(self.__ListaContacto) and not(salir)):

            contacto : Contacto = self.__ListaContacto[posicion]

            if (contacto.getTMovil().lower() == telefono.lower()):

                salir = True
                print("Contacto a Borrar : " , telefono)
                self.__ListaContacto.pop(posicion)

            posicion += 1

        if (not(salir)): 

            print("Contacto no encontrado")
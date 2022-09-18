
from Agenda import Agenda

def borrarContacto():

    salir = False

    while not(salir):

        print("Por Nombre -- 1")
        print("Por Telefono -- 2")

        print("Volver -- 3")

        numero = int(input("Escriba el numero del 1 al 3: "))

        if (type(numero) is int):

            if (numero == 1) :

                agenda.borrarContactoPorNombre(input("Nombre : "))

                salir = True

            elif (numero == 2) :

                agenda.borrarContactoPorNumero(input("Telefono : "))

                salir = True

            elif (numero == 3) :

                salir = True

            else:

                print("Por favor escriba número dentro del rango del 1 al 3\n\n")

        else:

            print("Escribar un numero correcto :(\n\n") 

def buscarContacto():

    salir = False

    while not(salir):

        print("Por Nombre -- 1")
        print("Por Telefono -- 2")

        print("Volver -- 3")

        numero = int(input("Escriba el numero del 1 al 3: "))

        if (type(numero) is int):

            if (numero == 1) :

                agenda.buscarContactoPorNombre(input("Nombre : "))

                salir = True

            elif (numero == 2) :

                agenda.buscarContactoPorNumero(input("Telefono : "))

                salir = True

            elif (numero == 3) :

                salir = True

            else:

                print("Por favor escriba número dentro del rango del 1 al 3\n\n")

        else:

            print("Escribar un numero correcto :(\n\n")

print("Bienvenido a la Agenda :D \n")

agenda : Agenda = Agenda()
agenda.cargarContacto()

salir = False

while not(salir):

    print("Elija una de estas opciones :\n")
    print("Crear Contacto -- 1")
    print("Borrar Contacto -- 2")
    print("Buscar Contacto -- 3")
    print("Mostrar Agenda -- 4")
    print("Guardar Agenda -- 5")
    print("Salir -- 6")

    numero = int(input("Escriba el numero del 1 al 6: "))

    if (type(numero) is int):

        if (numero == 1) :

            agenda.crearContacto()

        elif (numero == 2) :

            borrarContacto()

        elif (numero == 3) :

            buscarContacto()

        elif (numero == 4) :

            agenda.mostrarAgenda()

        elif (numero == 5) :

            agenda.guardarContactos()

        elif(numero == 6):

            salir = True

        else:

            print("Por favor escriba número dentro del rango del 1 al 6\n\n")

    else:

        print("Escribar un numero correcto :(\n\n")

   
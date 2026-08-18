from clase_jugadores import Jugador, crear_seleccion_inicial

ARCHIVO_CONVOCADOS = "convocados_argentina.txt"


def leer_archivo(nombre_archivo):
    # Leo el archivo al iniciar el programa para recuperar los datos de los jugadores convocados por default
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    # Estas lineas contendran los datos de los primeros jugadores convocados que vienen de la funcion crear_selecccion_inicial 
    lineas = archivo.readlines() #readlines me devuelve una lista de lineas de texto del archivo 
    archivo.close()
    return lineas #retorno la lista de lineas de texto del archivo para poder utilizarlo en el metodo cargar_convocados_txt


def guardar_archivo(nombre_archivo, convocados):
    # con write sobreescribo el archivo a medida que se van convocando jugadores y asi evito duplicados
    archivo = open(nombre_archivo, "w", encoding="utf-8")
    # Recorro la lista de convocados y con el metodo write escribo en el archivo los datos de cada jugador
    for jugador in convocados:
        archivo.write(f"{jugador.nombre},{jugador.apellido},{jugador.posicion},{jugador.club}\n")
    archivo.close()

# al momento de ejecutar el codigo, recibira la seleccion por default 
# porque este metodo al ejecutarse tendra como parametro la variable que almacena la funcion crear_seleccion_inicial de clase_jugadores
def cargar_convocados_txt(seleccion):
    seleccion.convocados = []
    lineas = leer_archivo(ARCHIVO_CONVOCADOS) # en lineas tengo alojado los datos de los jugadores convocados por default

    for linea in lineas: #recorro la lista de lineas
        # datos es una lista de strings que contiene los datos de cada jugador separados por comas
        datos = linea.strip().split(",")
        # si el largo de la lista datos es 4, significa que tiene los datos de un jugador completo
        if len(datos) == 4:
            nombre, apellido, posicion, club = datos
            # creo un objeto jugador con los datos de cada jugador utilizando la clase Jugador
            jugador = Jugador(nombre, apellido, posicion, club)
            # convoco el jugador
            seleccion.convocar(jugador)

# metodo para quitar un jugador
# recorre la lista de convocados seleccion.convocados y compara con los datos introducidos por el usuario
def quitar_jugador(seleccion, nombre, apellido):
    nombre = nombre.strip().title() # elimino espacios y convierto a mayusculas
    apellido = apellido.strip().title()
    for jugador in seleccion.convocados:
        # si los datos del jugador coinciden con los datos del jugador a quitar, lo elimino
        if jugador.nombre == nombre and jugador.apellido == apellido: 
            seleccion.convocados.remove(jugador) 
            return True
    return False


def mostrar_menu():
    print("\n--- MENU ---")
    print("1 - Mostrar plantel")
    print("2 - Convocar jugador")
    print("3 - Quitar jugador por lesion")
    print("0 - Salir")


if __name__ == "__main__":
    # Creo el archivo si no existe
    open(ARCHIVO_CONVOCADOS, "a", encoding="utf-8").close()

    sel_argentina = crear_seleccion_inicial() # Llamo a la funcion crear_seleccion_inicial de clase_jugadores.py
    cargar_convocados_txt(sel_argentina) # Le paso como parametro la seleccion por default al metodo cargar_convocados_txt  

    # Si el archivo esta vacio, creo la seleccion inicial y guardo los convocados en el archivo
    # sel_argentina.convocados es una lista de objetos de la clase Jugador
    if len(sel_argentina.convocados) == 0:
        sel_argentina = crear_seleccion_inicial()
        guardar_archivo(ARCHIVO_CONVOCADOS, sel_argentina.convocados)

    while True:
        mostrar_menu()
        opcion = input("Opcion: ").strip()

        if opcion == "1":
            print("\nPlantel actual:\n")
            print(sel_argentina.mostrar_convocados())

        elif opcion == "2":
            nombre = input("Nombre: ").strip()
            apellido = input("Apellido: ").strip()
            posicion = input("Posicion: ").strip().title()
            club = input("Club: ").strip()

            jugador_nuevo = Jugador(nombre, apellido, posicion, club)
            sel_argentina.convocar(jugador_nuevo) # Llamo al metodo convocar de la clase SeleccionFutbol
            guardar_archivo(ARCHIVO_CONVOCADOS, sel_argentina.convocados) # Paso el ARCHIVO_CONVOCADOS y la lista de convocados para guardarlos en el archivo
            print("Jugador convocado y guardado.")

        elif opcion == "3":
            nombre = input("Nombre del lesionado: ").strip()
            apellido = input("Apellido del lesionado: ").strip()

            # 
            if quitar_jugador(sel_argentina, nombre, apellido):
                # Una vez quitado el jugador utilizo el metodo guardar_archivo para actualizar el mismo 
                guardar_archivo(ARCHIVO_CONVOCADOS, sel_argentina.convocados)
                print("Jugador quitado y archivo actualizado.")
            else:
                print("No se encontro ese jugador.")

        elif opcion == "0":
            print("Saliendo del sistema")
            break

        else:
            print("Opcion invalida.")

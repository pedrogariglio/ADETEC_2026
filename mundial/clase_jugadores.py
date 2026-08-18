from clase_seleccion_futbol import SeleccionFutbol


class Jugador:
    """Clase que representa a un jugador de fútbol."""

    def __init__(self, nombre, apellido, posicion, club, edad=None):
        self.nombre = nombre.strip().title()
        self.apellido = apellido.strip().title()
        self.posicion = posicion.strip().title()
        self.club = club.strip()
        self.edad = edad

    #metodo string para definir como se imprime una instancia de la clase Jugador o sea un objeto
    #por ejemplo si imprimo un objeto jugador, se imprimira el nombre, apellido, posicion y club
    def __str__(self):
        if self.edad is None:
            return f"{self.nombre} {self.apellido} - {self.posicion} ({self.club})"
        return (
            f"{self.nombre} {self.apellido} - {self.posicion} "
            f"({self.club}, {self.edad} años)"
        )

#con esta funcion creo la seleccion inicial y convoco los jugadores iniciales
def crear_seleccion_inicial():
    #creo el objeto seleccion_argentina que es una instancia de la clase SeleccionFutbol
    seleccion_argentina = SeleccionFutbol("Argentina", "Lionel Scaloni", 3)

    jugadores_iniciales = [
        Jugador("Lionel", "Messi", "Delantero", club="Inter Miami"),
        Jugador("Julian", "Alvarez", "Delantero", club="Atletico Madrid"),
        Jugador("Emiliano", "Martinez", "Arquero", club="Aston Villa"),
        Jugador("Cristian", "Romero", "Defensor", club="Tottenham"),
        Jugador("Enzo", "Fernandez", "Mediocampista", club="Chelsea"),
    ]

    #recorro la lista de jugadores_iniciales
    #si el jugador pertenece a la lista, lo convoco utilizando el metodo convocar de la clase SeleccionFutbol
    for jugador in jugadores_iniciales:
        seleccion_argentina.convocar(jugador) 

    #retorno el objeto seleccion_argentina para poder utilizarlo mas adelante (en el main)
    return seleccion_argentina

#ejecucion del programa (demo aparte no escribe el archivo convocados.txt)
if __name__ == "__main__":
  
    seleccion_argentina = crear_seleccion_inicial()
    print(seleccion_argentina)
    print("Jugadores convocados:\n")
    #imprimo los jugadores convocados con el metodo mostrar_convocados de la clase SeleccionFutbol
    print(seleccion_argentina.mostrar_convocados())

    
    for _ in range(3):
        print("\nConvocar jugador:")
        nombre = input("Ingrese el nombre del jugador: ")
        apellido = input("Ingrese el apellido del jugador: ")
        posicion = input("Ingrese la posicion del jugador: ")
        edad_texto = input("Ingrese la edad del jugador (opcional): ").strip()
        club = input("Ingrese el club del jugador: ")

        edad = int(edad_texto) if edad_texto.isdigit() else None
        #creo el objeto jugador con los datos ingresados por el usuario
        jugador = Jugador(nombre=nombre, apellido=apellido, posicion=posicion, club=club, edad=edad)
        #sumo al jugador a la lsita de convocados utilizando el metodo convocar de la clase SeleccionFutbol
        seleccion_argentina.convocar(jugador)

    print("\nConvocados actualizados:\n")
    print(seleccion_argentina.mostrar_convocados())


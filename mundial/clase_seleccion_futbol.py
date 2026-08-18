class SeleccionFutbol:
    """Clase que representa una selección de fútbol."""

    POSICIONES_VALIDAS = ("Arquero", "Defensor", "Mediocampista", "Delantero")

    def __init__(self, nacionalidad, director_tecnico, titulos_mundiales):
        self.nacionalidad = nacionalidad
        self.director_tecnico = director_tecnico
        self.titulos_mundiales = titulos_mundiales
        self.convocados = []
        
    def convocar(self, jugador):
        if jugador not in self.convocados: #evito duplicados 
            self.convocados.append(jugador)

    def mostrar_convocados(self):
        #creo un diccionario que tiene por clave la posicion del jugador y por valor una lista vacia
        agrupados = {posicion: [] for posicion in self.POSICIONES_VALIDAS}
        #recorro los jugadores convocados y con getattr obtengo el atributo posicion
        for jugador in self.convocados:
            #getattr (objeto, atributo, valor_por_defecto)
            #posicion es un atributo de la clase Jugador
            posicion = getattr(jugador, "posicion", "").strip().title()
            #chequeo que el atributo posicion este como clave en el diccionario agrupados
            if posicion in agrupados:
                #si existe esa posicion agrego con .append al jugador a la lista con su respectiva clave posicion
                agrupados[posicion].append(jugador)
        
        #en esta lista almacenare los jugadores convocados agrupados por posicion
        #seria una lista de objetos Jugador con sus respectivos atributos
        lineas = []
        #recorro las posiciones validas
        for posicion in self.POSICIONES_VALIDAS:
            #agrego la posicion a la lsita
            lineas.append(f"{posicion}s:")
            #chequeo que la posicion tenga jugadores convocados
            if agrupados[posicion]:
                #si hay jugadores convocados, en esa posicion, recorro la lista
                for jugador in agrupados[posicion]:
                    #a esa lista de jugadpres convocados en esa posicion, agrego el nombre, apellido y club
                    lineas.append(f"- {jugador.nombre} {jugador.apellido} ({jugador.club})")
            else:
                lineas.append("- Sin convocados")
            #linea vacia para separar las posiciones visualmente
            lineas.append("")
        #retorno la lista lineas (con los convocados agrupados por posicion)     
        #elimino espacios en blanco y con join concateno las lineas
        return "\n".join(lineas).rstrip() #

    #metodo string que retorna todo la informacion (nacionalidad, director tecnico y titulos mundiales)
    def __str__(self):
        return (
            f"Seleccion de {self.nacionalidad} con director tecnico "
            f"{self.director_tecnico} y {self.titulos_mundiales} titulos mundiales."
        )

from datetime import timedelta

class Equipo:
    def __init__(self, nombre, iniciales, logo = ''):
        self.nombre = nombre
        self.iniciales = iniciales
        self.logo = logo

    def __str__(self):
        return self.nombre + '(' + self.iniciales + ')'

class Partido:
    def __init__(self, fecha, equipos = [], ganador = None):
        self.equipos = equipos
        self.fecha = fecha
        self.ganador = ganador
    
    def __str__(self):
        if self.ganador == None:
            return str(self.equipos[0]) + ' vs ' + str(self.equipos[1])
        else:
            return str(self.equipos[0]) + ' vs ' + str(self.equipos[1]) + '\tGanador: ' + str(self.ganador)

class Eliminatoria:
    def __init__(self, equipos = [], partidos = [], ganador = None):
        self.partidos = partidos
        self.equipos = equipos
        self.ganador = ganador

    def __str__(self):
        if self.ganador == None:
            return 'Eliminatoria: ' + str(self.equipos[0]) + ' vs ' + str(self.equipos[1])
        else:
            return 'Eliminatoria: ' + str(self.equipos[0]) + ' vs ' + str(self.equipos[1]) + '\tGanador: ' + str(self.ganador)
<<<<<<< HEAD

    def nuevo_partido(self, equipo1, equipo2, fecha):
        Partido(fecha, [equipo1, equipo2])

    def nuevo_ganador(self):
        contador_equipo1 = 0
        contador_equipo2 = 0
        for equipo in self.partidos:
            if equipo == self.equipos[0]:
                contador_equipo1 += 1
            elif equipo == self.equipos[1]:
                contador_equipo2 += 1
                
            if contador_equipo1 == 4:
                return self.equipos[0]
            elif contador_equipo2 == 4:
                return self.equipos[1]

=======

    def nuevo_partido(self, equipo1, equipo2, fecha):
        Partido(fecha, [equipo1, equipo2])
>>>>>>> 2da130e1728fbbe5bdada2fa6ada5b4ff51d3ea4

class Temporada:
    def __init__(self, nombre, equipos = [], eliminatorias = []):
        self.nombre = nombre
        self.equipos = equipos
        self.eliminatorias = eliminatorias

    def __str__(self):
        string = 'Temporada: ' + self.nombre + '\n'
        for equipo in self.equipos:
            string += '\t' + str(equipo) + '\n'
        return string
    
    def nueva_eliminatoria(self, equipo1, equipo2, fecha):
        lista_partidos = []
        for i in range(4):
            lista_partidos.append(Partido(fecha, [equipo1, equipo2]))
            fecha += timedelta(days=2)
        self.eliminatorias.append(Eliminatoria([equipo1, equipo2], lista_partidos))
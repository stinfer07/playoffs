class Equipo:
    def __init__(self, nombre, iniciales):
        self.nombre = nombre
        self.iniciales = iniciales

    def __str__(self):
        return self.nombre + '(' + self.iniciales + ')'

class Partido:
    def __init__(self, ganador, fecha, equipos = []):
        self.equipos = equipos
        self.ganador = ganador
        self.fecha = fecha
    
    def __str__(self):
        return self.equipos[0] + ' vs ' + self.equipos[1] + '\nGanador: ' + self.ganador

class Eliminatoria:
    def __init__(self, ganador, equipos = [], partidos = []):
        self.partidos = partidos
        self.equipos = equipos
        self.ganador = ganador

    def __str__(self):
        return 'La eliminatoria se han jugado ' + str(len(self.resultado)) + '\nGanador: ' + self.ganador

    #def nuevo_partido(self):

class Temporada:
    def __init__(self, nombre, equipos = [], eliminatoias = []):
        self.nombre = nombre
        self.equipos = equipos
        self.eliminatorias = eliminatorias

    def __str__(self):
        string = 'Temporada: ' + self.nombre + '\n'
        for equipo in self.equipos:
            string += '\t' + str(equipo) + '\n'
        return string
    
    #def nueva_eliminatoria(self, ):
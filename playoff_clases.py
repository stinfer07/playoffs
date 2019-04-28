class Equipo:
    def __init__(self, nombre, iniciales, partidos_ganados = 0):
        self.nombre = nombre
        self.iniciales = iniciales
        self.partidos_ganados = partidos_ganados

    def __str__(self):
        return self.nombre + '(' + self.iniciales + ')'

class Partido:
    def __init__(self, ganador, equipos = []):
        self.equipos = equipos
        self.ganador = ganador
    
    def __str__(self):
        return self.equipos[0] + ' vs ' + self.equipos[1] + '\nGanador: ' + self.ganador

class Eliminatoria:
    def __init__(self, ganador, equipos = [], resultado = []):
        self.resultado = resultado
        self.equipos = equipos
        self.ganador = ganador

    def __str__(self):
        return 'La eliminatoria se han jugado ' + str(len(self.resultado)) + '\nGanador: ' + self.ganador

class Temporada:
    def __init__(self, nombre, equipos = [], resultados = []):
        self.nombre = nombre
        self.equipos = equipos
        self.resultados = resultados

    def __str__(self):
        string = 'Temporada: ' + self.nombre + '\n'
        for equipo in self.equipos:
            string += '\t' + str(equipo) + '\n'
        return string
        
    #def nuevo_resultado()):
    # Falta definir la introduccion de un nuevo resultado.

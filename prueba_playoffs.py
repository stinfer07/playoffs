from playoff_clases import *
from datetime import *

Warriors = Equipo('Golden State Warriors', 'GSW')
Clippers = Equipo('LA Clippers', 'LAC')
Rockets = Equipo('Houston Rockets', 'HOU')
Jazz = Equipo('Utah Jazz', 'UTA')
Blazers = Equipo('Portland Trail Blazers', 'POR')
Thunder = Equipo('Oklahoma City Thunder', 'OKC')
Nuggets = Equipo('Denver Nuggets', 'DEN')
Spurs = Equipo('San Antonio Spurs', 'SAS')
Bucks = Equipo('Milwaukee Bucks', 'MIL')
Pistons = Equipo('Detroit Pistons', 'DET')
Celtics = Equipo('Boston Celtics', 'BOS')
Pacers = Equipo('Indiana Pacers', 'IND')
Nets = Equipo('Brooklyn Nets', 'BKN')
Philadelphia = Equipo('Philadelphia 76ers', 'PHI')
Magic = Equipo('Orlando Magic', 'ORL')
Raptors = Equipo('Toronto Raptors', 'TOR')

partido_uno = [Warriors, Clippers]
partido_dos = [Rockets, Jazz]
partido_tres = [Blazers, Thunder]
partido_cuatro = [Nuggets, Spurs]
partido_cinco = [Bucks, Pistons]
partido_seis = [Celtics, Pacers]
partido_siete = [Nets, Philadelphia]
partido_ocho = [Magic, Raptors]

equipos = [Warriors, Clippers, Rockets, Jazz, Blazers, Thunder, Nuggets, 
           Spurs, Bucks, Pistons, Celtics, Pacers, Nets, Philadelphia, Magic, Raptors]

primer_partido = Eliminatoria(Warriors,[Partido(Warriors, partido_uno), Partido(Clippers, partido_uno), 
                                        Partido(Warriors, partido_uno), Partido(Warriors, partido_uno), 
                                        Partido(Clippers, partido_uno), Partido(Warriors, partido_uno)])

segundo_partido = Eliminatoria(Rockets, [Partido(Rockets, partido_dos), Partido(Rockets, [Rockets, Jazz]), 
                                        Partido(Rockets, [Rockets, Jazz]), Partido(Jazz, [Rockets, Jazz]), 
                                        Partido(Rockets, [Rockets, Jazz])])

t = Temporada('2018/19', equipos)
t.nueva_eliminatoria(Warriors, Clippers, date(2019, 4, 29))
for elim in t.eliminatorias:
    for partido in elim.partidos:
        partidos = Partido(date(2019, 4, 29), [Warriors, Clippers], Warriors)
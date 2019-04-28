from playoff_clases import *

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

equipos = [Warriors, Clippers, Rockets, Jazz, Blazers, Thunder, Nuggets, 
           Spurs, Bucks, Pistons, Celtics, Pacers, Nets, Philadelphia, Magic, Raptors]

primer_partido = Eliminatoria(Warriors,[Partido(Warriors, [Warriors, Clippers]), Partido(Clippers, [Warriors, Clippers]), 
                                        Partido(Warriors, [Warriors, Clippers]), Partido(Warriors, [Warriors, Clippers]), 
                                        Partido(Clippers, [Warriors, Clippers]), Partido(Warriors, [Warriors, Clippers])])

segundo_partido = Eliminatoria(Rockets, [Partido(Rockets, [Rockets, Jazz]), Partido(Rockets, [Rockets, Jazz]), 
                                        Partido(Rockets, [Rockets, Jazz]), Partido(Jazz, [Rockets, Jazz]), 
                                        Partido(Rockets, [Rockets, Jazz])])

t = Temporada('2018/19', equipos, [primer_partido, segundo_partido])
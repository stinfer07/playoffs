import tkinter as tk
import os
import pygubu
from playoff_clases import *
from tkinter import Label

class Application:
    def __init__(self, master, temporada):
        master.title("Playoffs NBA")
        self.temporada = temporada

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('principal.ui')

        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('principal', master)

        self.builder.get_object('equipo1').configure(text=temporada.equipos[0].iniciales)
        self.builder.get_object('equipo2').configure(text=temporada.equipos[1].iniciales)
        self.builder.get_object('equipo3').configure(text=temporada.equipos[2].iniciales)
        self.builder.get_object('equipo4').configure(text=temporada.equipos[3].iniciales)
        self.builder.get_object('equipo5').configure(text=temporada.equipos[4].iniciales)
        self.builder.get_object('equipo6').configure(text=temporada.equipos[5].iniciales)
        self.builder.get_object('equipo7').configure(text=temporada.equipos[6].iniciales)
        self.builder.get_object('equipo8').configure(text=temporada.equipos[7].iniciales)
        self.builder.get_object('equipo9').configure(text=temporada.equipos[8].iniciales)
        self.builder.get_object('equipo10').configure(text=temporada.equipos[9].iniciales)
        self.builder.get_object('equipo11').configure(text=temporada.equipos[10].iniciales)
        self.builder.get_object('equipo12').configure(text=temporada.equipos[11].iniciales)
        self.builder.get_object('equipo13').configure(text=temporada.equipos[12].iniciales)
        self.builder.get_object('equipo14').configure(text=temporada.equipos[13].iniciales)
        self.builder.get_object('equipo15').configure(text=temporada.equipos[14].iniciales)
        self.builder.get_object('equipo16').configure(text=temporada.equipos[15].iniciales)


        self.colocar_equipos()

    def colocar_equipos(self):
        print('hola')
        self.lblEquipo1 = Label(principal, text='hola')

if __name__ == '__main__':
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

    principal = tk.Tk()
    t = Temporada('2018/19', equipos)
    app = Application(principal, t)
    principal.mainloop()
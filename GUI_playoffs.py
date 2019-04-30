import tkinter as tk
import os
import pygubu
from playoff_clases import *
from tkinter import Label
import os

class Application:
    def __init__(self, master, temporada):
        master.title("Playoffs NBA")
        self.temporada = temporada

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        self.builder.add_from_file('principal.ui')

        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('principal', master)
        self.builder.connect_callbacks(self)

        self.builder.get_object('equipo1').configure(text=temporada.equipos[0].iniciales, image=temporada.equipos[0].img_logo)
        self.builder.get_object('equipo2').configure(text=temporada.equipos[1].iniciales, image=temporada.equipos[1].img_logo)
        self.builder.get_object('equipo3').configure(text=temporada.equipos[2].iniciales, image=temporada.equipos[2].img_logo)
        self.builder.get_object('equipo4').configure(text=temporada.equipos[3].iniciales, image=temporada.equipos[3].img_logo)
        self.builder.get_object('equipo5').configure(text=temporada.equipos[4].iniciales, image=temporada.equipos[4].img_logo)
        self.builder.get_object('equipo6').configure(text=temporada.equipos[5].iniciales, image=temporada.equipos[5].img_logo)
        self.builder.get_object('equipo7').configure(text=temporada.equipos[6].iniciales, image=temporada.equipos[6].img_logo)
        self.builder.get_object('equipo8').configure(text=temporada.equipos[7].iniciales, image=temporada.equipos[7].img_logo)
        self.builder.get_object('equipo9').configure(text=temporada.equipos[8].iniciales, image=temporada.equipos[8].img_logo)
        self.builder.get_object('equipo10').configure(text=temporada.equipos[9].iniciales, image=temporada.equipos[9].img_logo)
        self.builder.get_object('equipo11').configure(text=temporada.equipos[10].iniciales, image=temporada.equipos[10].img_logo)
        self.builder.get_object('equipo12').configure(text=temporada.equipos[11].iniciales, image=temporada.equipos[11].img_logo)
        self.builder.get_object('equipo13').configure(text=temporada.equipos[12].iniciales, image=temporada.equipos[12].img_logo)
        self.builder.get_object('equipo14').configure(text=temporada.equipos[13].iniciales, image=temporada.equipos[13].img_logo)
        self.builder.get_object('equipo15').configure(text=temporada.equipos[14].iniciales, image=temporada.equipos[14].img_logo)
        self.builder.get_object('equipo16').configure(text=temporada.equipos[15].iniciales, image=temporada.equipos[15].img_logo)

    def nuevo_formulario(self):
        self.builder2 = pygubu.Builder()
        self.builder2.add_from_file('principal.ui')
        self.top = tk.Toplevel(self.mainwindow)
        self.builder2.get_object('formulario', self.top)
        self.builder2.connect_callbacks(self)

        self.lista_equipos = []
        self.lista_jugadores = []

        for nombre in self.temporada.equipos:
            self.lista_equipos.append(nombre)

        self.builder2.get_object("cb_eq1")["values"] = self.lista_equipos
        self.builder2.get_object("cb_eq2")["values"] = self.lista_equipos

        def rEleccion(self):
        # Recupera el valor de la variable asociada a los radio button
            valor = self.builder.get_variable("eleccion").get()
            return valor

        def btnCancel(self):
            self.top.destroy()

        def btnAceptar(self):
            if self.builder2.get_object("cb_eq1").get() and self.builder2.get_object("cb_eq2").get():
                equipo1 = self.builder2.get_object("cb_eq1").get()
                equipo2 = self.builder2.get_object("cb_eq2").get()
                for eliminatoria in self.temporada.eliminatorias:
                    if [equipo1,equipo2] == eliminatoria.equipos:
                        for partido in eliminatoria.partidos:
                            print(partido)

            


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

    eliminatorias = [Eliminatoria([Warriors, Clippers]), 
                     Eliminatoria([Rockets, Jazz]), 
                     Eliminatoria([Blazers, Thunder]), 
                     Eliminatoria([Nuggets, Spurs]), 
                     Eliminatoria([Bucks, Pistons]), 
                     Eliminatoria([Celtics, Pacers]), 
                     Eliminatoria([Nets, Philadelphia]), 
                     Eliminatoria([Magic, Raptors])
                     ]

    principal = tk.Tk()

    # Se cargan las imágenes de logos
    lista_logos = []
    for equipo in equipos:
        equipo.img_logo = tk.PhotoImage(file="logos_resize/"+equipo.iniciales+".png")
        lista_logos.append(equipo.img_logo)

    t = Temporada('2018/19', equipos, eliminatorias)
    app = Application(principal, t)
    principal.mainloop()
    
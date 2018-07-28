# new metronome
import pygame 
from pygame.locals import * 
import pyaudio
import wave
import time
import sys
import select
import termios

pygame.init()
window = pygame.display.set_mode((1300,720))
pygame.display.set_caption("Metronomo de: ")
miFuente = pygame.font.Font(None,200)

class Metronome():
    def __init__(self, bpm, time_sig,loops, name, color):
        self.bpm = int(bpm)
        self.loops = int(loops)
        self.time_sig = int(time_sig)
        self.accent_file = "High Seiko SQ50.wav"
        self.beat_file = "Low Seiko SQ50.wav"
        self.name = str(name)
        self.color = int(color)


        # Prepare sound files
        self.p = pyaudio.PyAudio()
        high = wave.open(self.accent_file, "rb")
        low = wave.open(self.beat_file, "rb")

        self.stream = self.p.open(format=self.p.get_format_from_width(high.getsampwidth()),
                                  channels=high.getnchannels(),
                                  rate=high.getframerate(),
                                  output=True)

        self.high_data = high.readframes(2048)
        self.low_data = low.readframes(2048)

        print("bpm: {}, time_sig: {}".format(self.bpm, self.time_sig))
        return None

    def start_metronome(self):
        window.fill(paleta[self.color])
        texto = miFuente.render(self.name, 0, (0,0,0))
        window.blit(texto,(100,100))
        #pygame.draw.rect(window, (255,255,255), (0,10, 50,100))
        pygame.display.update()
        for beat in range(self.loops):
            for i in range(self.time_sig):
                if i % self.time_sig == 0:
                    self.stream.write(self.high_data)
                else:
                    self.stream.write(self.low_data)
                time.sleep(60 / self.bpm)

    def acelerate_metronome(self, velfin):
        bpm = self.bpm
        steps = (velfin - bpm)/(self.time_sig*self.loops) 
        window.fill(paleta[self.color])
        texto = miFuente.render(self.name, 0, (0,0,0))
        window.blit(texto,(100,100))
        #pygame.draw.rect(window, (255,255,255), (0,10, 50,100))
        pygame.display.update()
        for beat in range(self.loops):
            for i in range(self.time_sig):
                if i % self.time_sig == 0:
                    self.stream.write(self.high_data)
                else:
                    self.stream.write(self.low_data)
                time.sleep(60 / bpm)
                bpm += steps
    def decrease_metronome(self, velfin):
        bpm = self.bpm
        steps = (bpm - velfin)/(self.time_sig*self.loops) 
        window.fill(paleta[self.color])
        texto = miFuente.render(self.name, 0, (0,0,0))
        window.blit(texto,(100,100))
        #pygame.draw.rect(window, (255,255,255), (0,10, 50,100))
        pygame.display.update()
        for beat in range(self.loops):
            for i in range(self.time_sig):
                if i % self.time_sig == 0:
                    self.stream.write(self.high_data)
                else:
                    self.stream.write(self.low_data)
                time.sleep(60 / bpm)
                bpm -= steps   	


# Definiendo paleta de colores 
paleta = [pygame.Color(255, 87, 51), pygame.Color(255, 189, 51), pygame.Color(219, 255, 51) ,pygame.Color(117, 255, 51) ,pygame.Color(51, 255, 87) ,pygame.Color(51, 255, 189)]




#Ejecución


m = Metronome(100, 4, 2, "CUENTA REGRESIVA", 0)
m.start_metronome()

m = Metronome(100, 4, 8,"INTRO SOLO", 1 )
m.start_metronome()
m = Metronome(100, 4, 8,"INTRO ACELERANDO", 2 )
m.acelerate_metronome(140)
m = Metronome(140, 4, 16,"INTRO COMUNAL", 3 )
m.start_metronome()
m = Metronome(140, 4, 16,"VERSO", 4 )
m.start_metronome()
m = Metronome(140, 4, 16,"CORO", 5 )
m.start_metronome()
m = Metronome(140, 4, 16,"PUENTE SOLO", 0 )
m.start_metronome()
m = Metronome(140, 4, 16,"VERSO", 4 )
m.start_metronome()

m = Metronome(140, 4, 16,"CORO", 5 )
m.start_metronome()

m = Metronome(140, 4, 32,"Pseudo Final", 2 )
m.start_metronome()

m = Metronome(140, 4, 16,"CORO", 5 )
m.start_metronome()

m = Metronome(140, 4, 2 ,"Post - CORO", 5 )
m.start_metronome()

m = Metronome(140, 4, 4,"CAYENDO", 3 )
m.decrease_metronome(100)

m = Metronome(100, 4, 8 ,"Solo Guitarra", 0 )
m.start_metronome()



"""
# Cada sección de la cancion tendrá los siguientes parámetros
Metronome = (bpm, time_sig,loops, name, color)
bpm= beats por minuto
metrica = contedo de cuandos golpes hay por compas 
compaces = Número de compases para cada sección
nombre = Nombre de la sección para que aparezca en la pantalla
color = color de la pantalla
"""
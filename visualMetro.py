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


def cancion(file, li = 1, ls =100):
    song = open(file, "r")
    sections = []
    for section in song:
        sections.append(section.split(","))
    
    # INICIO DEL METRONOMO
    m = Metronome(int(sections[li-1][0]), int(sections[li-1][1]), 2, "CUENTA REGRESIVA", 0)
    m.start_metronome()

    try: 
        for section_i in range(li-1,ls):
            m = Metronome(int(sections[section_i][0]), int(sections[section_i][1]), int(sections[section_i][2]), sections[section_i][3], int(sections[section_i][4]))
            if len(sections[section_i]) == 5:
                m.start_metronome()            
            else:
                if sections[section_i][-2] == "decrease":
                    m.decrease_metronome(int((sections[section_i][-1])))
                else:
                    m.acelerate_metronome(int((sections[section_i][-1])))
    except: 
        pass

    # FIN DEL METRONOMO
    m = Metronome(int(sections[ls-1][0]), int(sections[ls-1][1]), 2, "FINAL DEL METRONOMO", 0)
    m.start_metronome()



cancion("test.txt",2,3)


"""
# Cada sección de la cancion tendrá los siguientes parámetros
Metronome = (bpm, time_sig,loops, name, color)
bpm= beats por minuto
metrica = contedo de cuandos golpes hay por compas 
compaces = Número de compases para cada sección
nombre = Nombre de la sección para que aparezca en la pantalla
color = color de la pantalla
"""
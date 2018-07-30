import pygame 
from pygame.locals import * 
import pyaudio
import wave
import time
import argparse

pygame.init()

# Definiendo paleta de colores 
paleta = [pygame.Color(255, 87, 51), pygame.Color(255, 189, 51), pygame.Color(219, 255, 51) ,pygame.Color(117, 255, 51) ,pygame.Color(51, 255, 87) ,pygame.Color(51, 255, 189)]

# Definiendo la pantalla
window = pygame.display.set_mode((1366,768))
miFuente = pygame.font.Font(None,200)

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

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
        blit_text(window, self.name, (100,280) , miFuente)
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
        blit_text(window, self.name, (100,280) , miFuente)
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
        blit_text(window, self.name, (100,280) , miFuente)
        pygame.display.update()
        for beat in range(self.loops):
            for i in range(self.time_sig):
                if i % self.time_sig == 0:
                    self.stream.write(self.high_data)
                else:
                    self.stream.write(self.low_data)
                time.sleep(60 / bpm)
                bpm -= steps   	


def cancion(file, li = 1, ls =100):
    song = open(file, "r")
    sections = []
    pygame.display.set_caption("Metronomo de: " + file)
    for section in song:
        sections.append(section.split(","))
    
    # INICIO DEL METRONOMO
    m = Metronome(int(sections[li-1][0]), int(sections[li-1][1]), 2, "Cuenta regresiva", 0)
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
    m = Metronome(int(sections[ls-1][0]), int(sections[ls-1][1]), 1, "Final del metrónomo", 0)
    m.start_metronome()


parser = argparse.ArgumentParser()
parser.add_argument("file", help="select the file of the song",
                    type=str)
parser.add_argument("-s", "--start", help="select the section where start the metronome",
                    type=int, default= 1)
parser.add_argument("-e", "--end", help="select the section where the metronome end",
                    type=int, default = 100)

args = parser.parse_args()

### Ejecutando la canción 
cancion(args.file, args.start, args.end)



"""
### Cada sección de la cancion tendrá los siguientes parámetros
Metronome = (bpm, time_sig,loops, name, color)
bpm= beats por minuto
metrica = contedo de cuandos golpes hay por compas 
compaces = Número de compases para cada sección
nombre = Nombre de la sección para que aparezca en la pantalla
color = color de la pantalla

# Adicionalmente si es que necesitas una sección que cambie de velocidad, 
puede añadir 2 parametros al final

change, FSpeed 

change = Puede tomar 2 valores, "acelerate" o "decrease", para acelerar o disminuir la velocidad respectivamente
FSpeed = Es la velocidad final a la que se quiere llegar una vez terminada la transición 
"""
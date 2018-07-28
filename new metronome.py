# new metronome
import pygame 
from pygame.locals import * 
import pyaudio
import wave
import time
import argparse
import sys
import select
import termios

pygame.init()
window = pygame.display.set_mode((600,480))
pygame.display.set_caption("Metronomo de: ")

while True:
	for evento_i in pygame.event.get():
		if evento_i == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()




class Metronome():
    def __init__(self, bpm, time_sig, accent_file, beat_file, loops):
        self.bpm = int(bpm)
        self.loops = int(loops)
        self.time_sig = int(time_sig)
        self.accent_file = accent_file
        self.beat_file = beat_file
        self.pause_flag = False

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

    def metronome(self):
        for beat in range(self.loops):
            for i in range(self.time_sig):
                if self.pause_flag:
                    continue
                if i % self.time_sig == 0:
                    self.stream.write(self.high_data)
                else:
                    self.stream.write(self.low_data)
                time.sleep(60 / self.bpm)



parser = argparse.ArgumentParser()
parser.add_argument("-b", "--bpm", default=120)
parser.add_argument("-t", "--time_sig", default=4)
args = parser.parse_args()

TIME_SIG = args.time_sig
BPM = args.bpm

m = Metronome(BPM, TIME_SIG, r"High Seiko SQ50.wav", r"Low Seiko SQ50.wav", 4)
m.metronome()

m = Metronome(140, 4, r"High Seiko SQ50.wav", r"Low Seiko SQ50.wav", 8)
m.metronome()

### En esta parte vamos a poner la estructura de la canción
# ciudad y de mi gente 
Base = 145

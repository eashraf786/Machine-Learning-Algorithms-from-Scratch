import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pygame
import threading
import time
import librosa.display
import numpy as np
import sys
import os
import random
pygame.init()
fig, ax = plt.subplots(figsize=(10,5))
mode = 2
if mode == 1:
    file_path = "D:/MUSIC/Taare Ginn - A.R. Rahman  Mohit Chauhan  Shreya Ghoshal (128.mp3"
else:
    sng = os.listdir("D:/MUSIC/")
    rs = random.choice(sng)
    print(rs)
    file_path = os.path.join("D:/MUSIC/",rs)
song, sr = librosa.load(file_path)
ts = 60
lstep = 0.1
fr = np.arange(0,ts+lstep+0.0033,lstep+0.0033)
#ts = len(song)/22050
sound = pygame.mixer.Sound(file_path)
y = np.abs(librosa.stft(song[:ts*22050])) ** 2
y_log = librosa.power_to_db(y)
librosa.display.specshow(y_log, sr=sr, x_axis='time', y_axis='log',ax=ax)
vline = ax.axvline(x=0, color='r')
figon = True
def playsong():
    pygame.time.delay(3500)
    sound.play()
def on_close(event):
    sound.stop()
    plt.close()
fig.canvas.mpl_connect('close_event', on_close)
def update(num, vline):
    #print(num)
    vline.set_xdata(num)
    if num > ts:
        on_close(num)
    return [vline]
ani = animation.FuncAnimation(fig, update, frames=fr, fargs=[vline], interval=lstep*1000,blit=True)
song_thread = threading.Thread(target=playsong)
song_thread.start()
plt.show()

import pygame
from pygame.locals import*

# inicia o player
pygame.mixer.init(44100, -16, 2, 1024)

#Este configura el volumen del sonido 
pygame.mixer.music.set_volume(0.8)

 #Sonido numero uno
 #abriendo elprograma
 pygame.mixer.music.load("666.mp3")
        pygame.mixer.music.play()

#Sonido numero dos
#sonido del disapro 
  pygame.mixer.music.load("hit.mp3")
        pygame.mixer.music.play()


#sonido numero tres
#sonido de game over
pygame.mixer.music.load("gameover.mp3")
        pygame.mixer.music.play()
